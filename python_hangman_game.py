import random
from hangman_game_word_list import python_terms

# Game Data
stats = {
    "games_played": 0,
    "correct": 0,
    "incorrect": 0,
    "total_score": 0,
    "current_score": 0,
    "current_streak": 0,
    "best_streak": 0
}

history = []

personal_best = 0

difficulty_points = {
    "Easy": 10,
    "Medium": 20,
    "Hard": 30
}

# Main Menu
def show_menu():
    print("\n" + "=" * 55)
    print("🐍 PYTHON DICTIONARY")
    print("=" * 55)

    print("1. 🎮 Play")
    print("2. 📚 Browse Python Terms")
    print("3. 📊 Statistics")
    print("4. 🏆 Personal Best")
    print("5. 📜 Game History")
    print("6. ❓ How to Play")
    print("7. 🚪 Exit")

    print("=" * 55)

# Choose Mode
def choose_mode():
    print("\n" + "=" * 40)
    print("🎮 CHOOSE GAME MODE")
    print("=" * 40)

    print("1. Definition -> Guess the Term")
    print("2. Term -> Guess the Definition")
    print("3. Multiple Choice")

    while True:
        choice = input("\nChoose a mode: ").strip()

        if choice == "1":
            return "definition"
        elif choice == "2":
            return "term"
        elif choice == "3":
            return "multiple"
        else:
            print("❌ Invalid choice. Please choose 1-3.")

# Choose Difficulty
def choose_difficulty():
    print("\n" + "=" * 40)
    print("🎚️ CHOOSE DIFFICULTY")
    print("=" * 40)

    print("1. 🟢 Easy    - 10 points")
    print("2. 🟡 Medium  - 20 points")
    print("3. 🔴 Hard    - 30 points")

    while True: 
        choice = input("\nChoose difficulty: ").strip()

        if choice == "1":
            return "Easy"
        elif choice == "2":
            return "Medium"
        elif choice == "3":
            return "Hard"
        else:
            print("❌ Invalid choice. Please choose 1-3.")

# Get Terms By Difficulty
def get_terms_by_difficulty(difficulty):

    available_terms = []

    for term, information in python_terms.items():

        if information["difficulty"] == difficulty:
            available_terms.append(term)

    return available_terms

# Choose Random Term
def choose_term(difficulty):
    available_terms = get_terms_by_difficulty(difficulty)

    if not available_terms:
        available_terms = list(python_terms.keys())

    return random.choice(available_terms)

# Create Hidden Word
def create_hidden_word(word, guessed_letters):

    hidden_word = []

    for character in word:

        # Keep spaces and special characters visible 
        if not character.isalpha():
            hidden_word.append(character)

        elif character.lower() in guessed_letters:
            hidden_word.append(character)

        else:
            hidden_word.append("_")

    return " ".join(hidden_word)

# Check If Word Is Completed
def is_word_complete(word, guessed_letters):

    for character in word: 
        if character.isalpha():
            if character.lower() not in guessed_letters:
                return False

    return True

# Definition -> Term Mode
def definition_mode(term):

    information = python_terms[term]

    definition = information["definition"]
    example = information["example"]
    category = information["category"]
    difficulty = information["difficulty"]

    guessed_letters = set()

    lives = 6

    print("\n" + "=" * 55)
    print("🐍 GUESS THE PYTHON TERM")
    print("=" * 55)

    print(f"\n📖 Definition: ")
    print(definition)

    print(f"\n🗂️ Category: {category}")
    print(f"🎚️ Difficulty: {difficulty}")

    print("\n💡 Example: ")
    print(example)

    print("\n" + "-" * 55)

    while lives > 0:
        hidden_word = create_hidden_word(term, guessed_letters)

        print(f"\nWord: {hidden_word}")

        if guessed_letters:
            print(
                "🔤 Guessed letters: ",
                ",".join(sorted(guessed_letters))
            )
        else:
            print("🔤 Guessed letters: -")

        print(f"♥️ Lives: {lives}")

        # Check if the word has already been completed
        if is_word_complete(term, guessed_letters):
            print("\n🎉 AMAZING! You guessed the term!")
            print(f"🐍 Term: {term}")

            return True

        letter = input("\nEnter a letter: ").strip().lower()

        # Input validation
        if len(letter) != 1 or not letter.isalpha():

            print("❌ Please enter ONE letter.") 

            continue

        guessed_letters.add(letter)

        # Correct letter
        if letter in term.lower():
            print("✅ Correct!")

        # Wroong letter
        else:
            lives -= 1
            print("❌ Wrong letter!")

    # Player lost
    print("\n💀 Out of lives!")

    print(f"🐍 The correct term was: {term}")

    return False

