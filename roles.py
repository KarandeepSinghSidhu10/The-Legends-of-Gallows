ROLES = {
    1: {"name": "Warrior", "lives": 7, "hint_triggers": [3, 5], 
        "desc": "Extra Life & Adept Striker: Starts with 7 lives. If your next guess is correct after a miss, the miss is negated.", 
        "adept_striker": True, "reveal_letter": False, "forgiving": False, "bard": False, "druid": False},
    
    2: {"name": "Mage", "lives": 6, "hint_triggers": [2, 4], 
        "desc": "Extra Hints & Arcane Insight: Hints at 2 and 4 misses. Can use a hint to ask if a letter is a vowel or consonant (once).", 
        "arcane_insight": True, "reveal_letter": False, "forgiving": False, "bard": False, "druid": False},
    
    3: {"name": "Rogue", "lives": 6, "hint_triggers": [3, 5], 
        "desc": "Reveal a Letter & Swift Escape: One random letter is shown at start. Can skip one wrong guess penalty per game.", 
        "swift_escape": True, "reveal_letter": True, "forgiving": False, "bard": False, "druid": False},
    
    4: {"name": "Paladin", "lives": 6, "hint_triggers": [3, 5], 
        "desc": "Forgiving Mistakes & Divine Smite: Incorrect guesses only count after 3 in a row. Reveal 5th unique letter for a free guess.", 
        "divine_smite": True, "reveal_letter": False, "forgiving": True, "bard": False, "druid": False},
    
    5: {"name": "Bard", "lives": 6, "hint_triggers": [3, 5], 
        "desc": "Encouraging Messages & Inspiring Performance: Motivational boosts. 3 consecutive correct guesses grants a one-time wrong guess shield.", 
        "inspiring_performance": True, "reveal_letter": False, "forgiving": False, "bard": True, "druid": False},
    
    6: {"name": "Druid", "lives": 6, "hint_triggers": [3, 5], 
        "desc": "Nature's Aid & Fungal Growth: Correct vowel guesses restore a life. Guesses containing 'g', 'r', or 'o' reveal extra letters.", 
        "fungal_growth": True, "reveal_letter": False, "forgiving": False, "bard": False, "druid": False},
    
    7: {"name": "Astronaut", "lives": 6, "hint_triggers": [2, 4], 
        "desc": "Scanner Sweep: Can use a hint to reveal the two most common remaining consonants (once).", 
        "scanner_sweep": True, "reveal_letter": False, "forgiving": False, "bard": False, "druid": False},
    
    8: {"name": "Pirate", "lives": 6, "hint_triggers": [3, 5], 
        "desc": "Treasure Sense: Starts with +1 Life if the word contains 'e', 's', or 'a'.", 
        "treasure_sense": True, "reveal_letter": False, "forgiving": False, "bard": False, "druid": False},
    
    9: {"name": "Wizard", "lives": 6, "hint_triggers": [2, 4], 
        "desc": "Elemental Affinity: The first guessed vowel is fully revealed in all instances.", 
        "elemental_affinity": True, "reveal_letter": False, "forgiving": False, "bard": False, "druid": False},
    
    10: {"name": "Detective", "lives": 6, "hint_triggers": [3, 5], 
        "desc": "Forgiving Mistakes & Motive Analysis: Incorrect guesses only count after 3 in a row. A correct guess after 2 misses reveals an extra correct letter.", 
        "motive_analysis": True, "reveal_letter": False, "forgiving": True, "bard": False, "druid": False},
    
    11: {"name": "Ninja", "lives": 6, "hint_triggers": [3, 5], 
        "desc": "Reveal a Letter & Shadow Step: One random letter shown at start. Can swap the word once per game.", 
        "shadow_step": True, "reveal_letter": True, "forgiving": False, "bard": False, "druid": False},
    
    12: {"name": "Explorer", "lives": 6, "hint_triggers": [3, 5], 
        "desc": "Ancient Map: Receives a bonus hint use if the secret word is 7 or more letters long.", 
        "ancient_map": True, "reveal_letter": False, "forgiving": False, "bard": False, "druid": False}
}