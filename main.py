from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import (scrap, gen)
import uvicorn

app = FastAPI(title="JustLink", description="One Click Generator")
origins = [
    "http://localhost:4200"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
)
app.include_router(scrap.router)
app.include_router(gen.router)
uvicorn.run(app, port=2000)