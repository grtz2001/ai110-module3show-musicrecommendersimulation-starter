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

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    headers = ("#", "Title", "Artist", "Score", "Reasons")
    rows = [headers]
    for rank, rec in enumerate(recommendations, start=1):
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        rows.append((str(rank), song["title"], song["artist"], f"{score:.2f}", explanation.replace("; ", ", ")))

    widths = [max(len(row[col]) for row in rows) for col in range(len(headers))]

    def print_row(row):
        print(" | ".join(cell.ljust(widths[i]) for i, cell in enumerate(row)))

    print("\nTop recommendations:\n")
    print_row(headers)
    print("-+-".join("-" * w for w in widths))
    for row in rows[1:]:
        print_row(row)
    print()


if __name__ == "__main__":
    main()
