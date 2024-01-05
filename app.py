# Import necessary modules 
from flask import Flask, request, jsonify
import fitz
import speech_recognition as sr

# Create a Flask web application 
app = Flask(__name__)

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    # Open the PDF document 
    doc = fitz.open(pdf_path)
    text = ""

    # GO through each page of the PDF and concatenate text
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()

    # Close the PDF document
    doc.close()
    return text

# Function to extract text from an audio 
def extract_text_from_audio(audio_file_path):
    # Create a speech recognition recognizer
    recognizer = sr.Recognizer()

    # Open the audio file and adjust for ambient noise
    with sr.AudioFile(audio_file_path) as source:
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.record(source)
        # to convert audio to text
        text = recognizer.recognize_google(audio_data)

    return text

# extract text based on file type (PDF or audio)
def extract_text(file_path):
    # Check the file type and perform extraction
    if file_path.lower().endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.lower().endswith(('.wav', '.mp3')):
        return extract_text_from_audio(file_path)
    else:
        raise ValueError("Unsupported file type. Please provide a PDF or audio file.")

# serve the main index.html file
@app.route('/')
def index():
    return app.send_static_file('index.html')

# Route to handle file upload and text extraction
@app.route('/upload', methods=['POST'])
def upload_file():
    # Get the uploaded file from the request
    uploaded_file = request.files['file']

    # Save the uploaded file to a known location
    file_path = 'uploads/' + uploaded_file.filename
    uploaded_file.save(file_path)

    # Extract text from the uploaded file
    result = extract_text(file_path)

    # Return the extracted text 
    return jsonify({"message": "TEXT EXTRACTED : \n" + result})

# Run the Flask web application
if __name__ == '__main__':
    app.run(debug=True)
