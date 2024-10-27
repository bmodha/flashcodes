from profile_manager import create_profile, load_profile
from gameplay import play_game

def main():
    print("Welcome to the Flashcard System!")
    username = input("Enter your username: ")
    profile = load_profile(username)
    if not profile:
        create_profile(username)
        profile = load_profile(username)

    while True:
        print("\nMain Menu:")
        print("1. Play")
        print("2. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            language = input("Choose a language (e.g., C): ")
            difficulty = input("Choose difficulty (easy, medium, hard): ")
            play_game(profile, language, difficulty)
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
