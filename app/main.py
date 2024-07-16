from fastapi import FastAPI
from routers import user
from db.database import Base, engine
import uvicorn

app = FastAPI()
app.include_router(user.router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)