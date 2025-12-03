import random

DIFFICULTY_LEVELS = ["Easy", "Medium", "Hard"]

SHARED_CATEGORIES = [
    "Animals",
    "Objects",
    "Places",
    "Characters",
    "Special Items"
]

ROLE_WORDS = {
    "Warrior": {
        "Animals": {
            "Easy": ["boar", "wolf", "bear", "dog", "ram"],
            "Medium": ["stag", "hound", "steed", "panther", "falcon"],
            "Hard": ["mastiff", "griffon", "wyvern", "chimera", "grizzly"]
        },
        "Objects": {
            "Easy": ["sword", "shield", "axe", "bow", "mail"],
            "Medium": ["armor", "helmet", "banner", "spear", "dagger"],
            "Hard": ["battle-axe", "longspear", "sigil", "cuirass", "greatsword"]
        },
        "Places": {
            "Easy": ["fort", "keep", "camp", "gate", "wall"],
            "Medium": ["barracks", "arena", "outpost", "ruins", "tower"],
            "Hard": ["citadel", "battlefield", "wasteland", "stronghold", "rampart"]
        },
        "Characters": {
            "Easy": ["guard", "chief", "hero", "knight", "squire"],
            "Medium": ["soldier", "captain", "champion", "lieutenant", "general"],
            "Hard": ["commander", "mercenary", "legionary", "gladiator", "warlord"]
        },
        "Special Items": {
            "Easy": ["war-cry", "rune", "pact", "badge", "sash"],
            "Medium": ["battlehelm", "gauntlet", "vambrace", "scabbard", "talisman"],
            "Hard": ["battle-axe", "longspear", "war-banner", "bravery", "loyalty"]
        }
    },
    "Mage": {
        "Animals": {
            "Easy": ["owl", "toad", "imp", "bat", "crow"],
            "Medium": ["raven", "familiar", "bat", "serpent", "cat"],
            "Hard": ["phoenix", "chimera", "golem", "wyrm", "minotaur"]
        },
        "Objects": {
            "Easy": ["staff", "tome", "orb", "scroll", "ring"],
            "Medium": ["crystal", "cauldron", "vial", "amulet", "wand"],
            "Hard": ["spellbook", "mana-vial", "starshard", "phylactery", "scepter"]
        },
        "Places": {
            "Easy": ["tower", "vault", "room", "cellar", "study"],
            "Medium": ["sanctum", "library", "hall", "crypt", "archive"],
            "Hard": ["laboratory", "etherhall", "astralplane", "academy", "observatory"]
        },
        "Characters": {
            "Easy": ["mage", "apprentice", "seer", "scholar", "wizard"],
            "Medium": ["enchanter", "sorcerer", "oracle", "alchemist", "diviner"],
            "Hard": ["archmage", "illusionist", "necromancer", "conjurer", "warlock"]
        },
        "Special Items": {
            "Easy": ["elixir", "rune", "charm", "spell", "potion"],
            "Medium": ["spellscroll", "amulet", "scroll", "incense", "reagent"],
            "Hard": ["aether-stone", "starshard", "phylactery", "grimoire", "elements"]
        }
    },
    "Rogue": {
        "Animals": {
            "Easy": ["rat", "fox", "cat", "weasel", "mouse"],
            "Medium": ["ferret", "magpie", "weasel", "raven", "viper"],
            "Hard": ["shadowcat", "viper", "carrion-bird", "panther", "wolf"]
        },
        "Objects": {
            "Easy": ["dagger", "cloak", "hood", "mask", "boots"],
            "Medium": ["lockpick", "coinpouch", "mask", "gauntlet", "caltrops"],
            "Hard": ["shadowcloak", "silent-boot", "masterkey", "grappling-hook", "acid-vial"]
        },
        "Places": {
            "Easy": ["alley", "dock", "roof", "inn", "sewer"],
            "Medium": ["thievesden", "market", "sewer", "gallows", "warehouse"],
            "Hard": ["speakeasy", "backstreets", "rooftop", "underpass", "blackmarket"]
        },
        "Characters": {
            "Easy": ["thief", "spy", "fence", "scout", "beggar"],
            "Medium": ["pickpocket", "assassin", "informant", "smuggler", "burglar"],
            "Hard": ["shadowbroker", "cutthroat", "infiltrator", "saboteur", "mastermind"]
        },
        "Special Items": {
            "Easy": ["poisons", "talisman", "gem", "smoke", "wire"],
            "Medium": ["smokepellet", "cipher", "codex", "disguise", "lockbox"],
            "Hard": ["masterkey", "silent-talc", "acid-vial", "invisibility", "stealth"]
        }
    },
    "Paladin": {
        "Animals": { 
            "Easy": ["stag", "horse", "mutt", "dove", "lamb"], 
            "Medium": ["eagle", "mutt", "mastiff", "warhorse", "hound"], 
            "Hard": ["mastiff", "pegasus", "griffin", "unicorn", "charger"] 
        },
        "Objects": { 
            "Easy": ["mail", "relic", "shield", "robe", "sword"], 
            "Medium": ["tabard", "banner", "mace", "holy-book", "gauntlet"], 
            "Hard": ["holyshield", "oathstone", "blessed-mail", "crusader", "scepter"] 
        },
        "Places": { 
            "Easy": ["chapel", "shrine", "abbey", "crypt", "vault"], 
            "Medium": ["sanctuary", "citadel", "temple", "monastery", "altar"], 
            "Hard": ["cathedral", "pilgrimway", "holy-ground", "baptistery", "fortress"] 
        },
        "Characters": { 
            "Easy": ["cleric", "seer", "acolyte", "preacher", "bishop"], 
            "Medium": ["templar", "herald", "priest", "vicar", "righteous"], 
            "Hard": ["inquisitor", "crusader", "exorcist", "martyr", "prophet"] 
        },
        "Special Items": { 
            "Easy": ["blessing", "sigil", "faith", "prayer", "charm"], 
            "Medium": ["sacred-oil", "oathstone", "chalice", "scripture", "virtue"], 
            "Hard": ["relic-shard", "divine-fire", "righteousness", "sanctity", "redemption"] 
        }
    },
    "Bard": {
        "Animals": { 
            "Easy": ["lark", "cat", "finch", "dove", "sparrow"], 
            "Medium": ["fox", "magpie", "raven", "lizard", "parrot"], 
            "Hard": ["nightingale", "chameleon", "mockingbird", "siren", "griffin"] 
        },
        "Objects": { 
            "Easy": ["lute", "flute", "drum", "lyre", "quill"], 
            "Medium": ["scroll", "quill", "songbook", "mandolin", "harp"], 
            "Hard": ["tuning-fork", "chorus-scroll", "glamour", "ballad", "sonnet"] 
        },
        "Places": { 
            "Easy": ["tavern", "inn", "stage", "square", "road"], 
            "Medium": ["square", "theatre", "bar", "palace", "market"], 
            "Hard": ["gallery", "amphitheater", "coliseum", "conservatory", "festival"] 
        },
        "Characters": { 
            "Easy": ["poet", "bard", "singer", "dancer", "actor"], 
            "Medium": ["minstrel", "troubadour", "musician", "performer", "rhyme"], 
            "Hard": ["storyteller", "maestro", "composer", "impresario", "wordsmith"] 
        },
        "Special Items": { 
            "Easy": ["lyre", "chant", "song", "tune", "poem"], 
            "Medium": ["ballad", "sonnet", "ode", "satire", "melody"], 
            "Hard": ["chorus-scroll", "glamour", "charisma", "symphony", "harmony"] 
        }
    },
    "Druid": {
        "Animals": { 
            "Easy": ["stag", "owl", "badger", "fox", "toad"], 
            "Medium": ["wolf", "badger", "swan", "bear", "elk"], 
            "Hard": ["chimera", "behemoth", "treant", "golem", "satyr"] 
        },
        "Objects": { 
            "Easy": ["staff", "totem", "gourd", "herb", "seed"], 
            "Medium": ["gourd", "sickle", "stone", "talisman", "amulet"], 
            "Hard": ["herb-pouch", "moonstone", "root-bone", "sickle", "sap-essence"] 
        },
        "Places": { 
            "Easy": ["grove", "glade", "marsh", "lake", "tree"], 
            "Medium": ["marsh", "oakwood", "spring", "cave", "thicket"], 
            "Hard": ["sacred-pool", "treetop-home", "wilderness", "canopy", "caverns"] 
        },
        "Characters": { 
            "Easy": ["healer", "warden", "spirit", "ranger", "shrub"], 
            "Medium": ["shaman", "spirit", "beast", "warden", "faerie"], 
            "Hard": ["tree-keeper", "arch-druid", "elemental", "warden", "protector"] 
        },
        "Special Items": { 
            "Easy": ["seed", "amulet", "leaf", "moss", "bark"], 
            "Medium": ["moonstone", "root-bone", "pollen", "spore", "resin"], 
            "Hard": ["seed-of-life", "sap-essence", "transformation", "wildshape", "ecology"] 
        }
    },
    "Astronaut": {
        "Animals": { 
            "Easy": ["bat", "worm", "ant", "fly", "mite"], 
            "Medium": ["moonowl", "voidfish", "spacebat", "comet", "alien"], 
            "Hard": ["cometworm", "nebularabbit", "space-whale", "xenomorph", "crab"] 
        },
        "Objects": { 
            "Easy": ["rover", "thruster", "suit", "helmet", "pack"], 
            "Medium": ["oxygenpack", "antenna", "probe", "radio", "module"], 
            "Hard": ["spacesuit", "quantumcore", "warpdrive", "nanoprobe", "ionshield"] 
        },
        "Places": { 
            "Easy": ["orbit", "nebula", "moon", "mars", "void"], 
            "Medium": ["lunarbase", "marscolony", "station", "belt", "galaxy"], 
            "Hard": ["asteroidbelt", "deepspace", "spacewalk", "cryosleep", "terraforming"] 
        },
        "Characters": { 
            "Easy": ["pilot", "engineer", "crew", "medic", "robot"], 
            "Medium": ["commander", "navigator", "cosmonaut", "captain", "scientist"], 
            "Hard": ["cosmonaut", "exobiologist", "astrogator", "terraformer", "chief"] 
        },
        "Special Items": { 
            "Easy": ["stardust", "probe", "fuel", "laser", "data"], 
            "Medium": ["nanoprobe", "ionshield", "hologram", "beacon", "gravity"], 
            "Hard": ["warpdrive", "gravitywell", "blackhole", "teleport", "hyperspace"] 
        }
    },
    "Pirate": {
        "Animals": { 
            "Easy": ["shark", "parrot", "crab", "gull", "eel"], 
            "Medium": ["manta", "albatross", "squid", "dolphin", "whale"], 
            "Hard": ["reef-scorpion", "kraken", "sea-serpent", "mermaid", "octopus"] 
        },
        "Objects": { 
            "Easy": ["anchor", "cutlass", "flag", "coin", "hook"], 
            "Medium": ["compass", "spyglass", "pistol", "map", "rum"], 
            "Hard": ["treasuremap", "sextant", "doubloon", "blackspot", "sea-chart"] 
        },
        "Places": { 
            "Easy": ["island", "reef", "harbor", "ship", "port"], 
            "Medium": ["lagoon", "harbor", "cove", "shoals", "beach"], 
            "Hard": ["shipwreck", "tidetunnel", "dead-mans-bay", "tortuga", "deepsea"] 
        },
        "Characters": { 
            "Easy": ["captain", "matey", "sailor", "cook", "gunner"], 
            "Medium": ["buccaneer", "gunner", "bosun", "powder-monkey", "crewman"], 
            "Hard": ["quartermaster", "swashbuckler", "freebooter", "corsair", "admiral"] 
        },
        "Special Items": { 
            "Easy": ["rumflask", "doubloon", "gold", "grog", "patch"], 
            "Medium": ["sea-chart", "blackspot", "compass", "cutlass", "treasure"], 
            "Hard": ["enchantedchest", "sea-shanty", "pieces-of-eight", "mutiny", "piracy"] 
        }
    },
    "Wizard": {
        "Animals": { 
            "Easy": ["phoenix", "imp", "owl", "cat", "bat"], 
            "Medium": ["dragon", "griffin", "toad", "raven", "familiar"], 
            "Hard": ["basilisk", "beholder", "wyvern", "manticores", "lich"] 
        },
        "Objects": { 
            "Easy": ["wand", "orb", "tome", "robe", "staff"], 
            "Medium": ["spellbook", "cauldron", "amulet", "scroll", "ring"], 
            "Hard": ["rune-stone", "phylactery", "scepter", "starshard", "elixir"] 
        },
        "Places": { 
            "Easy": ["tower", "shrine", "chamber", "vault", "cave"], 
            "Medium": ["crystalcave", "faeforest", "library", "school", "hall"], 
            "Hard": ["enchantedgrove", "etherhall", "astral-plane", "nexus", "sanctuary"] 
        },
        "Characters": { 
            "Easy": ["seer", "sorcerer", "warlock", "mage", "sage"], 
            "Medium": ["apprentice", "oracle", "enchanter", "diviner", "shaman"], 
            "Hard": ["archmage", "necromancer", "conjurer", "illusionist", "master"] 
        },
        "Special Items": { 
            "Easy": ["elixir", "rune", "charm", "potion", "spell"], 
            "Medium": ["binding-rune", "starshard", "scroll", "talisman", "magic"], 
            "Hard": ["phoenix-feather", "whisper-talisman", "spell-formula", "mana-bomb", "abjuration"] 
        }
    },
    "Detective": {
        "Animals": { 
            "Easy": ["rat", "pigeon", "dog", "cat", "mouse"], 
            "Medium": ["raven", "hound", "ferret", "owl", "crow"], 
            "Hard": ["bloodhound", "ferret", "alley-cat", "viper", "weasel"] 
        },
        "Objects": { 
            "Easy": ["camera", "notebook", "pen", "hat", "file"], 
            "Medium": ["magnifier", "cufflink", "lockpick", "torch", "watch"], 
            "Hard": ["lockpick", "blueprint", "casefile", "cipher-note", "fingerprint"] 
        },
        "Places": { 
            "Easy": ["alley", "cellar", "office", "street", "pub"], 
            "Medium": ["warehouse", "dockyard", "hotel", "station", "museum"], 
            "Hard": ["speakeasy", "backroom", "gallows", "apartment", "morgue"] 
        },
        "Characters": { 
            "Easy": ["suspect", "witness", "officer", "victim", "client"], 
            "Medium": ["informant", "coroner", "inspector", "detective", "journalist"], 
            "Hard": ["inspector", "mastermind", "alibi", "fugitive", "henchman"] 
        },
        "Special Items": { 
            "Easy": ["alibi", "motive", "clue", "proof", "note"], 
            "Medium": ["casefile", "cipher-note", "evidence", "testimony", "weapon"], 
            "Hard": ["fingerprint", "interrogation", "deduction", "forensics", "break-in"] 
        }
    },
    "Ninja": {
        "Animals": { 
            "Easy": ["viper", "koi", "cat", "owl", "bat"], 
            "Medium": ["falcon", "panther", "raven", "hawk", "snake"], 
            "Hard": ["shadowfox", "komodo-dragon", "tiger", "cobra", "mantis"] 
        },
        "Objects": { 
            "Easy": ["katana", "mask", "shuriken", "rope", "dart"], 
            "Medium": ["shuriken", "rope-dart", "smokescreen", "hook", "chain"], 
            "Hard": ["smokescreen", "chain-sickle", "ninjatō", "kama", "kunai"] 
        },
        "Places": { 
            "Easy": ["dojo", "shrine", "roof", "forest", "village"], 
            "Medium": ["bamboo-grove", "castle-rooftop", "fortress", "swamp", "mountain"], 
            "Hard": ["hiddenvillage", "mountain-pass", "temple", "grotto", "compound"] 
        },
        "Characters": { 
            "Easy": ["sensei", "ronin", "apprentice", "spy", "guard"], 
            "Medium": ["assassin", "apprentice", "master", "warrior", "shadow"], 
            "Hard": ["clanleader", "shogun", "samurai", "warlord", "master"] 
        },
        "Special Items": { 
            "Easy": ["talc", "dart", "smoke", "wire", "trap"], 
            "Medium": ["poison-dart", "stealth-cloak", "camo", "silence", "shadow"], 
            "Hard": ["chakra-stone", "whisper-talisman", "secrecy", "discipline", "assault"] 
        }
    },
    "Explorer": {
        "Animals": { 
            "Easy": ["tiger", "toucan", "monkey", "parrot", "lizard"], 
            "Medium": ["jaguar", "capybara", "boa", "tapir", "sloth"], 
            "Hard": ["anaconda", "chupacabra", "mammoth", "sasquatch", "griffin"] 
        },
        "Objects": { 
            "Easy": ["maproll", "lantern", "compass", "machete", "rope"], 
            "Medium": ["machete", "compass", "satchel", "shovel", "tent"], 
            "Hard": ["satchel", "survival-kit", "revolver", "radio", "shovel"] 
        },
        "Places": { 
            "Easy": ["temple", "canopy", "jungle", "river", "ruin"], 
            "Medium": ["waterfall", "riverbend", "canyon", "pyramid", "oasis"], 
            "Hard": ["lostcity", "pyramid", "plateau", "tomb", "expedition"] 
        },
        "Characters": { 
            "Easy": ["guide", "ranger", "tracker", "scout", "native"], 
            "Medium": ["tracker", "shaman", "archaeologist", "paleontologist", "naturalist"], 
            "Hard": ["archaeologist", "cartographer", "explorer", "adventurer", "pioneer"] 
        },
        "Special Items": { 
            "Easy": ["totem", "idol", "relic", "gem", "coin"], 
            "Medium": ["scrollpiece", "golden-mask", "artifact", "treasure", "amulet"], 
            "Hard": ["ancient-tablet", "crystal-skull", "unearth", "discovery", "mystery"] 
        }
    }
}

def get_word_for(role_name, category_name, difficulty):
    """
    Return a random word based on role name, category, and difficulty.
    """
    words_list = ROLE_WORDS.get(role_name, {}).get(category_name, {}).get(difficulty, [])
    
    if not words_list:
        words_from_all_difficulties = []
        category_data = ROLE_WORDS.get(role_name, {}).get(category_name, {})
        for level in DIFFICULTY_LEVELS:
            words_from_all_difficulties.extend(category_data.get(level, []))
        words_list = words_from_all_difficulties
        
    if not words_list:
        all_words = []
        for role_data in ROLE_WORDS.values():
            for category_data in role_data.values():
                for level_words in category_data.values():
                    all_words.extend(level_words)
        if not all_words:
            return "oracle" 
        return random.choice(all_words).replace(" ", "").replace("-", "").lower()

    w = random.choice(words_list)
    return w.replace(" ", "").replace("-", "").lower()
