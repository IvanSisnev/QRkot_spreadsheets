"""
Создание и заполнение таблицы Google Sheets c отчетом.
"""
from datetime import datetime

from aiogoogle import Aiogoogle

from app.core.config import settings
from app.models.charity_project import CharityProject
from app.core.constants import (DATE_FORMAT, REPORT_TITLE, LOCALE, SHEET_TYPE,
                                ROW_COUNT, COLUMN_COUNT, REPORT_DESCRIPTION,
                                COLUMN1_HEADER, COLUMN2_HEADER,
                                COLUMN3_HEADER, MAJOR_DIMENSION,
                                VALUE_INPUT_OPTION, TABLE_RANGE)
from app.services.utils import timedelta_to_str


# todo перенести в google_client?
async def set_user_permissions(spreadsheet_id: str,
                               wrapper_services: Aiogoogle) -> None:
    """
    Получить доступ к документу на Google Drive по id документа.
    """
    permissions_body = {'type': 'user',
                        'role': 'writer',
                        'emailAddress': settings.email}
    service = await wrapper_services.discover('drive', 'v3')
    await wrapper_services.as_service_account(
        service.permissions.create(fileId=spreadsheet_id,
                                   json=permissions_body,
                                   fields='id')
    )


async def spreadsheets_create(
        wrapper_services: Aiogoogle
) -> tuple[str, str]:
    """
    Создать таблицу, вернуть ее id и время создания
    """
    now_date_time = datetime.now().strftime(DATE_FORMAT)

    document_sheet_title: str = f'{REPORT_TITLE} {now_date_time}'

    service = await wrapper_services.discover('sheets', 'v4')

    spreadsheet_body = {
        'properties': {'title': f'{document_sheet_title}',
                       'locale': LOCALE},
        'sheets': [{'properties': {'sheetType': SHEET_TYPE,
                                   # todo
                                   # 'sheetId': 0,
                                   'title': f'{document_sheet_title}',
                                   'gridProperties': {
                                       'rowCount': ROW_COUNT,
                                       'columnCount': COLUMN_COUNT
                                   }
                                   }
                    }
                   ]
    }
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=spreadsheet_body)
    )
    spreadsheet_id = response['spreadsheetId'] # noqa
    return spreadsheet_id, now_date_time


async def spreadsheets_update_value(spreadsheet_id: str,
                                    now_date_time: str,
                                    closed_projects: list[CharityProject],
                                    wrapper_services: Aiogoogle) -> None:
    """
    Заполнить таблицу данными.
    """
    service = await wrapper_services.discover('sheets', 'v4')
    table_values = [
        [REPORT_TITLE, now_date_time],
        [REPORT_DESCRIPTION],
        [COLUMN1_HEADER, COLUMN2_HEADER, COLUMN3_HEADER]
    ]
    for project in closed_projects:
        # перевожу разницу во времени в строковое значение заданного формата
        completion_rate: str = await timedelta_to_str(
            project.close_date - project.create_date
        )
        new_row = [project.name, completion_rate, project.description]
        table_values.append(new_row)

    update_body = {
        'majorDimension': MAJOR_DIMENSION,
        'values': table_values
    }

    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheet_id,
            range=TABLE_RANGE,
            valueInputOption=VALUE_INPUT_OPTION,
            json=update_body
        )
    )
