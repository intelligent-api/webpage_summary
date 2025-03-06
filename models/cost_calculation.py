from pydantic import BaseModel


class CostCalculation(BaseModel):
    operation: str
    charactersIn: int
    charactersOut: int
    totalCharacters: int
    charactersPerPage: int
    pages: int
    pageCost: int
    totalCost: int
