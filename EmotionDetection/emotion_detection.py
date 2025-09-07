import requests
import json
import re
import random

def local_emotion_detector(text):

    if not text or text.strip() == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Convert to lowercase for matching
    text_lower = text.lower()
  
    emotion_keywords = {
        'joy': {
            'keywords': ['happy', 'glad', 'joyful', 'excited', 'cheerful', 'pleased', 'delighted', 
                        'satisfied', 'great', 'wonderful', 'amazing', 'fantastic', 'awesome', 
                        'good', 'excellent', 'love', 'perfect', 'brilliant', 'outstanding',
                        'smile', 'laugh', 'celebrate', 'enjoy', 'bliss', 'euphoric', 'elated',
                        'thrilled', 'overjoyed', 'content', 'grateful', 'blessed'],
            'multiplier': 1.2
        },
        'anger': {
            'keywords': ['angry', 'mad', 'furious', 'enraged', 'irritated', 'annoyed', 
                        'frustrated', 'outraged', 'hate', 'livid', 'pissed', 'rage', 
                        'stupid', 'damn', 'horrible', 'terrible', 'disgusting', 'awful',
                        'infuriate', 'aggravate', 'provoke', 'upset', 'hostile', 'bitter'],
            'multiplier': 1.1
        },
        'sadness': {
            'keywords': ['sad', 'depressed', 'unhappy', 'miserable', 'sorrowful', 'gloomy', 
                        'melancholy', 'dejected', 'downhearted', 'heartbroken', 'crying', 
                        'tears', 'sorry', 'unfortunate', 'disappointed', 'grief', 'mourn',
                        'lonely', 'hopeless', 'despair', 'blue', 'down', 'low'],
            'multiplier': 1.0
        },
        'fear': {
            'keywords': ['afraid', 'scared', 'frightened', 'terrified', 'anxious', 'worried', 
                        'nervous', 'panic', 'fearful', 'apprehensive', 'concerned', 'stress', 
                        'tension', 'uncertainty', 'dread', 'horror', 'terror', 'phobia',
                        'alarm', 'unease', 'distress', 'trouble'],
            'multiplier': 1.0
        },
        'disgust': {
            'keywords': ['disgusted', 'revolted', 'repulsed', 'sickened', 'nauseated', 'gross', 
                        'disgusting', 'awful', 'nasty', 'repugnant', 'offensive', 'vile',
                        'loathe', 'abhor', 'detest', 'reprehensible', 'revolting', 'foul'],
            'multiplier': 1.0
        }
    }
    
    emotion_scores = {}
    total_words = len(text.split())
    
    for emotion, data in emotion_keywords.items():
        score = 0.0
        keywords = data['keywords']
        multiplier = data['multiplier']
        
        for keyword in keywords:
           
            pattern = r'\b' + re.escape(keyword) + r'\b'
            matches = len(re.findall(pattern, text_lower))
            if matches > 0:
              
                word_score = matches * multiplier
                score += word_score
        
 
        base_score = random.uniform(0.05, 0.15)
        
   
        if score > 0:
           
            normalized_score = min((score / max(total_words, 1)) * 2, 0.8)
            final_score = base_score + normalized_score + random.uniform(0.1, 0.3)
            emotion_scores[emotion] = min(round(final_score, 6), 1.0)
        else:
            emotion_scores[emotion] = round(base_score, 6)
    
  
    total_score = sum(emotion_scores.values())
    if total_score > 3.0:  
        factor = 2.5 / total_score
        for emotion in emotion_scores:
            emotion_scores[emotion] = round(emotion_scores[emotion] * factor, 6)
    
   
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    return {
        'anger': emotion_scores['anger'],
        'disgust': emotion_scores['disgust'],
        'fear': emotion_scores['fear'],
        'joy': emotion_scores['joy'],
        'sadness': emotion_scores['sadness'],
        'dominant_emotion': dominant_emotion
    }

def emotion_detector(text_to_analyse):

    print(f"emotion_detector called with: '{text_to_analyse}'")
    
  
    if not text_to_analyse or text_to_analyse.strip() == "":
        print("Empty or None text detected")
        return {
            'anger': None,
            'disgust': None, 
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
   
    try:
        print("Trying Watson API...")
        url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
        headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
        myobj = {"raw_document": {"text": text_to_analyse}}
        
        response = requests.post(url, json=myobj, headers=headers, timeout=5)
        
        if response.status_code == 200:
            print("Watson API success")
            formatted_response = json.loads(response.text)
            emotions = formatted_response['emotionPredictions'][0]['emotion']
            
            emotion_scores = {
                'anger': round(emotions.get('anger', 0.0), 6),
                'disgust': round(emotions.get('disgust', 0.0), 6),
                'fear': round(emotions.get('fear', 0.0), 6),
                'joy': round(emotions.get('joy', 0.0), 6),
                'sadness': round(emotions.get('sadness', 0.0), 6)
            }
            
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)
            emotion_scores['dominant_emotion'] = dominant_emotion
            
            print(f"Watson result: {emotion_scores}")
            return emotion_scores
        else:
            print(f"Watson API failed with status: {response.status_code}")
            raise Exception(f"Watson API returned status {response.status_code}")
            
    except Exception as e:
        print(f"Watson API error: {e}")
        print("Falling back to local emotion detector...")

    result = local_emotion_detector(text_to_analyse)
    print(f"Local detector result: {result}")
    return result