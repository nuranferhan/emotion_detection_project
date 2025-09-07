from EmotionDetection.emotion_detection import emotion_detector
import json

def test_emotion_function():
    """Test the emotion detector function with sample inputs"""
    
    test_cases = [
        "I am very happy today",
        "I am really angry about this situation",
        "This makes me feel disgusted",
        "I am so sad about what happened",
        "I am afraid of what might happen",
        ""  # Empty string test
    ]
    
    print("Testing emotion detection function...")
    print("=" * 50)
    
    for i, text in enumerate(test_cases, 1):
        print(f"\nTest {i}: '{text}'")
        try:
            result = emotion_detector(text)
            print("Result:", json.dumps(result, indent=2))
            
            if result['dominant_emotion'] is not None:
                print(f"Dominant emotion: {result['dominant_emotion']}")
            else:
                print("No dominant emotion detected (likely invalid input)")
                
        except Exception as e:
            print(f"Error: {e}")
    
    print("\n" + "=" * 50)
    print("Testing completed.")

if __name__ == "__main__":
    test_emotion_function()