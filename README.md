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

Real-world music recommendation systems like Spotify and YouTube combine collaborative filtering (analyzing what similar users like) with content-based filtering (matching song attributes to user preferences) to predict what listeners will enjoy next. They prioritize user engagement by balancing familiarity with discovery, using vast amounts of behavioral data (plays, skips, likes) and audio features (tempo, energy, mood). My simplified version focuses on content-based filtering only, prioritizing musical "vibe" matching through numerical similarity scores on key audio features, with categorical boosts for genre and mood matches, to simulate how platforms recommend based on song characteristics rather than user behavior patterns.

**Song Object Features:**
- genre (categorical: pop, lofi, rock, etc.)
- mood (categorical: happy, chill, intense, etc.)  
- energy (numerical 0-1: intensity level)
- tempo_bpm (numerical: beats per minute)
- valence (numerical 0-1: musical positivity/happiness)
- danceability (numerical 0-1: suitability for dancing)
- acousticness (numerical 0-1: acoustic vs. electronic)

**UserProfile Object Features:**
- preferred_genre (categorical)
- preferred_mood (categorical)
- preferred_energy (numerical 0-1)
- preferred_tempo_bpm (numerical)
- preferred_valence (numerical 0-1)
- preferred_danceability (numerical 0-1)
- preferred_acousticness (numerical 0-1)

The Recommender computes a score for each song using Gaussian similarity for numerical features (rewarding closeness to user preferences) and exact-match bonuses for categorical features, then ranks songs by total score to recommend the top matches.

**Algorithm Recipe:**
- **Scoring Formula**: `total_score = genre_bonus + mood_bonus + (energy_sim * 0.8) + (valence_sim * 0.8) + (tempo_sim * 0.6) + (danceability_sim * 0.6) + (acousticness_sim * 0.4)`
- **Categorical Bonuses**: Genre match = +2.0 points, Mood match = +1.0 points
- **Numerical Similarities**: Gaussian similarity `exp(-((song_value - user_pref)^2) / (2 * 0.2^2))` (0-1 scale)
- **Ranking Rule**: Sort songs by total_score descending, return top 5 recommendations

**Potential Biases:**
- **Genre Over-prioritization**: The +2.0 genre bonus might ignore excellent songs that match mood/energy perfectly but are different genres (e.g., a happy rock song for a pop fan)
- **Numerical Dominance**: If numerical similarities are weighted too high, categorical preferences (genre/mood) could be overshadowed, leading to recommendations that feel "close" but wrong in style
- **Content-Only Limitation**: Lacks collaborative filtering, so it can't discover songs popular with similar users, potentially missing serendipitous recommendations
- **Scale Sensitivity**: Gaussian sigma=0.2 might be too strict for some features, creating harsh penalties for small differences

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


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

