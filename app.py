from flask import Flask, render_template, request
import random

app = Flask(__name__)

# قاعدة بيانات مصغرة للأفلام والمسلسلات
MEDIA_DATA = [
    {
        "id": 1, "title": "Interstellar", "type": "Movie", "genre": "Sci-Fi", 
        "mood": "Mind-bending", "runtime": "2h 49m", "year": 2014, 
        "desc": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
        "rating": "8.7/10"
    },
    {
        "id": 2, "title": "Knives Out", "type": "Movie", "genre": "Mystery", 
        "mood": "Fun", "runtime": "2h 10m", "year": 2019, 
        "desc": "A detective investigates the death of a patriarch of an eccentric, combative family.",
        "rating": "7.9/10"
    },
    {
        "id": 3, "title": "Whiplash", "type": "Movie", "genre": "Drama", 
        "mood": "Intense", "runtime": "1h 46m", "year": 2014, 
        "desc": "A promising young drummer enlists at a cut-throat music conservatory where his instructor will stop at nothing.",
        "rating": "8.5/10"
    },
    {
        "id": 4, "title": "House of the Dragon", "type": "Series", "genre": "Fantasy", 
        "mood": "Intense", "runtime": "2 Seasons", "year": 2022, 
        "desc": "An internal succession war within House Targaryen at the height of its power.",
        "rating": "8.4/10"
    },
    {
        "id": 5, "title": "Modern Family", "type": "Series", "genre": "Comedy", 
        "mood": "Fun", "runtime": "11 Seasons", "year": 2009, 
        "desc": "Three different but related families face trials and tribulations in their own uniquely comedic ways.",
        "rating": "8.5/10"
    },
    {
        "id": 6, "title": "Severance", "type": "Series", "genre": "Sci-Fi", 
        "mood": "Mind-bending", "runtime": "1 Season", "year": 2022, 
        "desc": "Mark leads a team of office workers whose memories have been surgically divided between work and life.",
        "rating": "8.7/10"
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    media_type = request.form.get('type')
    genre = request.form.get('genre')
    mood = request.form.get('mood')

    filtered = MEDIA_DATA

    if media_type and media_type != "Any":
        filtered = [m for m in filtered if m['type'] == media_type]
    
    if genre and genre != "Any":
        filtered = [m for m in filtered if m['genre'] == genre]

    if mood and mood != "Any":
        filtered = [m for m in filtered if m['mood'] == mood]

    if not filtered:
        filtered = MEDIA_DATA

    selected = random.choice(filtered)
    return render_template('result.html', media=selected)

if __name__ == '__main__':
    app.run(debug=True)