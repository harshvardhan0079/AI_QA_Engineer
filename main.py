from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.quality import router as quality_router
from routers.review import router as review_router
from routers.fix import router as fix_router
from routers.explain import router as explain_router
from routers.tests import router as tests_router
from routers.history import router as history_router
from routers.bugs import router as bugs_router
app = FastAPI(
    title="AI QA Engineer",
    description="Production Grade AI QA Platform",
    version="2.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(quality_router)
app.include_router(review_router)
app.include_router(fix_router)
app.include_router(explain_router)
app.include_router(tests_router)
app.include_router(history_router)
app.include_router(bugs_router)

@app.get("/")
def home():
    return {
        "message": "🚀 AI QA Engineer Backend Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }