from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector')
def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] == None:
        return {'message': 'Invalid text! Please try again!'}

    return "For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {}, 'sadness': {}. The dominant emotion is {}.".format(response['anger'], response['disgust'], response['fear'], response['joy'], response['sadness'], response['dominant_emotion'])

if __name__ == "__main__":
    app.run(port=5000)
