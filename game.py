import random
import sys
from collections import Counter

from colorama import Fore, Style, init
from helpers import typewriter, reveal_letter_in_word, get_most_common_consonants
from ui import scene_loader, display_game
from roles import ROLES
from words import get_word_for, DIFFICULTY_LEVELS, SHARED_CATEGORIES, ROLE_WORDS

init(autoreset=False)

WIN_MESSAGES = [
    "You are the hero Eldoria deserved!",
    "Legends will sing of your triumph!",
    "The sorcerer trembles at your name!",
    "Victory tastes sweeter than dragon's gold!",
    "You've rewritten fate itself!"
]

LOSE_MESSAGES = [
    "The sorcerer laughs: 'Better luck next time, peasant!'",
    "Eldoria weeps – and so should you!",
    "Even a goblin could have guessed that!",
    "The word mocks you from the gallows!",
    "Try again? Or admit defeat like a true loser?"
]

def simple_hint(secret_word, hint_type='definition'):
    if hint_type == "length":
        return f"The oracle senses it's {len(secret_word)} letters long."
    if hint_type == "first":
        return f"The first rune is '{secret_word[0]}'."
    if hint_type == "last":
        return f"The final rune is '{secret_word[-1]}'."
    return f"Think of words that fit the theme."

def list_roles():
    typewriter("\nChoose your destiny (roles):", 0.02)
    for num, r in ROLES.items():
        typewriter(Fore.CYAN + f"{num}. {r['name']} - {r['desc']}", 0.005)

def select_role():
    list_roles()
    while True:
        try:
            choice = int(input(Fore.WHITE + "Enter the number of your chosen role: "))
            if choice in ROLES:
                selected = ROLES[choice]
                return selected
            else:
                typewriter(Fore.RED + "Invalid choice. Pick a valid role number.", 0.005)
        except ValueError:
            typewriter(Fore.RED + "Please enter a number.", 0.005)

def select_difficulty():
    typewriter(Fore.MAGENTA + Style.BRIGHT + "\nChoose your challenge level:", 0.02)
    for idx, level in enumerate(DIFFICULTY_LEVELS, start=1):
        typewriter(Fore.YELLOW + f"{idx}. {level}", 0.005)
    
    while True:
        try:
            c = int(input(Fore.WHITE + "Choose a difficulty number: "))
            if 1 <= c <= len(DIFFICULTY_LEVELS):
                return DIFFICULTY_LEVELS[c - 1]
            else:
                typewriter(Fore.RED + f"Choose between 1 and {len(DIFFICULTY_LEVELS)}.", 0.005)
        except ValueError:
            typewriter(Fore.RED + "Please enter a number.", 0.005)

def select_category_for_role(role_name):
    typewriter(Fore.MAGENTA + Style.BRIGHT + f"Categories for {role_name}:", 0.02)
    for idx, cat in enumerate(SHARED_CATEGORIES, start=1):
        typewriter(Fore.CYAN + f"{idx}. {cat}", 0.005)
    while True:
        try:
            c = int(input(Fore.WHITE + "Choose a category number: "))
            if 1 <= c <= len(SHARED_CATEGORIES):
                return SHARED_CATEGORIES[c - 1]
            else:
                typewriter(Fore.RED + f"Choose between 1 and {len(SHARED_CATEGORIES)}.", 0.005)
        except ValueError:
            typewriter(Fore.RED + "Please enter a number.", 0.005)

