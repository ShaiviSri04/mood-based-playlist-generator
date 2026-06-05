import pytest
from project import (get_mood_from_input, generate_playlist, get_vibe, format_song, validate_name)

def test_detect_happy():
    assert get_mood_from_input("I feel so happy today")=="happy"

def test_detect_sad():
    assert get_mood_from_input("I am really sad and lonely") == "sad"

def test_detect_chill():
    assert get_mood_from_input("feeling very chill and relaxed") == "chill"

def test_detect_motivated():
    assert get_mood_from_input("I am so motivated to work") == "motivated"

def test_detect_unknown_returns_none():
    assert get_mood_from_input("blah blah xyz") is None
 
def test_detect_case_insensitive():
    assert get_mood_from_input("I AM SO HAPPY") == "happy"

def test_playlist_length():
    playist=generate_playlist("happy",5)
    assert len(playist)==5

def test_playlist_returns_tuples():
    playlist=generate_playlist("chill",3)
    for item in playlist:
        assert isinstance(item,tuple)
        assert len(item)==2

def test_playlist_invalid_mood_raises_error():
    with pytest.raises(ValueError):
        generate_playlist("confused")

def test_playlist_default_does_not_exceed_available():
    playlist=generate_playlist("sad",8)
    assert len(playlist)<=8

def test_vibe_returns_string():
    vibe = get_vibe("happy")
    assert isinstance(vibe, str)
 
def test_vibe_invalid_mood_raises_error():
    with pytest.raises(ValueError):
        get_vibe("sleepy")

def test_format_song_contains_index():
    result = format_song(1, "happy", "pharrell williams")
    assert "1." in result
 
def test_format_song_contains_title():
    result = format_song(2, "lose yourself", "eminem")
    assert "Lose Yourself" in result  # title() applied
 
def test_format_song_contains_artist():
    result = format_song(3, "numb", "linkin park")
    assert "Linkin Park" in result

def test_format_song_contains_index():
    result = format_song(1, "happy", "pharrell williams")
    assert "1." in result
 
def test_format_song_contains_title():
    result = format_song(2, "lose yourself", "eminem")
    assert "Lose Yourself" in result  # title() applied
 
def test_format_song_contains_artist():
    result = format_song(3, "numb", "linkin park")
    assert "Linkin Park" in result