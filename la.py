#Step 1: Import libraries
import string as s
import random as r
import streamlit as st



#Step 2: The password generator function
def generate_password(length: int)-> str:
    # Compin all characters together
    all_chars = s.ascii_letters + s.digits + s.punctuation
    
    # Define the empty password
    password = ''
    
    # Repeat the random choice
    for n in range(length):
        password += r.choice(all_chars)

    # Return the password
    return password
# Step 3: The men stremlit app
with st.sidebar:
    password_number = st.number_input(
        label='How many passwords',
        min_value=1,
        max_value=1000,
        value=1,
    )

    password_length = st.slider(
        label='Length of the password',
        min_value=8,
        max_value=100,
        value=16,
    )
    button = st.button('Generate Passwords')
    

st.title('Secure Password Generator')
st.header(':green[Generated Passwords:]')

if button:
    for i in range(password_number):
        result = generate_password(password_length)
        st.code(result)
