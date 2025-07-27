import streamlit as st
import sklearn
import pickle
import string
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.stem import PorterStemmer

port_stemmer = PorterStemmer()

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

def clean_text(text):
    text = word_tokenize(text) 
    text= " ".join(text) 
    text = [char for char in text if char not in string.punctuation] 
    text = ''.join(text) 
    text = [char for char in text if char not in re.findall(r"[0-9]", text)] 
    text = ''.join(text) 
    text = [word.lower() for word in text.split() if word.lower() not in set(stopwords.words('english'))] 
    text = ' '.join(text) 
    text = list(map(lambda x: port_stemmer.stem(x), text.split()))
    return " ".join(text)   

st.title("SMS Spam Classifier")

input_sms = st.text_input("Enter the Message to check if it's spam or not")

if st.button('Predict'):

    if input_sms == "":
        st.header('Please Enter Your Message !!!')

    else:

        #Preprocessing
        transform_text = clean_text(input_sms)

        #Vectorizing
        vector_input = tfidf.transform([transform_text])

        #Predicting
        result = model.predict(vector_input)

        #Displaying

        if result == 1:
            st.header(" This is a SPAM message")
        else:
            st.header(" This is NOT a spam message")
st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: transparent;
        color: gray;
        text-align: center;
        padding: 10px;
    }
    </style>
    <div class="footer">
        Project by: Srijita Ghorai
    </div>
""", unsafe_allow_html=True)

