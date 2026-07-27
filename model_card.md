# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**MoodMatch 1.0**

---

## 2. Intended Use  

MoodMatch suggests songs based on genre, mood, and energy. It's a classroom project, not a real product. It assumes the user can name one genre, one mood, and one energy level (0 to 1) that describes what they want.

---

## 3. How the Model Works  

Each song gets points based on how well it fits what the user wants. Same genre as the user? +1 point. Same mood? +1 point. Close energy level? Up to +1 point, less the further apart they are. All the points get added up, and the highest-scoring songs win.

I changed the starting weights: genre used to be worth double mood, and energy was worth half a point. I made genre and energy equal instead, to see if it changed the results.

---

## 4. Data  

The catalog has 18 songs. Genres include pop, rock, lofi, metal, classical, jazz, folk, and more — most genres only have one song each. Moods include happy, chill, intense, romantic, and others. I didn't add or remove any songs.

Missing: no blended genres like "pop rock," no mood called "angsty," and few songs at medium energy levels. Fast, high-energy genres and slow, low-energy genres never overlap.

---

## 5. Strengths  

It works well when the user's genre and mood actually exist in the catalog. Chill Lofi and Deep Intense Rock both got clean, sensible top picks that matched their genre, mood, and energy all at once. When there's a real match in the data, the scoring finds it.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

In this catalog, intense genres (metal, rock, EDM) are always high energy, and mellow genres (classical, ambient, folk) are always low energy. So a classical fan who wants high energy gets metal or rock songs instead — pure energy match, wrong genre. The system never says "no good match found." It just confidently picks the highest score anyway.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

I tested three profiles: **Pop-Rock Angsty** (pop rock, angsty, energy 0.65), **Chill Lofi** (lofi, chill, energy 0.35), and **Deep Intense Rock** (rock, intense, energy 0.90).

What surprised me: "pop rock" and "angsty" don't exist in the catalog, so Pop-Rock Angsty got zero genre or mood credit anywhere. It still confidently returned a top pick — "Shadow Ledger," a hip-hop song — based on energy alone.

**Comparisons:**

- **Pop-Rock Angsty vs. Deep Intense Rock:** Both want "rock," but only the exact word "rock" exists in the data. Deep Intense Rock matches genre and mood; Pop-Rock Angsty matches neither.
- **Deep Intense Rock vs. Chill Lofi:** Opposite results (high energy vs. low energy), and both are clean matches. Makes sense since their genres and moods are both real, just at opposite energy levels.
- **Chill Lofi vs. Pop-Rock Angsty:** Chill Lofi is a real match; Pop-Rock Angsty is just an energy coincidence. But both get shown the same confident way, with a precise-looking score.

---

## 8. Future Work  

- Let genres partly match (like "pop rock" counting toward "pop" and "rock").
- Tell the user when there's no real match, instead of quietly guessing.
- Limit how many songs from the same genre or artist show up in the top results.
- Let users weigh genre, mood, and energy themselves, instead of fixed points.

---

## 9. Personal Reflection  

I learned that small changes to scoring weights can flip which song wins. The most surprising part was that the system never says "I'm not sure" — it always picks a top song, even when nothing really matches, and shows it with the same confidence either way. This made me realize real recommendation apps probably do this too, and it's worth being skeptical of a confident-looking result.
