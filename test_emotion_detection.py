import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    
    def test_emotion_detector_joy(self):
        """Test emotion detector with joyful text"""
        result = emotion_detector('I am glad this happened')
        self.assertEqual(result['dominant_emotion'], 'joy')
    
    def test_emotion_detector_anger(self):
        """Test emotion detector with angry text"""
        result = emotion_detector('I am really mad about this')
        self.assertEqual(result['dominant_emotion'], 'anger')
    
    def test_emotion_detector_disgust(self):
        """Test emotion detector with disgusting text"""
        result = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result['dominant_emotion'], 'disgust')
    
    def test_emotion_detector_sadness(self):
        """Test emotion detector with sad text"""
        result = emotion_detector('I am so sad about this')
        self.assertEqual(result['dominant_emotion'], 'sadness')
    
    def test_emotion_detector_fear(self):
        """Test emotion detector with fearful text"""
        result = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result['dominant_emotion'], 'fear')
    
    def test_emotion_detector_blank_text(self):
        """Test emotion detector with blank text"""
        result = emotion_detector('')
        self.assertIsNone(result['dominant_emotion'])

if __name__ == '__main__':
    unittest.main()