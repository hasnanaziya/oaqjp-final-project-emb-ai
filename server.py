'''
Emotion Detector Flask Application
This Flask application provides an API endpoint for emotion detection. 
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    '''
    This method handles the emotion detection fuunctionality
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze:
        return "Invalid text! Please try again!."

    dominant_emotion = emotion_detector(text_to_analyze)['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again."

    return f"The given text has been identified as {dominant_emotion}."
    #return (f"For the given statement, the system response is 'anger':  {anger},
    #'disgust':  {disgust}, 'fear':  {fear}, 'joy':  {joy},'sadness':  {sadness}
    #and the dominant emotion is  {dominant_emotion}")


@app.route("/")
def render_index_page():
    """
    Endpoint to render the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
