"""To route the application"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """To show the landing page"""
    return render_template('index.html')

@app.route('/emotionDetector')
def sent_detector():
    """To analyze and show the emotion detector result"""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return {'message': 'Invalid text! Please try again!'}

    return (f"For the given statement, the system response is"
    f"'anger': {response['anger']},"
    f"'disgust': {response['disgust']},"
    f"'fear': {response['fear']},"
    f"'joy': {response['joy']},"
    f"'sadness': {response['sadness']}."
    f"The dominant emotion is {response['dominant_emotion']}.")

if __name__ == "__main__":
    app.run(port=5000)
