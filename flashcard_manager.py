import json
import os

FLASHCARD_DIR = "data/"  # Adjust this path if necessary

def load_flashcards(language, difficulty):
    file_path = os.path.join(FLASHCARD_DIR, f"{difficulty}_{language}.json")
    
    try:
        with open(file_path, 'r') as file:
            flashcards = json.load(file)
            return flashcards
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return []
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from {file_path}: {e}")
        return []
