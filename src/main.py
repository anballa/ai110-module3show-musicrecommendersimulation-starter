"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # System Evaluation: define several user profiles, including edge-case/adversarial preferences
    profiles = [
        (
            "High-Energy Pop",
            {
                "genre": "pop",
                "mood": "happy",
                "energy": 0.9,
                "valence": 0.85,
                "danceability": 0.9,
            },
        ),
        (
            "Chill Lofi",
            {
                "genre": "lofi",
                "mood": "calm",
                "energy": 0.3,
                "acousticness": 0.75,
                "danceability": 0.45,
            },
        ),
        (
            "Deep Intense Rock",
            {
                "genre": "rock",
                "mood": "angry",
                "energy": 0.85,
                "tempo_bpm": 140.0,
                "acousticness": 0.2,
            },
        ),
        (
            "Adversarial Sad Energy",
            {
                "genre": "rock",
                "mood": "sad",
                "energy": 0.9,
                "valence": 0.2,
                "acousticness": 0.1,
            },
        ),
    ]

    for profile_name, user_prefs in profiles:
        print(f"\n=== {profile_name} ===")
        print(f"User prefs: {user_prefs}")

        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\nTop recommendations for {profile_name}:\n")
        print(f"{'Title':<30} {'Score':<8} {'Reasons'}")
        print("-" * 100)
        for song, score, explanation in recommendations:
            print(f"{song['title']:<30} {score:<8.2f} {explanation}")


if __name__ == "__main__":
    main()
