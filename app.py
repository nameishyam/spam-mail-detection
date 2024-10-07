import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    
    text = y[:]
    y.clear()
    
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
            
    text = y[:]
    y.clear()
    
    for i in text:
        y.append(ps.stem(i))
    
            
    return " ".join(y)

tfidf = pickle.load(open('C:\\Users\\gedda\\OneDrive\\Desktop\\ML PROJECT\\vectorizer.pkl', 'rb'))
model = pickle.load(open('C:\\Users\\gedda\\OneDrive\\Desktop\\ML PROJECT\\model.pkl', 'rb'))

st.title("email classifier")

input_mail = st.text_input("Enter the text to classify")

if (st.button("Predict")):

    transformed_email = transform_text(input_mail)

    vector_input = tfidf.transform([transformed_email])

    result = model.predict(vector_input)[0]

    if result == 0:
        st.header("Not Spam!")
    else:
        st.header("Spam!")