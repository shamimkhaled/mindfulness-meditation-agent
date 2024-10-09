import streamlit as st
from src.meditation_agent import generate_meditation_script

# Streamlit App Interface
def main():
    st.title("Mindfulness Meditation Agent")
    
    st.write("""
    Welcome to the Mindfulness Meditation Generator. Enter a prompt, and this app will generate a structured mindfulness meditation script based on your input.
    """)

    # Input from the user
    prompt = st.text_area("Enter your meditation request", "Create a 60-second mindfulness meditation focused on relaxation.")

    # Button to generate the script
    if st.button("Generate Meditation Script"):
        with st.spinner('Generating meditation script...'):
            meditation_script = generate_meditation_script(prompt)
        
        if meditation_script:
            st.success("Meditation script generated successfully!")
            st.write("### Meditation Script:")
            st.json(meditation_script.model_dump_json(indent=2))

if __name__ == "__main__":
    main()