from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from app.pipeline.write_a_book import generate_book
from app.models.user_input import UserInput
from dotenv import load_dotenv
import os
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    logger.info("Application is starting...")
    
    load_dotenv()
    openai_key = os.getenv('OPENAI_API_KEY')
    os.environ["OPENAI_API_KEY"] = openai_key
    
    logger.info("Startup tasks completed")

@app.post("/write_a_book")
async def write_a_book(input_data: UserInput):
    return StreamingResponse(generate_book(input_data.user_input), media_type="application/json")
