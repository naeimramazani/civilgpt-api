from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# اجازه اتصال از رابط کاربری‌ات
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class Prompt(BaseModel):
    prompt: str
    lang: str = "fa"

@app.post("/infer")
def infer_text(prompt: Prompt):
    return {
        "answer": f"🤖 پاسخ CivilGPT ({prompt.lang}): شما پرسیدید → {prompt.prompt}"
    }
