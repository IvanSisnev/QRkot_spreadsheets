"""
Эндпоинт Google API.
"""
from aiogoogle import Aiogoogle
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.google_client import get_service
from app.core.user import current_superuser
from app.crud.charity_project import charity_project_crud
from app.schemas.charity_project import CharityProjectRead
from app.services.google_api import (spreadsheets_create,
                                     set_user_permissions,
                                     spreadsheets_update_value)

router = APIRouter()


@router.post(
    '/',
    response_model=list[CharityProjectRead],
    dependencies=[Depends(current_superuser)],
    summary='Создать отчет о пожертвованиях'
)
async def get_report(
        session: AsyncSession = Depends(get_async_session),
        wrapper_services: Aiogoogle = Depends(get_service)
):
    """
    Создать отчёт в Google Sheets о скорости закрытия благотворительных
    проектов.
    """
    closed_projects = await (
        charity_project_crud.get_projects_by_completion_rate(session)
    )
    now_date_time, spreadsheet_id, = await spreadsheets_create(
        wrapper_services
    )
    await set_user_permissions(spreadsheet_id, wrapper_services)
    await spreadsheets_update_value(spreadsheet_id,
                                    now_date_time,
                                    closed_projects,
                                    wrapper_services)
    return closed_projects
