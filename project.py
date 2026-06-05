from moods import MOOD_PLAYLISTS, MOOD_KEYWORDS
import re
import random
from datetime import date, datetime
import statistics
import sys
import csv 

#step 1: detect mood from text input
def get_mood_from_input(text):
    text=text.lower().strip()
    for mood,keywords in MOOD_KEYWORDS.items():
        for keyword in keywords:
            if re.search(rf"\b{keyword}\b",text):
                return mood 
            
    return None  

#step 2: after identifying the mood, we will generate the playlist
def generate_playlist(mood,num_songs=5):
    if mood not in MOOD_PLAYLISTS:
        raise ValueError(f"Unknown mood: '{mood}'. Choose from {list(MOOD_PLAYLISTS.keys())}")
    songs=MOOD_PLAYLISTS[mood]["songs"].copy()
    random.shuffle(songs)
    return songs[:num_songs]

#step 3: return the vibe of the generated playlist
def get_vibe(mood):
    if mood not in MOOD_PLAYLISTS:
        raise ValueError(f"Unknown mood: '{mood}")
    return MOOD_PLAYLISTS[mood]["vibe"]

#step 4: now format the songs to display
def format_song(index,title,artist):
    return f"{index}. {title.title()} - {artist.title()}"

#step 5: save song history into a CSV file
def save_to_history(mood,playlist):
    filename = "history.csv"
    session_id = datetime.now().isoformat()

    with open(filename,"a",newline="") as f:
        writer = csv.writer(f)
        for title,artist in playlist:
            writer.writerow([session_id, mood, title, artist])
        print(f"\n Playlist saved to '{filename}'")

#step 6: read from CSV file
def load_history():
    filename="history.csv"
    try:
        with open(filename,"r") as f:
            reader = csv.reader(f)
            rows=list(reader)

        if not rows:
            print("No history found yet")
            return 
        
        #group songs by date
        sessions={}
        for row in rows:
            date_key = row[0]
            if date_key not in sessions:
                sessions[date_key]=[]
            sessions[date_key].append((row[1],row[2],row[3]))

        for session_date,entries in sessions.items():
            mood=entries[0][0]
            print(f"{session_date} - Mood: {mood.capitalize()}")
            for _,title,artist in entries:
                print(f"     • {title} — {artist}")
            print()
    except FileNotFoundError:
        print("No history found yet. Generate a playlist first")

#step 7: now generate stats using csv file
def get_mood_stats():
    
    filename="history.csv"
    try:
        with open(filename,"r") as f:
            reader = csv.reader(f)
            rows=list(reader)
            if not rows:
                print("No stats yet")
                return
        
            mood_counts={}
            for row in rows:
                mood=row[1]
                mood_counts[mood]=mood_counts.get(mood,0)+1

            sorted_moods=sorted(mood_counts.items(),key=lambda x: x[1],reverse=True)
            counts=list(mood_counts.values())
            avg=statistics.mean(counts)

            print("\n Your Mood Stats:\n")
            for mood, count in sorted_moods:
                bar = "█" * count
                print(f"  {mood.capitalize():<12} {bar} ({count} songs)")
            print(f"\n  Average songs per mood: {avg:.1f}")
 
    except FileNotFoundError:
        print("No stats yet. Generate a playlist first!")

def validate_name(name):
    return bool(re.fullmatch(r"[A-Za-z ]+", name.strip()))

def ask_mood_interactively():
    valid_moods = list(MOOD_PLAYLISTS.keys())
 
    print("\nHow are you feeling? You can:")
    print("  • Type a mood directly:", ", ".join(valid_moods))
    print("  • Or describe how you feel (e.g. 'I feel really tired and lazy')\n")

    while True:
        user_input=input("Your mood:").strip()

        if not user_input:
            print("Please enter something")
            continue

        #if direct mood input
        if user_input.lower() in valid_moods:
            return user_input.lower()
        
        #otherwise detect mood
        detected=get_mood_from_input(user_input)
        if detected:
            return detected
        
        print(f"Couldn't detect your mood. Please choose from: {', '.join(valid_moods)}")

def ask_num_songs():
    while True:
        try:
            n = int(input("How many songs? (1-8, default 5): ").strip() or "5")
            if 1<=n<=8:
                return n
            print("Please enter a number between 1 and 8.")
        except ValueError:
            print("That's not a valid number.")

def main():
    if len(sys.argv)>1:
        flag=sys.argv[1].lower()
        if flag == "--history":
            load_history()
            sys.exit(0)
        elif flag == "--stats":
            get_mood_stats()
            sys.exit(0)
        elif flag == "--help":
            print("Usage:")
            print("  python project.py              → Generate a playlist")
            print("  python project.py --history    → View past playlists")
            print("  python project.py --stats      → View mood statistics")
            sys.exit(0)
        else:
            print(f"❌ Unknown flag '{sys.argv[1]}'. Use --help for usage info.")
            sys.exit(1)

    while True:
        name = input("\nWhat's your name? ").strip()
        if validate_name(name):
            break
        print("Name should only contain letters.")
 
    print(f"\nHey {name.title()}! Let's find the perfect playlist for you.\n")

    while True:
        mood=ask_mood_interactively()
        num_songs=ask_num_songs()

        playlist = generate_playlist(mood,num_songs)
        vibe=get_vibe(mood)

        print(f"\n Vibe: {vibe}\n")

        for i, (title,artist) in enumerate(playlist,start=1):
            print(format_song(i,title,artist))

        save_to_history(mood,playlist)

        print("\nWhat would you like to do next?")
        print("  1. Generate another playlist")
        print("  2. View my history")
        print("  3. View mood stats")
        print("  4. Exit")

        while True:
            choice = input("\nYour choice (1/2/3/4): ").strip()
            if choice in ["1", "2", "3", "4"]:
                break
            print("Please enter 1, 2, 3, or 4.")
 
        if choice == "1":
            continue
        elif choice == "2":
            load_history()
        elif choice == "3":
            get_mood_stats()
        elif choice == "4":
            print(f"\nSee you later, {name.title()}! Keep vibing! 🎵\n")
            sys.exit(0)
 
 
if __name__ == "__main__":
    main()



    



        
