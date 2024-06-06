from sqlalchemy import insert, select
from app.bookings.models import Bookings
from app.database import async_session_maker

class BaseDAO:
    model = None

    @classmethod
    async def find_by_id(class_, model_id: int):
         async with async_session_maker() as session:
            query = select(class_.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.scalar_one_or_none() 


    @classmethod
    async def find_one_or_none(class_, **filter_by):
         async with async_session_maker() as session:
            query = select(class_.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none() 


    @classmethod
    async def find_all(class_, **filter_by):
       async with async_session_maker() as session:
            query = select(class_.model).filter_by(**filter_by) # SELECT * FROM
            result = await session.execute(query)
            # Result.total_cost
            return result.scalars().all() # одноразовая
       
    @classmethod
    async def add(class_, **data):
       async with async_session_maker() as session:
           query = insert(class_.model).values(**data)
           await session.execute(query)
           await session.commit()
