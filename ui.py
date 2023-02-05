import streamlit as st
import json
import requests

st.title("Basic Iris App 💻")

st.write('')
st.write('Select the numbers from slider below: ⏬')
sepal_length = st.slider('sepal_length', 4.3, 7.9, 0.1)
sepal_width = st.slider('sepal_width', 2.0, 4.4, 0.1)
petal_length = st.slider('petal_length', 1.0, 6.9, 0.1)
petal_width = st.slider('petal_width', 0.1, 2.5, 0.1)

# coverting the inputs into a json format
inputs = {
  "data_array": [sepal_length, sepal_width, petal_length, petal_width],
}

# when the user clicks on button it will fetch the API
if st.button('Predict'):
    res = requests.post(url = 'http://127.0.0.1:8000/predict', data = json.dumps(inputs))

    st.subheader(f'Response from API 🚀 = {res.text}')