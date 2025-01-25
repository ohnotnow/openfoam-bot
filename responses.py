from pydantic import BaseModel

class InvestigatorResponse(BaseModel):
    key_parameters: list[str]
    assumptions: list[str]
    questions: list[str]

class AdvisorResponse(BaseModel):
    solver: str
    boundary_conditions: str
    best_practice_tips: str
    summary: str

class WorkerResponse(BaseModel):
    body: str
