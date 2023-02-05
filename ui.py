import streamlit as st
import json
import requests

st.title("Basic Calculator App 💻")

# taking user inputs
option = st.selectbox('Operatoin: ', ['add', 'sub', 'div', 'mul'])

st.write('')
st.write('Select the numbers from slider below: ⏬')
x = st.slider('x', 0, 100, 1)
y = st.slider('y', 0, 100, 1)

# coverting the inputs into a json format
inputs = {
  "operation": option,
  "x": x,
  "y": y
}

# when the user clicks on button it will fetch the API
if st.button('Calculate'):
    res = requests.post(url = 'http://127.0.0.1:8000/calculate', data = json.dumps(inputs))

    st.subheader(f'Response from API 🚀 = {res.text}')