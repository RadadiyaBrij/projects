🎙️ Jarvis Voice Assistant

A simple Python-based personal voice assistant that listens to your voice commands and performs tasks like searching Wikipedia, opening websites or apps, and telling the current time.

🚀 Features:

-> Voice interaction using speech_recognition and pyttsx3

-> Searches information from Wikipedia

->  Opens websites (YouTube, Google) and desktop apps (Chrome, WhatsApp, JioSaavn, VS Code)

->  Tells the current time

->  Greets you based on the time of day

Requirements:

Install dependencies with:

    pip install pyttsx3, SpeechRecognition, pyaudio, wikipedia

🛠️ How to Run:

    Save the script as jarvis.py

Run in terminal:

    python jarvis.py


Speak commands like:

    “Wikipedia Albert Einstein”

    “Open YouTube”

    “What’s the time?”

    “Open VS Code”

⚙️ Main Modules Used

    pyttsx3 – text-to-speech engine

    speech_recognition – converts speech to text

    wikipedia – fetches summaries

    webbrowser / os – opens links and applications
