import tkinter as tk
from tkinter import messagebox, ttk
from textblob import TextBlob
from googletrans import Translator
from spellchecker import SpellChecker

# Initialize Translator and SpellChecker
translator = Translator()
spell = SpellChecker()

# Functions for text analysis

# Function to analyze the sentiment of the input text
def analyze_sentiment():
    text = input_text.get("1.0", "end-1c")  # Get the text from the input box
    if not text.strip():  # Check if the text is empty
        messagebox.showerror("Error", "Please enter some text!")  # Show error if empty
        return
    blob = TextBlob(text)  # Create a TextBlob object
    sentiment = blob.sentiment  # Analyze sentiment
    result = f"Polarity: {sentiment.polarity}, Subjectivity: {sentiment.subjectivity}"  # Format result
    output_label.config(text=result)  # Display result in output label

# Function to correct spelling errors in the input text
def correct_spelling():
    text = input_text.get("1.0", "end-1c")  # Get the text from the input box
    if not text.strip():  # Check if the text is empty
        messagebox.showerror("Error", "Please enter some text!")  # Show error if empty
        return
    words = text.split()  # Split text into words
    corrected_words = []
    for word in words:
        if word.lower() in spell:  # Check if word is already correct
            corrected_words.append(word)
        else:
            corrected_words.append(spell.correction(word) or word)  # Correct the word or keep it as is
    corrected_text = ' '.join(corrected_words)  # Join corrected words back into a string
    output_label.config(text=f"Corrected Text: {corrected_text}")  # Display corrected text

# Function to detect the language of the input text
def detect_language():
    text = input_text.get("1.0", "end-1c")  # Get the text from the input box
    if not text.strip():  # Check if the text is empty
        messagebox.showerror("Error", "Please enter some text!")  # Show error if empty
        return
    try:
        detection = translator.detect(text)  # Detect the language
        output_label.config(text=f"Detected Language: {detection.lang}")  # Display detected language
    except Exception as e:  # Handle any errors during detection
        output_label.config(text=f"Error detecting language: {e}")

# Function to translate the input text to a specified target language
def translate_text():
    text = input_text.get("1.0", "end-1c")  # Get the text from the input box
    target_language = language_entry.get()  # Get the target language code
    if not text.strip():  # Check if the text is empty
        messagebox.showerror("Error", "Please enter some text!")  # Show error if empty
        return
    if not target_language.strip():  # Check if the target language is empty
        messagebox.showerror("Error", "Please enter a target language code!")  # Show error if empty
        return
    try:
        translation = translator.translate(text, dest=target_language)  # Translate the text
        output_label.config(text=f"Translated Text: {translation.text}")  # Display the translation
    except Exception as e:  # Handle any errors during translation
        output_label.config(text=f"Translation Error: {e}")

# GUI Setup
root = tk.Tk()
root.title("Text Analysis Tool")  # Set the window title
root.geometry("600x500")  # Set the window size
root.configure(bg="#f4f4f4")  # Set the background color

# Title Label
title_label = tk.Label(root, text="Text Analysis Tool", font=("Arial", 20, "bold"), bg="#f4f4f4", fg="#333")
title_label.pack(pady=10)  # Add some padding for spacing

# Input Frame for text entry
input_frame = tk.Frame(root, bg="#f4f4f4")
input_frame.pack(pady=10)  # Add some padding for spacing

# Input text label and text box
tk.Label(input_frame, text="Enter Text:", font=("Arial", 12), bg="#f4f4f4").grid(row=0, column=0, sticky="w")
input_text = tk.Text(input_frame, height=8, width=60, font=("Arial", 10))  # Multi-line text box for input
input_text.grid(row=1, column=0, padx=5, pady=5)

# Buttons Frame for different functionalities
buttons_frame = tk.Frame(root, bg="#f4f4f4")
buttons_frame.pack(pady=10)

# Add buttons for various text analysis features
tk.Button(buttons_frame, text="Analyze Sentiment", command=analyze_sentiment, bg="#0078D7", fg="white", font=("Arial", 10), width=18).grid(row=0, column=0, padx=5, pady=5)
tk.Button(buttons_frame, text="Correct Spelling", command=correct_spelling, bg="#0078D7", fg="white", font=("Arial", 10), width=18).grid(row=0, column=1, padx=5, pady=5)
tk.Button(buttons_frame, text="Detect Language", command=detect_language, bg="#0078D7", fg="white", font=("Arial", 10), width=18).grid(row=1, column=0, padx=5, pady=5)
tk.Button(buttons_frame, text="Translate Text", command=translate_text, bg="#0078D7", fg="white", font=("Arial", 10), width=18).grid(row=1, column=1, padx=5, pady=5)

# Frame for translation language input
translation_frame = tk.Frame(root, bg="#f4f4f4")
translation_frame.pack(pady=10)

# Label and entry for target language code
tk.Label(translation_frame, text="Target Language Code (e.g., 'es' for Spanish):", font=("Arial", 12), bg="#f4f4f4").grid(row=0, column=0, sticky="w")
language_entry = tk.Entry(translation_frame, font=("Arial", 10), width=10)  # Entry box for language code
language_entry.grid(row=0, column=1, padx=5, pady=5)

# Output Label to display results
output_label = tk.Label(root, text="", font=("Arial", 12), bg="#f4f4f4", fg="#0078D7", wraplength=550, justify="center")
output_label.pack(pady=20)

# Run the GUI
root.mainloop()  # Start the main event loop
