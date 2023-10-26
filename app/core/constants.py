"""
Константы приложения.
"""
from typing import Final

# количество проектов в отчете Google sheets
PROJECTS_NUM_LIMIT: Final[int] = 10

# формат даты в названии и заголовке отчета
DATE_FORMAT: Final[str] = '%Y/%m/%d %H:%M:%S'
# формат представление скорости закрытия проекта
COMPLETION_RATE_FORMAT: Final[str] = ('Дней: {days}, часов: {hours}, минут: '
                                      'minutes}')

# установки таблицы отчета
# тип листа
SHEET_TYPE: Final[str] = 'GRID'
# количество строк и столбцов
ROW_COUNT: Final[int] = 3 + PROJECTS_NUM_LIMIT
COLUMN_COUNT: Final[int] = 3
# диапазон ячеек
TABLE_RANGE: Final[str] = f'A1:{chr(64+COLUMN_COUNT)}{COLUMN_COUNT}'
# способ заполнения данными
MAJOR_DIMENSION: Final[str] = 'ROWS'
VALUE_INPUT_OPTION: Final[str] = 'USER_ENTERED'
# наименования ячеек и столбцов
REPORT_TITLE: Final[str] = 'Отчет от'
REPORT_DESCRIPTION: Final[str] = 'Топ проектов по скорости закрытия'
COLUMN1_HEADER: Final[str] = 'Название проекта'
COLUMN2_HEADER: Final[str] = 'Средства собраны за'
COLUMN3_HEADER: Final[str] = 'Описание проекта'

# локаль
LOCALE: Final[str] = 'ru_RU'

# версии Google Drive и Sheets
DRIVE_VERSION: Final[str] = 'v3'
SHEETS_VERSION: Final[str] = 'v4'
