from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow.keras.models import load_model 
import numpy as np
import pickle

# Load the trained model
model = load_model('Translator.h5')

# Load tokenizers
with open('english_tokenizer.pkl', 'rb') as f:
    english_tokenizer = pickle.load(f)
    
with open('french_tokenizer.pkl', 'rb') as f:
    french_tokenizer = pickle.load(f)

# Function to translate an English sentence to French
def translate_sentence(sentence):
    # Tokenize and pad the input sentence
    sequence = english_tokenizer.texts_to_sequences([sentence])
    padded_sequence = tf.keras.preprocessing.sequence.pad_sequences(sequence, maxlen=20, padding='post')
    
    # Predict translation using the model
    predictions = model.predict(padded_sequence)
    translated_sequence = np.argmax(predictions, axis=-1)[0]  # Get the predicted indices

    # Convert indices to words
    translated_sentence = ' '.join([french_tokenizer.index_word.get(i, '') for i in translated_sequence if i > 0])
    return translated_sentence

# Initialize Flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    translation = ""
    if request.method == 'POST':
        english_sentence = request.form['english_sentence']
        translation = translate_sentence(english_sentence)
    return render_template('index.html', translation=translation)

if __name__ == '__main__':
    app.run(debug=True)
