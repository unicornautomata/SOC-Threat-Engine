from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.routes import router
from app.storage.database import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: ensure SQLite schema exists before serving requests.
    init_db()
    yield
    # Shutdown: nothing to clean up yet.

app = FastAPI(
    title="SOC Threat Engine",
    version="0.1.0",
    lifespan=lifespan
)

app.include_router(router)

@app.get("/")
def root():
    return {
        "application": "SOC Threat Engine",
        "status": "running"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
