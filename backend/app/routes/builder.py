from fastapi import APIRouter
from app.schemas import ProjectInput, ProjectOutput
from app.services.estimator import estimate_project

router = APIRouter()

@router.post("/estimate", response_model=ProjectOutput)
def estimate(input: ProjectInput):
    return estimate_project(input)