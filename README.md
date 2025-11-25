## The-Legends-of-Gallows
## Core Features
This is not a standard Hangman game; it is built around unique mechanics derived from fantasy RPG classes:

*Role-Based Gameplay*: Choose from 12 distinct classes such as the Warrior, Mage, Rogue, Paladin, Bard, and Ninja, each offering a fundamentally different way to approach the guessing challenge.

*Special Abilities*: Each role grants unique, one-time or triggered abilities that bend the rules of the game:

*Conditional Lives*: The Warrior's "Adept Striker" can negate a previous miss if the next guess is correct.

*Forgiving Mistakes*: Roles like the Paladin and Detective only count an incorrect guess after three consecutive misses.

*Strategic Revelation*: The Ninja can use "Shadow Step" to entirely swap the secret word once per game, resetting progress and lives.

*Themed Word Pools*: Words are dynamically selected based on the player's chosen Role, Difficulty ("Easy," "Medium," or "Hard"), and one of five general Categories (e.g., "Animals," "Objects," "Places").

*Atmospheric UI/UX*: The game features colored text output and a narrative typewriter effect for immersive dialogue. The hangman stages are rendered using detailed ASCII art that tells a story as the player's lives decrease.


 ## Role Showcase (Abilities Summary)
 The following table highlights a few of the specialized roles available to the adventurer:
 **ROLE**    **Key Ability**        **Mechanic Summary**
 *Warrior*   *Adept Striker*        *If the next guess after a miss is correct, the previous life loss is restored.**
 *Rogue*     *Swift Escape*         *Can skip one wrong guess penalty per game, allowing for a strategic error recovery.*   
 *Paladin*   *Forgiving Mistakes*   *Incorrect guesses only count as a life loss after 3 in a row.*
 *Wizard*    *Elemental Affinity*   *The first guessed vowel is fully revealed in all instances, giving a large early advantage.*   
 *Druid*     *Nature's Aid*         *Correct vowel guesses restore a life, encouraging strategic vowel hunting.*  
 *Ninja*     *Shadow Step*          *Can swap the entire word once per game to avoid certain defeat.*


## Installation and Setup
# Prerequisites
Python 3.x

# Steps to Run
1. Clone the Repository

*Bash

git clone [your-repository-url]
cd The-Legends-of-Gallows

2. Install Dependencies The only external requirement is the colorama library for cross-platform terminal coloring.

*Bash

*pip install -r requirement.txt

3. Start the Quest

*Bash

python main.py


## Technical Structure
The project is structured into several modular Python files to manage game logic, UI, and data:

*main.py: The entry point for the application.

*game.py: Contains the primary game loop, role selection, difficulty setting, guess processing, and win/loss conditions.

*roles.py: A dictionary defining all 12 available roles, their starting lives, and special flags for unique abilities.

*words.py: Contains the nested dictionary structure of all secret words, categorized by Role, Category, and Difficulty.

*ui.py: Manages terminal output, color handling, the loading animation (scene_loader), and the game display (calls the hangman animation).

*helpers.py: Provides utility functions like the typewriter text effect and logic for revealing letters.

*ascii_art.py: Stores the seven unique stages of the Hangman Sorcerer ASCII art.


## Contribution
We welcome contributions! Please open an Issue to discuss bug fixes, new roles, or expanding the word dictionary.

1. Fork the Project.

2. Create your Feature Branch (git checkout -b feature/NewFeature).

3. Commit your Changes (git commit -m 'Feat: Added new feature X').

4. Push to the Branch (git push origin feature/NewFeature).

5. Open a Pull Request.


## License
Distributed under the MIT License.

Copyright (c) 2025 KarandeepSinghSidhu10

See the LICENSE file for more information.