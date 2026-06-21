from fastapi import FastAPI

from app.api.routes import router
from app.storage.database import init_db

app = FastAPI(
    title="SOC Threat Engine",
    version="0.1.0"
)

app.include_router(router)


@app.on_event("startup")
def on_startup():
    # Ensures the SQLite schema exists before the app starts serving requests.
    init_db()


@app.get("/")
def root():
    return {
        "application": "SOC Threat Engine",
        "status": "running"
    }
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