# Term -> Definition Mode
def term_mode(term):

    information = python_terms[term]

    definition = information["definition"]
    example = information["example"]
    category = information["category"]
    difficulty = information["difficulty"]

    print("\n" + "=" * 55)
    print("📖 EXPLAIN THE PYTHON TERM")
    print("=" * 55)

    print(f"\n🐍 Term: {term}")
    print(f"🗂️ Category: {category}")
    print(f"🎚️ Difficulty: {difficulty}")

    print("\n💡 Example: ")
    print(example)

    print("\nTry to explain what this term means.")

    answer = input("\nYour answer: ").strip().lower()

    # Get important words from definition
    definition_words = definition.lower().split()
    
    meaningful_words = []

    for word in definition_words:
        clean_word = word.strip(".,!?()'\"")

        if len(clean_word) >= 4:
            meaningful_words.append(clean_word)

    matches = 0

    for word in meaningful_words:

        if word in answer:
            matches += 1

    # If enough important words appear
    if matches >= 2:
        print("\n✅ Good explanation!")
        return True

    else:
        print("\n❌ Not quite.")
        print(f"📖 Definition: {definition}")
        return False


# Multiple Choice Mode
def multiple_choice_mode(term):
    correct_definition = python_terms[term]["definition"]
    all_terms = list(python_terms.keys())

    wrong_terms = []
    for other_term in all_terms:
        if other_term != term:
            wrong_terms.append(other_term)

    selected_wrong_terms = random.sample(
        wrong_terms,
        min(3, len(wrong_terms))
    )

    options = [correct_definition]
    for wrong_term in selected_wrong_terms:
        options.append(
            python_terms[wrong_term]["definition"]
        )

    random.shuffle(options)

    print("\n" + "=" * 55)
    print("🧠 MULTIPLE CHOICE")
    print("=" * 55)

    print(f"\n🐍 Term: {term}")

    print(f"\n🗂️ Category: {python_terms[term]['category']}")
    print(f"🎚️ Difficulty: {python_terms[term]['difficulty']}")

    print("\nWhat is the correct definition?\n")

    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")

    while True:
        answer = input("\nChoose 1-4: ").strip()

        if answer in ["1", "2", "3", "4"]:
            selected_option = options[int(answer) - 1]

            if selected_option == correct_definition:
                print("\n✅ Correct!")

                return True

            else: 
                print("\n❌ Incorrect!")
                print(f"📖 Correct definition: {correct_definition}")
                return False

        else: 
            print("❌ Please choose a number from 1 to 4.")
# Calculate Score
def calculate_score(difficulty):
    base_score = difficulty_points[difficulty]
    streak_bonus = stats["current_streak"] * 2
    total_score = base_score + streak_bonus
    return total_score

# Update Correct Answer
def update_correct(score):
    global personal_best
    stats["correct"] += 1
    stats["current_streak"] += 1
    stats["total_score"] += score

    # Update best streak
    if stats["current_streak"] > stats["best_streak"]:
        stats["best_streak"] = stats["current_streak"]

    # Update personal best
    if score > personal_best:
        personal_best = score

# Update Incorrect Answer
def update_incorrect():
    stats["incorrect"] += 1
    stats["current_streak"] = 0

# Play Game
def play_game():
    stats["games_played"] += 1

    print("\n" + "=" * 55)
    print("🎮 NEW GAME")
    print("=" * 55)

    difficulty = choose_difficulty()

    mode = choose_mode()

    term = choose_term(difficulty)

    # Play selected mode
    if mode == "definition":
        correct = definition_mode(term)
    elif mode == "term":
        correct = term_mode(term)
    else:
        correct = multiple_choice_mode(term)

    # Correct answer
    if correct:
        score = calculate_score(difficulty)
        update_correct(score)

        print("\n" + "=" * 55)
        print("🎉 CORRECT!")
        print(f"⭐️ Score: +{score}")
        print(f"🔥 Current streak: {stats['current_streak']}")
        print(f"🏆 Best streak: {stats['best_streak']}")
        print(f"💰 Total score: {stats['total_score']}")

        result = "Correct"

    # Incorrect answer
    else:
        update_incorrect()

        print("\n" + "=" * 55)
        print("❌ INCORRECT")
        print(f"🔥 Current streak: {stats['current_streak']}")
        print(f"💰 Total score: {stats['total_score']}")
        print("=" * 55)

        result = "Incorrect"

    # Save game history
    history.append({
        "term": term,
        "difficulty": difficulty,
        "result": result,
        "score": score if correct else 0
    })

    # Replay
    while True:
        replay = input("\n🔁 Play another round? (y/n): ").strip().lower()
        if replay == "y":
            play_game()
            break
        elif replay == "n":
            break
        else: 
            print("❌ Please enter y or n.")

