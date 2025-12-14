from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from piccolo.engine import engine_finder
from piccolo.engine.base import Engine

# from academy.api.courses import router as course_router
from academy.api.courses import router as course_router

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    engine: Engine = engine_finder()
    if engine is None:
        raise RuntimeError("Piccolo engine not found")

    await engine.start_connection_pool()
    yield
    await engine.close_connection_pool()


app = FastAPI(
    title="Flyger Academy",
    lifespan=lifespan,
)

app.include_router(course_router)
