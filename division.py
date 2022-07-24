import streamlit as st

st.title('Division of 2 numbers')
a = st.number_input('Enter a number')
b = st.number_input('Enter another number')
if b != 0:
    result = a / b
else:
    result = "Zero error"
st.write(a, ' / ', b , '= ', result)
