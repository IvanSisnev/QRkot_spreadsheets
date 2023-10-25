"""
Утилиты проекта.
"""
from datetime import timedelta

from app.core.constants import COMPLETION_RATE_FORMAT


async def timedelta_to_str(time_obj: timedelta) -> str:
    """
    Принять объект timedelta, преобразовать его в строку заданного формата.
    """
    time_obj: str = COMPLETION_RATE_FORMAT.format(
        days=time_obj.days,
        hours=time_obj.seconds // 3600,
        minutes=(time_obj.seconds // 60) % 60
    )
    return time_obj
