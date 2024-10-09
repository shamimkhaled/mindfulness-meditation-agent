
def convert_to_milliseconds(meditation_script: dict) -> dict:
    """
    Convert the duration and pause times in the meditation script from seconds to milliseconds.
    """
    # Convert duration from seconds to milliseconds
    meditation_script["duration"] = meditation_script["duration"] * 1000
    
    # Convert each phrase's pause time from seconds to milliseconds
    for phrase in meditation_script["phrases"]:
        phrase["pause"] = phrase["pause"] * 1000
    
    return meditation_script