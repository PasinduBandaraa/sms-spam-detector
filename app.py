import streamlit as st

import pickle
import string
import nltk
from nltk.corpus import stopwords

from nltk.stem.porter import PorterStemmer

st.set_page_config(
     page_title="SMS Spam",
     page_icon="🅱️",
)

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


# tab1, tab2, tab3 = st.tabs(["Home", "SMS Classifier", "Awareness"])


# with tab1:
# st.title("Home")

# with tab2:
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.image('Logo.png')


st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):

    transformed_text = transform_text(input_sms)

    vector_input = tfidf.transform([transformed_text])
    result = model.predict(vector_input)[0]

    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
