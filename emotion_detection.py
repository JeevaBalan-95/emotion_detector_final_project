import requests
import json

def emotion_detector(text_to_analyze):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json =  {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=input_json, headers=headers)
    formatted_response = json.loads(response.text)
    
    identified_emotions = formatted_response["emotionPredictions"][0]["emotion"]
    # print(f"Identified emotions are {identified_emotions}")
    
    dominant_emotion = None
    dominant_emotion_score = -1
    for an_emotion in identified_emotions.keys():
        if dominant_emotion_score < identified_emotions[an_emotion]:
            dominant_emotion_score = identified_emotions[an_emotion]
            dominant_emotion = an_emotion

    # print(dominant_emotion)
    # print(dominant_emotion_score)
    identified_emotions["dominant_emotion"] = dominant_emotion

    return identified_emotions


# if __name__ == "__main__":
#     emotion_detector("I love this new technology.")