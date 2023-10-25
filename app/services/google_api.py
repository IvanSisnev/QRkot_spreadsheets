"""
Создание и заполнение таблицы Google Sheets c отчетом.
"""
from datetime import datetime

from aiogoogle import Aiogoogle

from app.core.config import settings
from app.models.charity_project import CharityProject


# todo перенести в google_client?
async def set_user_permissions(spreadsheet_id: str,
                               wrapper_services: Aiogoogle) -> None:
    """
    Получить доступ к документу на Google Drive.
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



async def spreadsheets_create(wrapper_services: Aiogoogle):
    """
    Создать таблицу.
    """
    pass


async def spreadsheets_update_value(spreadsheet_id: str,
                                    closed_projects: list[CharityProject],
                                    wrapper_services: Aiogoogle) -> None:
    """
    Заполнить таблицу данными.
    """
    pass
