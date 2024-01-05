Text Extraction Web Application
This Flask web application is designed to extract text from either PDF or audio files. It utilizes the Flask framework for the web interface and includes functionality for text extraction from PDFs and audio files using the PyMuPDF and SpeechRecognition libraries.

Table of Contents
Installation
Usage
Endpoints
File Types Supported
Installation
1.Make sure you have Python installed on your system.

2.Install the required Python packages by running:
   pip install flask PyMuPDF SpeechRecognition
3.Clone this repository to your local machine.
   git clone <repository-url>
4.Navigate to the project directory.
   cd <project-directory>
5.Run the application.
   python app.py
   
Usage
Access the web application by opening your browser and navigating to http://localhost:5000.
The main page (/) contains a simple interface with a file upload button.
Upload either a PDF or audio file using the provided button.
After uploading, the application will extract text from the file.
The extracted text will be displayed as a JSON response.
Endpoints
/: Main page with the file upload interface.
/upload: Endpoint for handling file uploads and text extraction.
File Types Supported
PDF: Text extraction from PDF files using the PyMuPDF library.
Audio: Text extraction from audio files (.wav or .mp3) using the SpeechRecognition library.
