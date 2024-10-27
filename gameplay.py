from profile_manager import load_profile, create_profile
from flashcard_manager import load_flashcards
import random

def play_game(profile, language, difficulty):
    flashcards = load_flashcards(language, difficulty)
    if not flashcards:
        print("No flashcards available.")
        return

    correct_count = 0
    for flashcard in random.sample(flashcards, min(len(flashcards), 10)):
        print("\nQuestion:")
        print(flashcard["question"])
        if flashcard["question_style"] == "multiple_choice":
            for idx, option in enumerate(flashcard["options"], 1):
                print(f"{idx}. {option}")
            answer = input("Choose the correct answer (1-4): ")
            if answer == str(flashcard["answer"]):
                correct_count += 1
                print("Correct!")
            else:
                print(f"Incorrect! The correct answer is: {flashcard['answer']}")
        else:
            # Extend for other question types
            user_answer = input("Your answer: ")
            if user_answer.strip().lower() == flashcard["answer"].strip().lower():
                correct_count += 1
                print("Correct!")
            else:
                print(f"Incorrect! The correct answer is: {flashcard['answer']}")

    print(f"\nYou got {correct_count}/{len(flashcards)} correct.")
