
import openai
from pydantic import ValidationError
from src.models import MeditationScript
from src.convert_to_milliseconds import convert_to_milliseconds
from dotenv import load_dotenv
import os
import json

# Load environment variables from .env
load_dotenv()

# Set your OpenAI API key from the .env file
openai.api_key = os.getenv('OPENAI_API_KEY')




def generate_meditation_script(prompt: str) -> MeditationScript:

    # Check if the prompt is empty or invalid (basic validation)
    if not prompt.strip():
        print("Invalid prompt: The prompt cannot be empty.")
        return None
    
    system_message = (
    "You are a mindfulness meditation assistant that provides structured outputs. "
    "Your role is to create meditation scripts based on the user's request, adapting the content to the duration, focus area, "
    "and type of meditation they specify. If the user asks for a specific duration or focus, adjust the meditation content accordingly. "
    "Please ensure the output follows the structure of duration, focus_area, and phrases with pauses."
    )

     # Define the schema for the structured output
    response_format = {
        "type": "json_schema",
        "json_schema": {
            "name": "meditation_response",
            "schema": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "duration": {"type": "integer"},  # Duration in milliseconds
                    "focus_area": {"type": "string"},
                    "phrases": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "text": {"type": "string"},
                                "pause": {"type": "integer"},  # Pause in milliseconds
                                "tts_duration": {"type": "integer"}  # Duration for TTS in milliseconds
                            },
                            "required": ["text", "pause", "tts_duration"],
                            "additionalProperties": False
                        }
                    },
                    "interval": {"type": "integer"},  # Default interval between phrases
                    "engagement": {"type": "integer"}  # Engagement level, 0-100
                },
                "required": ["title", "duration", "focus_area", "phrases", "interval", "engagement"],
                "additionalProperties": False
            },
            "strict": True
        }
    }

    try:
        # Call OpenAI API to generate a response based on the prompt
        response = openai.ChatCompletion.create(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt},
            ],
            response_format=response_format,
            max_tokens=500,
            temperature=0.7
        )
        
        # Extract the generated text
        generated_text = response.choices[0].message['content']

     

        # Attempt to parse the JSON-like response into a structured format
        structured_output = json.loads(generated_text)

        # Convert duration and pause times to milliseconds
        converted_output = convert_to_milliseconds(structured_output)

        # Validate the structured data with Pydantic
        meditation_script = MeditationScript(**converted_output)
        return meditation_script

    except (ValidationError, json.JSONDecodeError) as e:
        print(f"Validation or JSON parsing error: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    


# # Define your prompt for the meditation script
# prompt = "can you make a 60 second mindfulness meditation?"

# # Generate the meditation script
# meditation_script = generate_meditation_script(prompt)

# # Display the structured meditation script
# if meditation_script:
#     print(meditation_script.model_dump_json(indent=2))
# else:
#     print("Failed to generate meditation script.")



   # # Simulate structured data (you can dynamically parse it)
        # structured_outputs = {
        #     "duration": 45000,
        #     "focus_area": "relaxation",
        #     "phrases": [
        #         {"text": "Welcome to this meditation, take a deep breath in through your nose and out through your mouth.", "pause": 2000},
        #         {"text": "Feel the air fill your lungs, and then release any tension or stress as you exhale.", "pause": 2000},
        #         {"text": "Bring your attention to your body, starting from your toes and moving up to the top of your head.", "pause": 2000},
        #         {"text": "As you breathe in, imagine fresh, calming energy entering your body.", "pause": 2000},
        #         {"text": "As you breathe out, imagine any tension or stress leaving your body.", "pause": 2000},
        #         {"text": "Allow your muscles to relax, starting from your toes and moving up to the top of your head.", "pause": 4000},
        #         {"text": "Feel the weight of your body sinking into the ground, supported by the earth below.", "pause": 3000},
        #         {"text": "Imagine yourself in a peaceful, safe place, surrounded by calm and serenity.", "pause": 4000},
        #         {"text": "Stay here for a moment, breathing deeply and feeling the relaxation spread throughout your body.", "pause": 6000},
        #         {"text": "When you're ready, slowly open your eyes, and take a deep breath in, feeling refreshed and renewed.", "pause": 2000}
        #     ]
        # }