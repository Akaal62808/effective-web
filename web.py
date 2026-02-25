import streamlit as st
import time

st.set_page_config(page_title="For Nisha Mam 👑", layout="centered")

# Custom CSS
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #2c003e, #4b006e);
    color: gold;
    text-align: center;
}

.title {
    font-size: 50px;
    font-weight: bold;
    text-shadow: 0 0 20px gold;
}

.message {
    font-size: 22px;
    margin-top: 30px;
}

.stButton>button {
    background-color: gold;
    color: purple;
    border-radius: 30px;
    font-size: 18px;
    padding: 10px 25px;
    box-shadow: 0 0 15px gold;
    transition: 0.3s;
}

.stButton>button:hover {
    background-color: white;
    transform: scale(1.1);
}

</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">Thank You Nisha Mam 👑</div>', unsafe_allow_html=True)

# Typewriter Effect
message = """  
Nisha Mam, tusi sirf teacher nahi ho... tusi saade layi inspiration ho. 💜  

Tuhada support, tuhadi guidance te tuhadi smile hamesha yaad rahegi.  

Asi hamesha thankful rahange ke sanu tuhade vargi Mam mili.  
"""

placeholder = st.empty()
typed_text = ""

for char in message:
    typed_text += char
    placeholder.markdown(f'<div class="message">{typed_text}</div>', unsafe_allow_html=True)
    time.sleep(0.03)

# Special Button
if st.button("Click For Special Message ✨"):
    st.success("We Will Always Miss You Mam 💐👑")
