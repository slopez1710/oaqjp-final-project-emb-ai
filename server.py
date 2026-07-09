"""
Flask server for the Emotion Detection web application.
Handles routing for the index page and emotion detection API.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(
    __name__,
    template_folder='oaqjp-final-project-emb-ai/templates',
    static_folder='oaqjp-final-project-emb-ai/static'
)

@app.route("/")
def render_index_page():
    """
    Render the main HTML page for the Emotion Detection app.
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def run_emotion_detector():
    """
    Receive text from the frontend, run emotion detection,
    and return the dominant emotion or an error message.
    """
    text = request.args.get("textToAnalyze")
    result = emotion_detector(text)

    if result["dominant_emotion"] is None:
        return "Invalid input: please enter text."

    return result["dominant_emotion"]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
