from pydantic import BaseModel

class ProjectInput(BaseModel):
    land_cost: float
    permit_cost: float
    construction_cost: float
    sale_price: float

class ProjectOutput(BaseModel):
    total_cost: float
    profit: float
    timeline_months: int