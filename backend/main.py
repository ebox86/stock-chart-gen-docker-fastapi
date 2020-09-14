import sys

from fastapi import FastAPI

openapi_params = {
    "title": "stock-chart-gen-docker-fastapi",
    "openapi": "3.0.0",
    "version": "1.0",
    "docs_route": "/docs",
}
# cors ,doc

version = f"{sys.version_info.major}.{sys.version_info.minor}"

app = FastAPI()


@app.get("/")
async def read_root():
    message = f"Hello world! From FastAPI running on Uvicorn with Gunicorn. Using Python {version}"
    return {"message": message}