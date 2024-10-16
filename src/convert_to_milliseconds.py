
def convert_to_milliseconds(meditation_script: dict) -> dict:
    
    meditation_script["duration"] = meditation_script["duration"] * 1000

    # Convert interval from seconds to milliseconds, if it exists
    if "interval" in meditation_script:
        meditation_script["interval"] = meditation_script["interval"] * 1000

    # Convert each phrase's pause time and tts_duration from seconds to milliseconds
    for phrase in meditation_script.get("phrases", []):
        if "pause" in phrase:
            phrase["pause"] = phrase["pause"] * 1000
        if "tts_duration" in phrase:
            phrase["tts_duration"] = phrase["tts_duration"] * 1000

    return meditation_script