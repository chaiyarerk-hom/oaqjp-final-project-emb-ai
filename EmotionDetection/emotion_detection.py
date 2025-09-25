import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers)
    response_obj = json.loads(response.text)
    
    anger = response_obj['emotionPredictions'][0]['emotion']['anger']
    disgust = response_obj['emotionPredictions'][0]['emotion']['disgust']
    fear = response_obj['emotionPredictions'][0]['emotion']['fear']
    joy = response_obj['emotionPredictions'][0]['emotion']['joy']
    sadness = response_obj['emotionPredictions'][0]['emotion']['sadness']

    emo_score = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }

    keys = emo_score.keys()
    max_score = 0
    max_key = ''

    for key in keys:
        if emo_score[key] > max_score:
            max_score = emo_score[key]
            max_key = key
    
    emo_score.update({'dominant_emotion': max_key})

    return emo_score