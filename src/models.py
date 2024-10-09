from pydantic import BaseModel
from typing import List

class Phrase(BaseModel):
    text: str
    pause: int  # milliseconds

class MeditationScript(BaseModel):
    duration: int  # milliseconds
    focus_area: str
    phrases: List[Phrase]