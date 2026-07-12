from pydantic import BaseModel


class Prompt(BaseModel):
    prompt: str


class ScoreRequest(BaseModel):
    code: str


class ReviewRequest(BaseModel):
    code: str


class FixRequest(BaseModel):
    code: str


class ExplainRequest(BaseModel):
    code: str


class TestRequest(BaseModel):
    code: str