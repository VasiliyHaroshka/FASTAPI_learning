from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

engine = create_async_engine("sqlite+aiosqlite:///database.db")

new_session = async_sessionmaker(
    engine,
    expire_on_commit=False,
)


async def get_session():
    """Session generator"""
    async with new_session() as session:
        yield session
