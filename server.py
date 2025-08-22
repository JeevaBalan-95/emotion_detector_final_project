""" A web application for Emotion Detection """
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/")
def render_index_page():
    """Returns the Index Page"""
    return render_template('index.html')


@app.route("/emotionDetector")
def detect_emotion():
    """Detects the Emotion and sends the response"""
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    # Return a formatted string with the sentiment label and score
    return (f"For the given statement, the system response is 'anger': {response['anger']}, "
                f"'disgust': {response['disgust']}, "
                f"'fear': {response['fear']}, "
                f"'joy': {response['joy']} "
                f"and 'sadness': {response['sadness']}. "
                f"The dominant emotion is <b>{response['dominant_emotion']}</b>")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
