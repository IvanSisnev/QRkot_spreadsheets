"""
CRUD операции модели CharityProject.
"""
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import BaseCRUD
from app.models.charity_project import CharityProject


class CharityProjectCRUD(BaseCRUD):
    """
    CRUD операции модели CharityProject.
    """
    async def get_id_by_name(self, charity_project_name: str, # noqa
                             session: AsyncSession) -> Optional[int]:
        """
        Найти в БД проекты с таким же названием.
        """
        charity_project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == charity_project_name
            )
        )
        return charity_project_id.scalars().first()

    async def get_projects_by_completion_rate( # noqa
            self, session: AsyncSession) -> list[CharityProject]:
        """
        Получить из базы список благотворительных проектов, отсортированный
        по убыванию скорости их закрытия (возрастанию разницы между датами
        открытия и закрытия проекта).
        """
        closed_projects = await session.execute(
            select(CharityProject).where(
                CharityProject.fully_invested
            ).order_by(
                (CharityProject.close_date - CharityProject.create_date)
            )
        )
        return closed_projects.scalars().all()


charity_project_crud = CharityProjectCRUD(CharityProject)
