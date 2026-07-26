# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.
Answer:
Song — holds title, artist, genre, and mood as labels, plus the three features that drive scoring: energy, valence, and danceability. I use those three because the others (tempo, acousticness) just repeat energy.

UserProfile — stores the user's target value for each of those three features, e.g. energy 0.4, valence 0.6, danceability 0.6. Set by hand or averaged from liked songs.

Recommender scoring — for each feature, score = 1 − the gap between the song and the target. Closer means higher. Average the three into one score per song.

Picking songs — score every song, sort high to low, drop the current song, return the top few.

-

The system recommends songs by matching each song against a user's taste profile. It runs in three steps:

1. Input. The user profile holds a favorite genre, a favorite mood, and three target values: energy, valence, and danceability. The songs come from songs.csv.

2. Process (scoring). The system loops through every song and gives each one a score based on how well it matches the profile. Genre and mood are all-or-nothing matches. The three numeric features score by closeness—the nearer a song's value is to the target, the more points it earns.

3. Output (ranking). Once every song has a score, the system sorts them high to low, drops the song already playing, and returns the top few.

Algorithm Recipe
score = 2.0  if genre matches
      + 1.0  if mood matches
      + 0.5 × (1 − |energy − target_energy|)
      + 0.5 × (1 − |valence − target_valence|)
      + 0.5 × (1 − |danceability − target_danceability|)

Max score is 4.5. Genre and mood make up most of it (3.0), so they lead. The numeric features (1.5 total) fine-tune the order within a match.

Possible Biases
-Genre gets too much weight. Genre is worth 2.0 points—the biggest single lever. A great song in a different genre can lose to a weak song in the right genre. The system may miss good matches just because the genre label is off.
-Mood is easy to miss. Moods are very specific (angsty, chill, moody, dreamy...). A song has to match the exact label to earn the point, so close-but-not-exact moods get nothing.
-Scores bunch up. The closeness math rarely hits 0, so even bad matches score something. Songs can end up with similar totals, making the order between them less meaningful.
-No sense of popularity or novelty. It only measures similarity to your taste. It won't surface a hit you'd love that sits outside your usual profile.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
PS C:\Users\marit\OneDrive\Escritorio\ai110-module3show-musicrecommendersimulation-starter> python .\src\main.py
Loaded songs: 18

Top recommendations:

# | Title            | Artist        | Score | Reasons                                                        
--+------------------+---------------+-------+----------------------------------------------------------------
1 | Sunrise City     | Neon Echo     | 3.49  | genre match (+2.0), mood match (+1.0), energy closeness (+0.49)
2 | Gym Hero         | Max Pulse     | 2.44  | genre match (+2.0), energy closeness (+0.43)                   
3 | Rooftop Lights   | Indigo Parade | 1.48  | mood match (+1.0), energy closeness (+0.48)                    
4 | Night Drive Loop | Neon Echo     | 0.47  | energy closeness (+0.47)                                       
5 | Storm Runner     | Voltline      | 0.45  | energy closeness (+0.45)                                       

```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



