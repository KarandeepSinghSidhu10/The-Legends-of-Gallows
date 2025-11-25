import re
import sys
import time
from colorama import Fore, Style

# Regex used to detect leading ANSI sequences
_ansi_prefix_re = re.compile(r'^(?:\x1b\[[0-9;]*m)+')

def typewriter_raw(text, delay=0.05):
    """Print text in typewriter style while avoiding splitting ANSI sequences."""
    m = _ansi_prefix_re.match(text)
    prefix = m.group(0) if m else ''
    visible = text[len(prefix):] if prefix else text

    if prefix:
        sys.stdout.write(prefix)
        sys.stdout.flush()

    for char in visible:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(Style.RESET_ALL + "\n")
    sys.stdout.flush()

def typewriter(text, delay=0.05):
    """Simplified typewriter that prints fully if delay==0"""
    if delay == 0:
        print(text)
        return
    # We use typewriter_raw for color handling when delay > 0
    typewriter_raw(text, delay)

def reveal_letter_in_word(secret_word, display_word, letter_to_reveal):
    """Helper to reveal all instances of a letter."""
    newly_revealed = 0
    for i, letter in enumerate(secret_word):
        if letter == letter_to_reveal and display_word[i] == '_':
            display_word[i] = letter_to_reveal
            newly_revealed += 1
    return newly_revealed

def get_most_common_consonants(secret_word, guessed_letters):
    """Finds the two most common unrevealed consonants."""
    consonants = "bcdfghjklmnpqrstvwxyz"
    remaining_letters = [
        l for l in secret_word 
        if l not in guessed_letters and l in consonants
    ]
    
    if not remaining_letters:
        return []
    
    # Count frequencies
    from collections import Counter
    counts = Counter(remaining_letters)
    # Sort by frequency (desc) and then by alphabetical order (asc)
    sorted_counts = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    
    # Return the top 2 unique consonants
    return [c for c, count in sorted_counts[:2]]