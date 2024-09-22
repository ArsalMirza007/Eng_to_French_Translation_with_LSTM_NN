import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer 
import pickle

# Step 1: Load your dataset
# Assuming your dataset files are named 'vocab_en.csv' and 'vocab_fr.csv'

df_english = pd.read_csv('data/vocab_en.csv', sep='\t', names=['english'])
df_french = pd.read_csv('data/vocab_fr.csv', sep='\t', names=['french'])

# Step 2: Combine the datasets into a single DataFrame
df = pd.DataFrame({'english': df_english['english'], 'french': df_french['french']})

# Step 3: Create English Tokenizer
english_tokenizer = Tokenizer(char_level=False)
english_tokenizer.fit_on_texts(df['english'])

# Save English tokenizer
with open('english_tokenizer.pkl', 'wb') as f:
    pickle.dump(english_tokenizer, f)

# Step 4: Create French Tokenizer
french_tokenizer = Tokenizer(char_level=False)
french_tokenizer.fit_on_texts(df['french'])

# Save French tokenizer
with open('french_tokenizer.pkl', 'wb') as f:
    pickle.dump(french_tokenizer, f)

print("Tokenizers have been created and saved successfully!")
