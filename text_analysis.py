import tkinter as tk
from tkinter import messagebox, ttk
from textblob import TextBlob
from googletrans import Translator
from spellchecker import SpellChecker

# Initialize Translator and SpellChecker
translator = Translator()
spell = SpellChecker()

# Functions for text analysis
def analyze_sentiment():
    text = input_text.get("1.0", "end-1c")
    if not text.strip():
        messagebox.showerror("Error", "Please enter some text!")
        return
    blob = TextBlob(text)
    sentiment = blob.sentiment
    result = f"Polarity: {sentiment.polarity}, Subjectivity: {sentiment.subjectivity}"
    output_label.config(text=result)

def correct_spelling():
    text = input_text.get("1.0", "end-1c")
    if not text.strip():
        messagebox.showerror("Error", "Please enter some text!")
        return
    words = text.split()
    corrected_words = []
    for word in words:
        if word.lower() in spell:
            corrected_words.append(word)
        else:
            corrected_words.append(spell.correction(word) or word)
    corrected_text = ' '.join(corrected_words)
    output_label.config(text=f"Corrected Text: {corrected_text}")

def detect_language():
    text = input_text.get("1.0", "end-1c")
    if not text.strip():
        messagebox.showerror("Error", "Please enter some text!")
        return
    try:
        detection = translator.detect(text)
        output_label.config(text=f"Detected Language: {detection.lang}")
    except Exception as e:
        output_label.config(text=f"Error detecting language: {e}")

def translate_text():
    text = input_text.get("1.0", "end-1c")
    target_language = language_entry.get()
    if not text.strip():
        messagebox.showerror("Error", "Please enter some text!")
        return
    if not target_language.strip():
        messagebox.showerror("Error", "Please enter a target language code!")
        return
    try:
        translation = translator.translate(text, dest=target_language)
        output_label.config(text=f"Translated Text: {translation.text}")
    except Exception as e:
        output_label.config(text=f"Translation Error: {e}")

# GUI Setup
root = tk.Tk()
root.title("Text Analysis Tool")
root.geometry("600x500")  # Set the window size
root.configure(bg="#f4f4f4")  # Background color

# Title Label
title_label = tk.Label(root, text="Text Analysis Tool", font=("Arial", 20, "bold"), bg="#f4f4f4", fg="#333")
title_label.pack(pady=10)

# Input Frame
input_frame = tk.Frame(root, bg="#f4f4f4")
input_frame.pack(pady=10)

tk.Label(input_frame, text="Enter Text:", font=("Arial", 12), bg="#f4f4f4").grid(row=0, column=0, sticky="w")
input_text = tk.Text(input_frame, height=8, width=60, font=("Arial", 10))
input_text.grid(row=1, column=0, padx=5, pady=5)

# Buttons Frame
buttons_frame = tk.Frame(root, bg="#f4f4f4")
buttons_frame.pack(pady=10)

tk.Button(buttons_frame, text="Analyze Sentiment", command=analyze_sentiment, bg="#0078D7", fg="white", font=("Arial", 10), width=18).grid(row=0, column=0, padx=5, pady=5)
tk.Button(buttons_frame, text="Correct Spelling", command=correct_spelling, bg="#0078D7", fg="white", font=("Arial", 10), width=18).grid(row=0, column=1, padx=5, pady=5)
tk.Button(buttons_frame, text="Detect Language", command=detect_language, bg="#0078D7", fg="white", font=("Arial", 10), width=18).grid(row=1, column=0, padx=5, pady=5)
tk.Button(buttons_frame, text="Translate Text", command=translate_text, bg="#0078D7", fg="white", font=("Arial", 10), width=18).grid(row=1, column=1, padx=5, pady=5)

# Translation Frame
translation_frame = tk.Frame(root, bg="#f4f4f4")
translation_frame.pack(pady=10)

tk.Label(translation_frame, text="Target Language Code (e.g., 'es' for Spanish):", font=("Arial", 12), bg="#f4f4f4").grid(row=0, column=0, sticky="w")
language_entry = tk.Entry(translation_frame, font=("Arial", 10), width=10)
language_entry.grid(row=0, column=1, padx=5, pady=5)

# Output Label
output_label = tk.Label(root, text="", font=("Arial", 12), bg="#f4f4f4", fg="#0078D7", wraplength=550, justify="center")
output_label.pack(pady=20)

# Run the GUI
root.mainloop()
