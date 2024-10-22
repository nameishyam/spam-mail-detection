from flask import Flask, request, render_template
import pickle
import nltk
import numpy as np
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

porter_stemmer = PorterStemmer()

# Load the trained model and vectorizer
tfidf_vectorizer = pickle.load(open('./models/vectorizer.pkl', 'rb'))
spam_model = pickle.load(open('./models/model.pkl', 'rb'))

def tokenize_text(text):
    return nltk.word_tokenize(text.lower())

def filter_tokens(tokens):
    return [token for token in tokens if token.isalnum() and token not in stopwords.words('english')]

def stem_tokens(tokens):
    return [porter_stemmer.stem(token) for token in tokens]

def transform_text(text):
    tokens = tokenize_text(text)
    filtered_tokens = filter_tokens(tokens)
    stemmed_tokens = stem_tokens(filtered_tokens)
    return " ".join(stemmed_tokens)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_mail = request.form.get('mail_content')
        if not input_mail:
            return 'Invalid input', 400
        
        transformed_email = transform_text(input_mail)
        
        vector_input = tfidf_vectorizer.transform([transformed_email])
        
        prediction = spam_model.predict(vector_input)
        
        if prediction == 0:
            output = 'Not a Spam Mail!'
        else:
            output = 'Spam Mail!'
        
        return render_template('index.html', prediction_text='Prediction: {}'.format(output))
    except Exception as e:
        return f'Error occurred: {str(e)}'

if __name__ == "__main__":
    app.run(debug=True)
