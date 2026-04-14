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

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    print(f"{'Title':<25} {'Score':<8} {'Reasons'}")
    print("-" * 80)
    for rec in recommendations:
        song, score, explanation = rec
        print(f"{song['title']:<25} {score:<8.2f} {explanation}")


if __name__ == "__main__":
    main()