# Browse Python Terms
def browse_terms():
    print("\n" + "=" * 55)
    print("📚 BROWSE PYTHON TERMS")
    print("=" * 55)

    categories = []
    for information in python_terms.values():
        category = information["category"]
        if category not in categories:
            categories.append(category)

    print("\n0. 🌐 All Categoies")
    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")

    while True:
        choice = input("\nChoose a category: ").strip()
        if choice.isdigit():
            choice_number = int(choice)
            if choice_number == 0:
                selected_category = None
                break
            elif 1 <= choice_number <= len(categories):
                selected_category = categories[choice_number - 1]
                break

            print("❌ Invalid choice.")

        print("\n" + "=" * 55)
    for term, information in python_terms.items():
        if ( 
            selected_category is None
            or information["category"] == selected_category
        ):
            print(f"\n🐍 {term}")
            print(f"📖 {information['definition']}")
            print(f"💡 Example: {information['example']}")
            print(f"🎚️ Difficulty: {information['difficulty']}")
            print("-" * 55)



# Statistics
def show_statistics():
    print("\n" + "=" * 55)
    print("📊 STATISTICS")
    print("=" * 55)

    games = stats["games_played"]
    correct = stats["correct"]
    incorrect = stats["incorrect"]

    total_answers = correct + incorrect

    if total_answers > 0:
        accuracy = (correct / total_answers) * 100
    else: 
        accuracy = 0

    print(f"\n🎮 Games played: {games}")
    print(f"✅ Correct answers: {correct}")
    print(f"❌ Incorrect answers: {incorrect}")
    print(f"🎯 Accuracy: {accuracy:.1f}%")
    print(f"💰 Total score: {stats['total_score']}")
    print(f"🔥 Currect streak: {stats['current_streak']}")
    print(f"🏆 Best streak: {stats['best_streak']}")

# Personal Best
def show_personal_best():
    print("\n" + "=" * 55)
    print("🏆 PERSONAL BEST")
    print("=" * 55)

    if personal_best > 0:
        print(f"\n🥇 Highest single-round score: {personal_best}")
    else:
        print("\n📭 No personal best yet.")
        print("Play a game to set your record.")

# Game History
def show_history():
    print("\n" + "=" * 55)
    print("📜 GAME HISTORY")
    print("=" * 55)

    if not history:
        print("\n📭 No games played yet.")
        return
    for index, game in enumerate(history, start=1):
        print(f"\nGame #{index}")

        print(f"🐍 Term: {game['term']}")
        print(f"🎚️ Difficulty: {game['difficulty']}")
        print(f"📌 Result: {game['result']}")
        print(f"⭐️ Score: {game['score']}")

        print("-" * 55)

# How To Play
def show_how_to_play():
    print("\n" + "=" * 55)
    print("❓ HOW TO PLAY")
    print("=" * 55)

    print("""
🐍 Python Dictionary is a Python terminology learning game.

🎮 GAME MODES

1. Definition -> Guess the Term
   Read the definition and guess the term
   one letter at a time.
2. Term → Guess the Definition
   See the Python term and explain what it means.

3. Multiple Choice
   Choose the correct definition from four options.


🎚️ DIFFICULTY

🟢 Easy   → 10 points
🟡 Medium → 20 points
🔴 Hard   → 30 points

🔥 STREAK BONUS

Every correct answer increases your streak.

Your streak gives you bonus points.

❌ An incorrect answer resets your streak.


❤️ LETTER GUESSING

In Definition → Term mode:

• You have 6 lives.
• Guess one letter at a time.
• Correct letters appear in the word.
• Wrong letters remove one life.
• Repeated letters are not counted.
• Spaces and special characters are automatically revealed.


📊 STATISTICS

The game tracks:

• Games played
• Correct answers
• Incorrect answers
• Accuracy
• Total score
• Current streak
• Best streak


🏆 PERSONAL BEST

Your highest single-round score is saved
during the current program session.


📜 GAME HISTORY

Every round records:

• Python term
• Difficulty
• Result
• Score




""")

# Main Program
while True:
    show_menu()

    choice = input("Choose an option: ").strip()

    if choice == "1":
        play_game()
    elif choice == "2":
        browse_terms()
    elif choice == "3":
        show_statistics()
    elif choice == "4":
        show_personal_best()
    elif choice == "5":
        show_history()
    elif choice == "6":
        show_how_to_play()
    elif choice == "7":
        print("\n" + "=" * 55)
        print("🐍 Thanks for playing Python Dictionary!")
        print("Keep coding and keep learning! 💻🔥")
        print("=" * 55)

        break
    else:
        print("\n❌ Invalid choice. Please choose 1-7.")
