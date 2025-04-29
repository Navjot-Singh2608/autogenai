from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router



app = FastAPI(title="AutoGenAI - LLM Research Agent")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # your React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
print("Application started successfully hey where are you sir..............")