from fastapi import FastAPI
from src.routers import emp_gen_info
import uvicorn

app = FastAPI()


app.include_router(
    emp_gen_info.router,
    tags=['store general info']
)


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=2939)