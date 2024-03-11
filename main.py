# from transformers.pipelines.conversational import Conversation
# from transformers import pipeline
# from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# chatbot = pipeline("conversational")

@app.get("/hi")
def read_root():
    return {"Hello": "World"}

# class Message(BaseModel):
#     message: str

# @app.post("/chat")
# def post_chat(body: Message):
#     conversation = Conversation(body.message)
#     response = chatbot(conversation).generated_responses
#     print(response)
#     print(conversation)
#     return {"data": response[0]}