from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Returns a list of dictionaries with song data.
    Converts numerical fields to appropriate types.
    """
    import csv
    
    songs = []
    with open(csv_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert numerical fields
            song_dict = {
                'id': int(row['id']),
                'title': row['title'],
                'artist': row['artist'],
                'genre': row['genre'],
                'mood': row['mood'],
                'energy': float(row['energy']),
                'tempo_bpm': float(row['tempo_bpm']),
                'valence': float(row['valence']),
                'danceability': float(row['danceability']),
                'acousticness': float(row['acousticness'])
            }
            songs.append(song_dict)
    
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Scores a single song based on user preferences and returns score with reasons."""
    import math
    
    score = 0.0
    reasons = []
    
    # Categorical bonuses
    if song['genre'] == user_prefs.get('genre'):
        score += 1.0  # experimental weight shift: reduce genre influence
        reasons.append(f"genre match (+1.0)")
    
    if song['mood'] == user_prefs.get('mood'):
        score += 1.0
        reasons.append(f"mood match (+1.0)")
    
    # Numerical similarities with Gaussian
    sigma = 0.2
    numerical_features = [
        ('energy', 1.6),  # experimental weight shift: emphasize energy more strongly
        ('valence', 0.8), 
        ('tempo_bpm', 0.6),
        ('danceability', 0.6),
        ('acousticness', 0.4)
    ]
    
    for feature, weight in numerical_features:
        if feature in user_prefs and feature in song:
            user_val = user_prefs[feature]
            song_val = song[feature]
            similarity = math.exp(-((song_val - user_val) ** 2) / (2 * sigma ** 2))
            weighted_sim = similarity * weight
            score += weighted_sim
            reasons.append(f"{feature} similarity ({similarity:.2f} * {weight} = {weighted_sim:.2f})")
    
    return (score, reasons)

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Recommends top k songs by scoring and ranking all songs."""
    # Score all songs and create (song, score, explanation) tuples
    scored_songs = [
        (song, score, "; ".join(reasons))
        for song in songs
        for score, reasons in [score_song(user_prefs, song)]
    ]
    
    # Sort by score descending and return top k
    return sorted(scored_songs, key=lambda x: x[1], reverse=True)[:k]