def play_game():
    scene_loader("Summoning the quest", steps=8, delay=0.09)
    
    role = select_role()
    role_name = role["name"]
    typewriter(Fore.MAGENTA + Style.BRIGHT + f"\n=== {role_name} ===", 0.02)
    typewriter(Fore.CYAN + role["desc"], 0.02)

    difficulty = select_difficulty()
    typewriter(Fore.GREEN + f"Challenge set to: {difficulty}", 0.02)

    category = select_category_for_role(role_name)
    
    secret_word = get_word_for(role_name, category, difficulty)
    
    lives = role["lives"]
    max_lives = lives
    
    if role.get("treasure_sense") and any(c in secret_word for c in 'esa'):
        lives += 1
        max_lives += 1
        typewriter(Fore.GREEN + "The Pirate's Treasure Sense grants +1 Life!", 0.02)

    if role.get("ancient_map") and len(secret_word) >= 7:
        hint_uses = 3
        typewriter(Fore.GREEN + "The Explorer's Ancient Map grants +1 Hint!", 0.02)
    else:
        hint_uses = 2
        
    display_word = ['_'] * len(secret_word)
    guessed_letters = set()
    incorrect_guesses = 0
    consecutive_incorrect = 0
    consecutive_correct = 0 
    last_guess_was_miss = False 
    detective_miss_count = 0 
    vowels = 'aeiou'
    first_vowel_guessed = False 
    bard_shield_active = False 
    
    if role.get("reveal_letter"):
        available_letters = [letter for letter in secret_word if letter not in display_word]
        if available_letters:
            reveal = random.choice(available_letters)
            reveal_letter_in_word(secret_word, display_word, reveal)
            guessed_letters.add(reveal)
            typewriter(Fore.GREEN + f"As a {role_name}, a secret rune '{reveal}' is revealed!", 0.02)

    typewriter(Fore.MAGENTA + Style.BRIGHT + f"\n🌟 The Quest Begins — {category} ({difficulty}) — {len(secret_word)} runes to uncover 🌟\n", 0.02)
    
    ninja_swap_available = role.get("shadow_step")

    rogue_escape_available = role.get("swift_escape")

    while lives > 0 and '_' in display_word:
        display_game(secret_word, display_word, guessed_letters, lives, incorrect_guesses, role_name)

        prompt = Fore.WHITE + "Cast your spell — enter a rune (letter), 'hint' for wisdom"
        if ninja_swap_available:
            prompt += ", or 'swap' for Shadow Step"
        if rogue_escape_available:
             prompt += ", or 'escape' for Swift Escape"
        if role.get("arcane_insight") and hint_uses > 0:
            prompt += ", or 'vowel' for Arcane Insight"
        
        prompt += ": "
        guess = input(prompt).lower().strip()

        if guess == 'swap' and ninja_swap_available:
            secret_word = get_word_for(role_name, category, difficulty)
            display_word = ['_'] * len(secret_word)
            guessed_letters.clear()
            incorrect_guesses = 0
            lives = max_lives
            consecutive_incorrect = 0
            consecutive_correct = 0
            last_guess_was_miss = False
            detective_miss_count = 0
            first_vowel_guessed = False
            bard_shield_active = False
            ninja_swap_available = False
            typewriter(Fore.YELLOW + Style.BRIGHT + "Shadow Step activated! The word has been swapped. The quest restarts!", 0.02)
            continue
        elif guess == 'swap' and role.get("shadow_step"):
            typewriter(Fore.RED + "Shadow Step already used!", 0.005)
            continue
            
        if guess == 'escape' and rogue_escape_available:
            typewriter(Fore.YELLOW + "Swift Escape requires a failed attempt to activate. Guess a letter!", 0.01)
            continue

        if guess == 'vowel' and role.get("arcane_insight") and hint_uses > 0:
            hint_uses -= 1
            typewriter(Fore.GREEN + "Arcane Insight activated.", 0.01)
            letter_type = input(Fore.WHITE + "Enter a letter to check (a-z): ").lower().strip()
            
            if len(letter_type) != 1 or not letter_type.isalpha():
                typewriter(Fore.RED + "Invalid rune. Insight wasted!", 0.005)
            elif letter_type in vowels:
                typewriter(Fore.CYAN + f"The rune '{letter_type}' is a VOWEL!", 0.01)
            else:
                typewriter(Fore.CYAN + f"The rune '{letter_type}' is a CONSONANT!", 0.01)
            continue
        elif guess == 'vowel' and role.get("arcane_insight"):
            typewriter(Fore.RED + "No hints left for Arcane Insight!", 0.005)
            continue


        if guess == 'hint':
            if hint_uses > 0:
                hint_type = random.choice(['first', 'last', 'length', 'theme'])
                if hint_type == 'theme':
                    sample = ROLE_WORDS.get(role_name, {}).get(category, {}).get(difficulty, [])
                    if sample:
                        hint_word = random.choice(sample)
                        hint = f"Think of words like '{hint_word[:3]}...' ({len(hint_word)} letters)."
                    else:
                        hint = simple_hint(secret_word, "length")
                else:
                    hint = simple_hint(secret_word, hint_type)
                typewriter(Fore.GREEN + f"Oracle's Wisdom: {hint}", 0.01)
                hint_uses -= 1
                continue
            else:
                typewriter(Fore.RED + "No hints left! Trust your instincts.", 0.005)
                continue
        
        if len(guess) != 1 or not guess.isalpha():
            typewriter(Fore.RED + "Invalid spell! You must utter a single rune!", 0.005)
            continue
        if guess in guessed_letters:
            typewriter(Fore.RED + "You've already cast that spell!", 0.005)
            continue

        guessed_letters.add(guess)

        
        is_correct = guess in secret_word

        if is_correct:
            typewriter(Fore.GREEN + f"Success! The rune '{guess}' glows brightly – a piece of the word is revealed!", 0.005)
            
            newly_revealed = reveal_letter_in_word(secret_word, display_word, guess)
            
            consecutive_correct += 1
            consecutive_incorrect = 0 
            
            if role.get("adept_striker") and last_guess_was_miss and lives < max_lives:
                lives += 1
                typewriter(Fore.GREEN + "Adept Striker: Your swift hit negated your last miss, restoring 1 life!", 0.005)
            last_guess_was_miss = False

            if role.get("druid") and guess in vowels and lives < max_lives:
                lives += 1
                typewriter(Fore.GREEN + "Nature heals you! A life is restored.", 0.005)
            
            if role.get("elemental_affinity") and guess in vowels and not first_vowel_guessed:
                reveal_letter_in_word(secret_word, display_word, guess)
                first_vowel_guessed = True
                typewriter(Fore.GREEN + "Elemental Affinity: The first vowel guess revealed all its runes!", 0.005)

            revealed_count: int = sum(1 for char in display_word if char != '_')
            unique_revealed_count = len(set(c for c in display_word if c != '_'))
            if role.get("divine_smite") and unique_revealed_count == 5 and newly_revealed > 0:
                typewriter(Fore.YELLOW + "Divine Smite: You revealed a core rune! Take a free bonus guess (no penalty for a miss)!", 0.01)
                pass

            if role.get("motive_analysis") and detective_miss_count >= 2:
                remaining_correct_letters = [l for l in secret_word if l not in guessed_letters]
                if remaining_correct_letters:
                    extra_reveal = random.choice(remaining_correct_letters)
                    reveal_letter_in_word(secret_word, display_word, extra_reveal)
                    guessed_letters.add(extra_reveal)
                    typewriter(Fore.CYAN + f"Motive Analysis: Clues connected! Rune '{extra_reveal}' is also revealed!", 0.01)
                detective_miss_count = 0 
            
            if role.get("fungal_growth") and guess in 'gro':
                remaining_correct_letters = [l for l in secret_word if l not in guessed_letters]
                if remaining_correct_letters:
                    extra_reveal = random.choice(remaining_correct_letters)
                    reveal_letter_in_word(secret_word, display_word, extra_reveal)
                    guessed_letters.add(extra_reveal)
                    typewriter(Fore.GREEN + f"Fungal Growth: Hidden life found! Rune '{extra_reveal}' is also revealed!", 0.01)
            
            if role.get("inspiring_performance") and consecutive_correct == 3 and not bard_shield_active:
                bard_shield_active = True
                typewriter(Fore.YELLOW + Style.BRIGHT + "Inspiring Performance! You have a temporary shield against the next miss!", 0.02)

        else: 
            
            if bard_shield_active:
                typewriter(Fore.YELLOW + "The Sorcerer's spell rebounds off your Inspiring Performance shield! No life lost!", 0.005)
                bard_shield_active = False
                consecutive_correct = 0 
                continue
            
            if guess != 'escape' and rogue_escape_available and input(Fore.MAGENTA + "Activate Swift Escape to negate this miss? (y/n): ").lower().strip() == 'y':
                typewriter(Fore.YELLOW + "Swift Escape! You vanish and avoid the penalty!", 0.01)
                rogue_escape_available = False
                continue

            consecutive_correct = 0 
            last_guess_was_miss = True

            if role.get("forgiving"):
                consecutive_incorrect += 1
                if role.get("motive_analysis"):
                    detective_miss_count += 1
                
                if consecutive_incorrect < 3:
                    typewriter(Fore.YELLOW + f"Misfire, but your divine shield holds! ({3 - consecutive_incorrect} more until it counts.)", 0.005)
                    continue
            
            typewriter(Fore.RED + f"Misfire! The rune '{guess}' fades – the sorcerer draws nearer!", 0.005)
            lives -= 1
            incorrect_guesses += 1
            consecutive_incorrect = 0 

        if role.get("bard"):
            encouragements = ["Keep the faith!", "You're a legend in the making!", "The runes bend to your will!"]
            typewriter(Fore.GREEN + random.choice(encouragements), 0.005)

    display_game(secret_word, display_word, guessed_letters, lives, incorrect_guesses, role_name)
    if '_' not in display_word:
        typewriter(Fore.GREEN + Style.BRIGHT + f"\n🎉 Victory! As the {role_name}, you have deciphered the word '{secret_word}' and banished the Hangman Sorcerer! {random.choice(WIN_MESSAGES)}", 0.01)
    else:
        typewriter(Fore.RED + Style.BRIGHT + f"\n💀 Defeat! The word was '{secret_word}'. {random.choice(LOSE_MESSAGES)}", 0.01)

