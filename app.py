from flask import Flask, render_template
import random

app = Flask(__name__)

QUOTES = [
    "“The silence of the stars is louder than the voice of the ocean’s heartbeat.”",
    "“A broken mirror reflects the soul of a shadow.”",
    "“Truth is the wind that never forgets to fold the mountains.”",
    "“To understand the void, you must first fill the cup with echoes.”",
    "“When the horizon burns, the sky remembers the taste of gravity.”",
    "“Only the blind can see the light trapped in a tear of glass.”" ,
    "“The storm’s tears wash away the footprints of the clouds.”",
    "“Knowledge is the flower that blooms in the garden of unspoken dreams.”",
    "“In the reflection of time, eternity wears no face.” ",
    "“To swim in the river of doubt is to drink the fire of truth.” ",
    "“The tree of wisdom grows roots in the ashes of forgotten wings.” ",
    "“Darkness is the lover that embraces the moon’s hidden laughter.” "
]

@app.route("/")
def index():
    quote = random.choice(QUOTES)
    return render_template("index.html",quote=quote)

if __name__ == "__main__":
    app.run(debug=True)