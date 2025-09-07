from flask import Flask, request, render_template, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers.pop('Content-Security-Policy', None)
    response.headers.pop('X-Content-Security-Policy', None)
    response.headers.pop('X-WebKit-CSP', None)
    return response

@app.route("/emotionDetector")
def sent_emotion_detector():
    """
    Endpoint to detect emotions in text

    Returns:
        str: Formatted string with emotion analysis results
    """
    # Get text to analyze from query parameters
    text_to_analyze = request.args.get('textToAnalyze', '')
    
    # Debug: Print what we received
    print(f"\n=== EMOTION DETECTOR ENDPOINT ===")
    print(f"Raw text received: '{text_to_analyze}'")
    print(f"Text length: {len(text_to_analyze) if text_to_analyze else 0}")
    print(f"Text type: {type(text_to_analyze)}")
    print(f"All args: {request.args}")
    
    # URL decode işlemi (Flask otomatik yapar ama emin olalım)
    try:
        from urllib.parse import unquote
        decoded_text = unquote(text_to_analyze)
        print(f"URL decoded text: '{decoded_text}'")
        text_to_analyze = decoded_text
    except Exception as e:
        print(f"URL decode error: {e}")
    
    # Check for None or empty text
    if not text_to_analyze or text_to_analyze.strip() == "":
        print("❌ Empty text detected - returning invalid text message")
        return "Invalid text! Please try again!"

    try:
        print(f"🔄 Calling emotion_detector with: '{text_to_analyze}'")
        
        # Call emotion detector function
        response = emotion_detector(text_to_analyze)
        
        # Debug: Print response
        print(f"✅ Emotion detector response: {response}")
        print(f"Response type: {type(response)}")
        
        # Check if the dominant emotion is None (invalid input)
        if response is None:
            print("❌ Response is None")
            return "Invalid text! Please try again!"
            
        if not isinstance(response, dict):
            print(f"❌ Response is not a dict: {type(response)}")
            return "Error: Invalid response format!"
            
        dominant_emotion = response.get('dominant_emotion')
        if dominant_emotion is None:
            print("❌ No dominant emotion found")
            return "Invalid text! Please try again!"

        # Format the response string
        anger = response.get('anger', 0)
        disgust = response.get('disgust', 0)
        fear = response.get('fear', 0)
        joy = response.get('joy', 0)
        sadness = response.get('sadness', 0)

        print(f"📊 Emotion scores - anger: {anger}, disgust: {disgust}, fear: {fear}, joy: {joy}, sadness: {sadness}")
        print(f"🎯 Dominant emotion: {dominant_emotion}")

        # Create formatted response
        formatted_response = (
            f"For the given statement, the system response is "
            f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
            f"'joy': {joy} and 'sadness': {sadness}. "
            f"The dominant emotion is {dominant_emotion}."
        )

        print(f"📤 Formatted response: {formatted_response}")
        print("=== END EMOTION DETECTOR ===\n")
        return formatted_response
        
    except Exception as e:
        print(f"❌ Error in emotion detection: {e}")
        print(f"Error type: {type(e)}")
        import traceback
        traceback.print_exc()
        return f"Error analyzing text: {str(e)}"


@app.route("/")
def render_index_page():
    """
    Render the main index page
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)