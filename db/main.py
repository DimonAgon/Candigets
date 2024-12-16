
import asyncio

from .models import Base
from .engine import engine


async def main() -> None:
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)