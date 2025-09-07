# Emotion Detection Application

A web-based emotion detection application built with Flask that analyzes text and identifies emotions using Watson NLU API with a local fallback system.

## Features

- **Real-time emotion analysis** from text input
- **Watson NLU API integration** for accurate emotion detection
- **Local fallback system** when API is unavailable
- **Clean, responsive web interface**
- **Support for 5 emotions**: joy, anger, sadness, fear, disgust
- **Dominant emotion identification**

## Installation

### Prerequisites
- Python 3.7+
- pip package manager

### Setup

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/emotion-detection-app.git
cd emotion-detection-app
```

2. **Install required packages:**
```bash
pip install flask requests
```

3. **Run the application:**
```bash
python server.py
```

4. **Open your browser:**
Navigate to `http://127.0.0.1:5000`

## Project Structure

```
emotion_detection_project/
│
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
│
├── templates/
│   └── index.html
│
├── server.py
├── test_emotion_detection.py
└── README.md
```

## Usage

1. Enter text in the input field
2. Click "Analyze Emotion" button
3. View the emotion scores and dominant emotion

### Example Input/Output

**Input:** "I am very happy today!"

**Output:** 
```
For the given statement, the system response is 'anger': 0.123456, 'disgust': 0.087654, 'fear': 0.098765, 'joy': 0.789123 and 'sadness': 0.054321. The dominant emotion is joy.
```

## API Endpoints

### `/emotionDetector`
- **Method:** GET
- **Parameter:** `textToAnalyze` (string)
- **Returns:** Formatted emotion analysis result

### Example API Call
```bash
curl "http://127.0.0.1:5000/emotionDetector?textToAnalyze=I%20am%20happy"
```

## Technology Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **API:** Watson NLU Emotion API
- **Fallback:** Custom emotion detection algorithm

## How It Works

1. **Primary Method:** Uses Watson Natural Language Understanding API for emotion analysis
2. **Fallback Method:** When Watson API is unavailable, uses a local keyword-based emotion detection system
3. **Emotion Scoring:** Returns confidence scores for all five emotions
4. **Dominant Emotion:** Identifies the emotion with the highest confidence score

## Development

### Adding New Features
- Modify `emotion_detection.py` for new emotion analysis logic
- Update `templates/index.html` for UI changes
- Extend `server.py` for new endpoints

### Testing
```bash
python test_emotion_detection.py
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Watson Natural Language Understanding API for emotion analysis
- Flask framework for web application development

