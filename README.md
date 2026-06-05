# 🎵 Mood Based Playlist Generator

A command-line Python application that generates personalized playlists based on a user's mood. Inspired by concepts taught in Harvard's **CS50P: Introduction to Programming with Python**, this project combines user interaction, data processing, file handling, regular expressions, statistics, and testing into a real-world application.

---

## Problem

Imagine opening Spotify and not knowing what to listen to.

You may know how you're feeling:

* Happy
* Sad
* Angry
* Chill
* Motivated
* Romantic

But you don't know which songs fit that mood.

This project solves that problem by:

1. Understanding the user's mood
2. Generating a playlist that matches that mood
3. Saving playlist history
4. Analyzing mood statistics over time

---

## Features

### Mood Detection

Users can either:

* Enter a mood directly

```text
happy
```

or describe how they feel:

```text
I feel really tired and relaxed today
```

The application uses keyword matching and regular expressions to determine the most appropriate mood.

---

### Playlist Generation

Once a mood is identified, the application:

* Retrieves songs associated with that mood
* Randomly shuffles the playlist
* Returns a user-selected number of songs

Example:

```text
1. Happy - Pharrell Williams
2. Good as Hell - Lizzo
3. Shake It Off - Taylor Swift
```

---

### Mood Vibes

Each mood includes a descriptive vibe:

```text
Mood: Happy

Vibe:
Energetic, uplifting, and positive.
```

This improves the user experience and adds context to each playlist.

---

### Playlist History

Every generated playlist is saved to a CSV file.

Information stored:

* Session ID
* Mood
* Song Title
* Artist

Example:

```csv
2026-06-05T14:32:21,happy,Happy,Pharrell Williams
2026-06-05T14:32:21,happy,Good as Hell,Lizzo
```

---

### Mood Statistics

The application analyzes historical data and displays:

* Most frequently used moods
* Song counts per mood
* Average songs generated per mood

Example:

```text
Happy       ███████ (7 songs)
Sad         ████ (4 songs)
Angry       ██ (2 songs)

Average songs per mood: 4.3
```

---

## Project Structure

```text
mood_based_playlist/
│
├── project.py
├── moods.py
├── test_project.py
├── history.csv
├── README.md
└── .gitignore
```

---

## Topics Covered (CS50P Concepts)

This project was designed to practice and demonstrate concepts learned throughout Harvard CS50P.

### Variables

```python
mood = "happy"
```

---

### Functions

```python
generate_playlist()
get_vibe()
save_to_history()
load_history()
```

Functions help organize code into reusable building blocks.

---

### Conditionals

```python
if mood not in MOOD_PLAYLISTS:
    raise ValueError(...)
```

Used to make decisions based on user input.

---

### Loops

```python
for song in playlist:
```

```python
while True:
```

Used for repetition and input validation.

---

### Dictionaries

```python
MOOD_PLAYLISTS = {
    "happy": {...},
    "sad": {...}
}
```

Used for fast mood lookups.

---

### Lists

```python
songs = [...]
```

Used to store collections of songs.

---

### Tuples

```python
("Happy", "Pharrell Williams")
```

Used to represent immutable song records.

---

### Regular Expressions

```python
re.search(rf"\b{keyword}\b", text)
```

Used for detecting mood-related keywords inside user input.

---

### Exceptions

```python
raise ValueError(...)
```

```python
try:
    ...
except FileNotFoundError:
```

Used for robust error handling.

---

### File I/O

```python
with open(...)
```

Used for reading and writing playlist history.

---

### CSV Processing

```python
csv.writer(...)
csv.reader(...)
```

Used for persistent data storage.

---

### Date & Time

```python
datetime.now().isoformat()
```

Used to uniquely identify playlist sessions.

---

### Lambda Functions

```python
key=lambda x: x[1]
```

Used when sorting mood statistics.

---

### Statistics Module

```python
statistics.mean(...)
```

Used to calculate average songs generated per mood.

---

### Command-Line Arguments

```python
python project.py --history
python project.py --stats
```

Implemented using:

```python
sys.argv
```

---

### Unit Testing

Implemented using:

```python
pytest
```

Tests verify:

* Playlist length
* Playlist structure
* Error handling
* Playlist generation behavior

---

## Running The Project

### Clone Repository

```bash
git clone <repository-url>
```

---

### Navigate To Project

```bash
cd mood_based_playlist
```

---

### Run Application

```bash
python project.py
```

---

## Additional Commands

### View History

```bash
python project.py --history
```

---

### View Statistics

```bash
python project.py --stats
```

---

### Help

```bash
python project.py --help
```

---

## Running Tests

Install pytest:

```bash
pip install pytest
```

Run tests:

```bash
pytest test_project.py
```

---

## Sample Workflow

```text
What's your name?
> Shaivi

How are you feeling?
> I feel really cheerful today

Detected Mood: Happy

Vibe:
Energetic, uplifting, and positive.

1. Happy - Pharrell Williams
2. Good as Hell - Lizzo
3. Shake It Off - Taylor Swift
```

---

## Future Improvements

Potential enhancements:

* Spotify API integration
* Export playlists to JSON
* Playlist recommendations using machine learning
* GUI version using Tkinter
* Web version using Flask
* User authentication
* Data visualization dashboards

---

## Acknowledgements

This project was inspired by concepts taught in:

**Harvard CS50P – Introduction to Programming with Python**

Special thanks to **David J. Malan** and the CS50 team for making computer science accessible, engaging, and fun.

---