def show_main_menu():
    typewriter(Fore.MAGENTA + Style.BRIGHT + "=== THE TAVERN OF CHOICES ===", 0.01)
    typewriter(Fore.CYAN + "What will you do, adventurer?", 0.01)
    print(Fore.CYAN + "1) Play Hangman")
    print(Fore.CYAN + "2) View Roles & Stories")
    print(Fore.CYAN + "3) Exit Game" + Style.RESET_ALL)

def show_roles_library():
    typewriter(Fore.MAGENTA + Style.BRIGHT + "\n=== ROLE LIBRARY ===\n", 0.01)
    for num, r in ROLES.items():
        typewriter(Fore.CYAN + f"{num}. {r['name']}: {r['desc']}", 0.01)
        sample_role_name = r['name']
        if sample_role_name in ROLE_WORDS:
            for cat in SHARED_CATEGORIES:
                category_data = ROLE_WORDS[sample_role_name].get(cat, {})
                
                if not any(words for words in category_data.values()):
                    continue
                
                typewriter(Fore.YELLOW + f"  {cat} Runes:", 0.005)
                
                for difficulty in DIFFICULTY_LEVELS:
                    words = category_data.get(difficulty, [])
                    if words:
                        word_list = ", ".join(words)
                        
                        if difficulty == "Easy":
                            color = Fore.GREEN 
                        elif difficulty == "Medium":
                            color = Fore.BLUE
                        elif difficulty == "Hard":
                            color = Fore.RED
                        else:
                            color = Fore.WHITE
                        
                        typewriter(color + f"    - {difficulty}: {word_list}", 0.005)

    input(Fore.WHITE + "\nPress Enter to return to the tavern...")

def main():
    while True:
        show_main_menu()
        choice = input(Fore.WHITE + "Enter choice number: ").strip()
        if choice == '1':
            play_game()
            again = input(Fore.WHITE + "Return to tavern? (y/n): ").lower().strip()
            if again != 'y':
                typewriter(Fore.CYAN + "Farewell, adventurer! May your tales inspire bards.", 0.01)
                sys.exit()
        elif choice == '2':
            show_roles_library()
        elif choice == '3':
            typewriter(Fore.CYAN + "Farewell, adventurer! Return when the stars call you.", 0.01)
            sys.exit()
        else:
            typewriter(Fore.RED + "Choose a valid option (1-3).", 0.005)
