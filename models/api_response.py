from pydantic import BaseModel
from typing import List

from models.cost_calculation import CostCalculation


class APIResponse(BaseModel):
    costCalculation: CostCalculation
    summaryPoints: List[str]
