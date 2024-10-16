from pydantic import BaseModel
from typing import List

class Phrase(BaseModel):
    text: str
    pause: int  # milliseconds
    tts_duration: int  # milliseconds

class MeditationScript(BaseModel):
    title: str
    duration: int  # milliseconds
    focus_area: str
    phrases: List[Phrase]
    interval: int  # Default interval between phrases in milliseconds
    engagement: int  # Engagement level(0-100)
