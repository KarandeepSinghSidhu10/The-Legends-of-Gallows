import time
import sys
from colorama import Fore, Style
from ascii_art import HANGMAN_STAGES

def scene_loader(text="Preparing the scene...", steps=6, delay=0.12):
    """Simple loading animation"""
    for i in range(steps):
        dots = "." * (i % 4)
        sys.stdout.write(Fore.MAGENTA + Style.BRIGHT + f"\r{text}{dots}" + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def animate_hangman(stage, delay=0.02):
    """Prints the hangman stage by stage"""
    lines = HANGMAN_STAGES[stage].strip().split('\n')
    for line in lines:
        print(line)
        time.sleep(delay)

def display_game(secret_word, display_word, guessed_letters, lives, incorrect_guesses, role_name):
    """Displays the game state"""
    animate_hangman(min(incorrect_guesses, len(HANGMAN_STAGES)-1))
    print(Fore.YELLOW + "Mystical Runes: " + " ".join(display_word) + Style.RESET_ALL)
    print(Fore.YELLOW + "Spells Cast: " + (", ".join(sorted(guessed_letters)) if guessed_letters else "none") + Style.RESET_ALL)
    print(Fore.CYAN + f"{role_name}'s Lives: {lives}" + Style.RESET_ALL)