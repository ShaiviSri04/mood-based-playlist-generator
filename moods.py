# moods.py - Stores all mood and playlist data for the generator

# Dictionary of moods mapped to playlists
# Each mood has a list of songs: (title, artist)
MOOD_PLAYLISTS = {
    "happy": {
        "vibe": "Sunshine & Good Vibes ☀️",
        "songs": [
            ("Happy", "Pharrell Williams"),
            ("Can't Stop the Feeling", "Justin Timberlake"),
            ("Uptown Funk", "Mark Ronson ft. Bruno Mars"),
            ("Good as Hell", "Lizzo"),
            ("Walking on Sunshine", "Katrina and the Waves"),
            ("Shake It Off", "Taylor Swift"),
            ("I Gotta Feeling", "Black Eyed Peas"),
            ("Dancing Queen", "ABBA"),
        ],
    },
    "sad": {
        "vibe": "Rainy Day Feels 🌧️",
        "songs": [
            ("Someone Like You", "Adele"),
            ("The Night We Met", "Lord Huron"),
            ("Fix You", "Coldplay"),
            ("Let Her Go", "Passenger"),
            ("Skinny Love", "Bon Iver"),
            ("The Scientist", "Coldplay"),
            ("Liability", "Lorde"),
            ("When the Party's Over", "Billie Eilish"),
        ],
    },
    "angry": {
        "vibe": "Let It All Out 🔥",
        "songs": [
            ("Break Stuff", "Limp Bizkit"),
            ("Killing in the Name", "Rage Against the Machine"),
            ("Given Up", "Linkin Park"),
            ("Numb", "Linkin Park"),
            ("In the End", "Linkin Park"),
            ("Bulls on Parade", "Rage Against the Machine"),
            ("Chop Suey!", "System of a Down"),
            ("Down with the Sickness", "Disturbed"),
        ],
    },
    "chill": {
        "vibe": "Easy Breezy 🌿",
        "songs": [
            ("Sunset Lover", "Petit Biscuit"),
            ("Redbone", "Childish Gambino"),
            ("Come and Get Your Love", "Redbone"),
            ("Sunday Morning", "Maroon 5"),
            ("Budapest", "George Ezra"),
            ("Put It All on Me", "Ed Sheeran"),
            ("Banana Pancakes", "Jack Johnson"),
            ("Better Together", "Jack Johnson"),
        ],
    },
    "motivated": {
        "vibe": "Beast Mode Activated 💪",
        "songs": [
            ("Lose Yourself", "Eminem"),
            ("Eye of the Tiger", "Survivor"),
            ("Stronger", "Kanye West"),
            ("Till I Collapse", "Eminem"),
            ("Hall of Fame", "The Script"),
            ("Unstoppable", "Sia"),
            ("Can't Hold Us", "Macklemore & Ryan Lewis"),
            ("Legends Never Die", "Against the Current"),
        ],
    },
    "romantic": {
        "vibe": "Love in the Air 💕",
        "songs": [
            ("Perfect", "Ed Sheeran"),
            ("All of Me", "John Legend"),
            ("Make You Feel My Love", "Adele"),
            ("Thinking Out Loud", "Ed Sheeran"),
            ("A Thousand Years", "Christina Perri"),
            ("Can't Help Falling in Love", "Elvis Presley"),
            ("Lucky", "Jason Mraz ft. Colbie Caillat"),
            ("Your Song", "Elton John"),
        ],
    },
}

# Keyword mapping to help detect mood from user input
MOOD_KEYWORDS = {
    "happy": ["happy", "excited", "joy", "great", "awesome", "good", "wonderful", "cheerful", "amazing", "fantastic"],
    "sad": ["sad", "upset", "depressed", "down", "lonely", "heartbroken", "gloomy", "miserable", "blue", "unhappy"],
    "angry": ["angry", "mad", "frustrated", "annoyed", "furious", "irritated", "rage", "pissed", "agitated"],
    "chill": ["chill", "relaxed", "calm", "peaceful", "tired", "lazy", "easy", "mellow", "laid back", "cozy"],
    "motivated": ["motivated", "focused", "productive", "energetic", "pumped", "determined", "driven", "ready"],
    "romantic": ["romantic", "love", "crush", "date", "valentine", "affectionate", "tender", "sweet"],
}