import requests
import json


def emotion_detector(text_to_analyze):
    '''
        This funtion performsemotion detection
    '''
    #url of the sentiment analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    #headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    #Create a dictionary with the text that needs to be analyzed
    myobj = {"raw_document" : {"text": text_to_analyze}}

    #send post request to the API
    response = requests.post(url, json = myobj, headers=header)

    #return reponse text
    #return response.text
    formatted_response = json.loads(response.text)
    
    if response.status_code == 200:
        emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion_predictions.items(), key=lambda x: x[1])[0]

        return {
            'anger': emotion_predictions['anger'],
            'disgust': emotion_predictions['disgust'],
            'fear': emotion_predictions['fear'],
            'joy': emotion_predictions['joy'],
            'sadness': emotion_predictions['sadness'],
            'dominant_emotion': dominant_emotion
        }
    else:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
