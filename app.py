# app.py

from flask import Flask, request, jsonify, render_template
import pickle
import nltk
import numpy as np
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string

nltk.download('punkt_tab')

ps = PorterStemmer()

# Load the trained model
tfidf = pickle.load(open('D:\\render\\vectorizer.pkl', 'rb'))
model = pickle.load(open('D:\\render\\model.pkl', 'rb'))

def transform_text(text):
    text = text.lower()
    words = nltk.word_tokenize(text)
    
    filtered_words = [word for word in words if word.isalnum()]
    filtered_words = [word for word in filtered_words if word not in stopwords.words('english') and word not in string.punctuation]
    stemmed_words = [ps.stem(word) for word in filtered_words]
    
    return " ".join(stemmed_words)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract data from form
    input_mail = request.form.get('mail_content')  # Assuming the form field is named 'email'
    
    if not input_mail:
        return 'Invalid input', 400
    
    transformed_email = transform_text(input_mail)
    vector_input = tfidf.transform([transformed_email])  # Remove the outer list
    
    # Make prediction
    prediction = model.predict(vector_input)[0]
    if prediction == 0:
        output = 'Not Spam!'
    else:
        output = 'Spam!'

    return render_template('index.html', prediction_text='Prediction: {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)