from fastapi import FastAPI
from pydantic import BaseModel
from llm import invoke_agent


app = FastAPI()


class LLMRequest(BaseModel):
    user_input: str


class LLMResponse(BaseModel):
    input: str
    output: str

@app.post("/llm", response_model=LLMResponse)
async def run_llm(req: LLMRequest):
    result = await invoke_agent(req.user_input)
    return LLMResponse(input=req.user_input, output=result)
