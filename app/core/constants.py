"""
Константы приложения.
"""
from typing import Final

# формат даты отчета в Google sheets
FORMAT: Final[str] = '%Y/%m/%d %H:%M:%S'

# наименования ячеек и столбцов в отчете Google sheets
A1_title: Final[str] = 'Отчет от'
A2_description: Final[str] = 'Топ проектов по скорости закрытия'
COLUMN1_header: Final[str] = 'Название проекта'
COLUMN2_header: Final[str] = 'Средства собраны за'
COLUMN3_header: Final[str] = 'Описание проекта'
