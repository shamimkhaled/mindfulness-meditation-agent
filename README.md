# Mindfulness Meditation Agent

## Project Overview

The **Mindfulness Meditation Agent** is a Python-based tool that generates structured mindfulness meditation scripts using OpenAI's GPT-4. The meditation scripts are tailored based on user input and are validated using Pydantic models to ensure a consistent structure.


- **Structured Outputs**: Generates meditation scripts with a JSON structure, including session duration, focus area, and a list of phrases with pauses.
- **Pydantic Validation**: Ensures that the generated scripts adhere to a strict schema for easy integration into other applications.
- **Dynamic Script Generation**: Customizes each meditation session based on the user's input, such as the desired duration and focus area.
- **Unit Testing**: Includes tests to verify the functionality and robustness of the meditation script generation.

## Features

- Generates meditation scripts in a structured format.
- Adjusts durations and pauses from seconds to milliseconds.
- Validates the structure using Pydantic models.
- Unit tests to ensure script generation accuracy and reliability.

## Example Output

Here's an example of a structured meditation script generated by the agent:

```json
{
  "duration": 60000,
  "focus_area": "breath awareness",
  "phrases": [
    {
      "text": "Begin by finding a comfortable position.",
      "pause": 5000
    },
    {
      "text": "Gently close your eyes and take a deep breath in.",
      "pause": 7000
    },
    {
      "text": "Feel the air filling your lungs.",
      "pause": 5000
    },
    {
      "text": "Now, slowly exhale, releasing any tension.",
      "pause": 5000
    },
    {
      "text": "Bring your attention to your natural breath rhythm.",
      "pause": 5000
    },
    {
      "text": "Notice how your chest rises and falls.",
      "pause": 5000
    },
    {
      "text": "With each breath, feel more relaxed.",
      "pause": 5000
    },
    {
      "text": "If your mind wanders, gently bring it back to your breath.",
      "pause": 5000
    },
    {
      "text": "Inhale deeply, feeling calm and centered.",
      "pause": 5000
    },
    {
      "text": "Exhale slowly, letting go of any stress.",
      "pause": 5000
    },
    {
      "text": "When you're ready, gently open your eyes.",
      "pause": 3000
    },
    {
      "text": "Return to the present moment.",
      "pause": 5000
    }
  ]
}
```

## Installation

### Prerequisites

- Python 3.8 or higher.
- An OpenAI account with access to the GPT-4 API.

### Setup Instructions

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/shamimkhaled/mindfulness-meditation-agent.git
    cd mindfulness-meditation-agent
    ```

2. **Create a Virtual Environment**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**:

    Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**:

    Create a `.env` file using the provided template:

    ```bash
    cp .env.example .env
    ```

    Edit the `.env` file to include your OpenAI API key:

    ```
    OPENAI_API_KEY=your-openai-api-key-here
    ```

## Usage

To generate a mindfulness meditation script, run the following code:

```python
from src.meditation_agent import generate_meditation_script

prompt = "Create a 60-second mindfulness meditation focused on relaxation."
meditation_script = generate_meditation_script(prompt)

if meditation_script:
    print(meditation_script.model_dump_json(indent=2))
else:
    print("Failed to generate meditation script.")
```
To run the streamlit app:
```
streamlit run app.py
```

## Running Tests
To run unit tests, use the following command:
```
python -m unittest discover tests 

```
## Repository Structure

```
mindfulness-meditation-agent/
│
├── README.md                      # Project documentation
├── app.py                         # Streamlit app
├── .gitignore                     # Files and directories to ignore in version control
├── .env.example                   # Example environment variables
├── requirements.txt               # Python dependencies
├── src/                           # Source code for the agent
│   ├── __init__.py                # Init file for the src module
|   ├── convert_to_milliseconds.py # Convert seconds to milliseconds
│   ├── meditation_agent.py        # Main code for generating meditation scripts
│   ├── models.py                  # Pydantic models for structured validation
├── tests/                         # Unit tests for the project
│   ├── __init__.py                # Init file for the tests module
│   ├── test_meditation_agent.py # Unit tests for meditation_agent.py

```
## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.


## Development Workflow

- Create a Branch: Create a new branch for your feature or bug fix:
```
git checkout -b feature-name
```
- Make Changes: Implement your changes in the src/ or tests/ directory.

- Run Tests: Ensure all tests pass:
```
python -m unittest discover tests
```
- Commit Changes:
```
git add .
```
```
git commit -m "Add feature or fix bug"
```

- Push Changes:
```
    git push origin feature-name
```

- Create a Pull Request: Open a pull request on GitHub to merge your changes into the main branch.

## Documentation Updates

    - Update the README.md file if you change the structure of the meditation script or add significant new functionality.
    - Make sure to include accurate example usage and outputs in the documentation.
    - Provide detailed descriptions in pull requests to explain what has been changed or improved.

## Acknowledgements

    - OpenAI for providing the GPT-4 model, which powers the meditation agent.
    - Pydantic for data validation, ensuring consistent output structures.
    - All contributors who have helped improve this project.