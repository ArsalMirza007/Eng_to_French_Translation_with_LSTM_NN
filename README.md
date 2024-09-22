# Eng_to_French_Translation_with_LSTM_NN

## Screenshorts of Application:
![Screenshot (130)](https://github.com/user-attachments/assets/75879ec6-0c83-49ae-a909-e870bf132d5f)
![Screenshot (131)](https://github.com/user-attachments/assets/4820d46b-de59-4a56-a4f2-0e8e0f74a9b8)
![Screenshot (132)](https://github.com/user-attachments/assets/9117e311-3ab5-45e0-a482-208870f2dad5)


## Overview
- This project involves building a machine learning model for translating English sentences into French using a Long Short-Term Memory (LSTM) network. The translation system has been trained on a dataset of English-French sentence pairs and can be accessed via a Flask-based web interface, allowing users to input English sentences and receive French translations.

## Objectives
- Data Preparation: Clean and preprocess a dataset of English and French sentence pairs.
- Tokenization and Padding: Convert sentences into numerical sequences using tokenization and ensure uniform sequence length through padding.
- Model Training: Build and train a sequence-to-sequence LSTM model to learn the mappings between English and French sentences.
- Deployment: Deploy the trained model using a Flask web application for real-time translation.
- User Interface: Create a simple and aesthetically pleasing web interface where users can input English text and receive a French translation.

## Project Workflow
### Data Collection & Preprocessing
- Two datasets, vocab_en.csv and vocab_fr.csv, containing English and French sentences respectively, are loaded.
- Punctuation is removed, and sentences are tokenized to prepare them for model training.
- Tokenization involves converting words to numerical indices, and padding ensures consistent sequence length.

### Model Training
- A sequence-to-sequence LSTM model is built using Keras.
- The model uses an embedding layer to handle input text, followed by an LSTM layer to capture temporal dependencies.
- Another LSTM layer with return sequences enabled is used for the decoder.
- The output layer consists of a time-distributed dense layer with a softmax activation function to predict the French translation.
- The model is compiled with sparse_categorical_crossentropy as the loss function and trained on the prepared data.

### Model Deployment
- The trained model is saved in .h5 format.
- A Flask web application is created where users can input English text and receive French translations.
- The web app loads the trained model and the tokenizers, and performs predictions on user input in real-time.

### User Interface
- A simple and user-friendly interface is created using HTML and CSS.
- Users can enter English sentences and click a 'Translate' button to get the translation.
- The translation is displayed in a visually appealing manner below the input box.
- Technical Stack

### Libraries & Frameworks:
- **TensorFlow & Keras:** For building and training the LSTM model.
- **Flask:** For creating a web interface and deploying the model.
- **Pandas & NumPy:** For data handling and preprocessing.
- **NLTK:** For text processing and tokenization.
- **Jinja2**: For rendering the HTML templates in Flask.

### Web Technologies:
- **HTML/CSS:** For designing the user interface.
.
### Features
- **Real-Time Translation:** Users can translate English sentences to French on-the-fly.
- **User-Friendly Interface:** Simple and intuitive design with clear inputs and results display.
- **Data Preprocessing:** Robust handling of text data including tokenization, padding, and removal of unwanted characters.
- **Scalable Model:** The LSTM model is designed to be scalable and can be fine-tuned with more data for better accuracy.
  
### Future Enhancements
- **Improved Translation Accuracy:** By using a larger dataset and more advanced architectures such as Transformer models.
- **Bi-Directional Translation:** Enable translations from French to English as well.
- **User Authentication:** Allow users to save translations and access them later.
- **Advanced UI:** Enhance the UI with more features like language detection and auto-complete.
  
**This project demonstrates a comprehensive approach to building, training, and deploying a language translation model using deep learning techniques and web technologies.**
