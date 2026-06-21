
import streamlit as st

st.title("🏥 AI Medical Chatbot")
st.write("Ask me anything about health!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    else:
        st.chat_message("assistant").write(message["content"])

def get_response(msg):
    msg = msg.lower()
    if any(w in msg for w in ["hello","hi","salam"]):
        return "Hello! I am your medical assistant!"
    elif any(w in msg for w in ["diabetes","sugar","glucose"]):
        return "Normal glucose: 4-7 mmol/L. Above 11 = Diabetes risk!"
    elif any(w in msg for w in ["pressure","bp"]):
        return "Normal BP: 120/80 mmHg. Above 140/90 = High BP!"
    elif any(w in msg for w in ["ph","acid"]):
        return "Normal blood pH: 7.35 to 7.45"
    elif any(w in msg for w in ["fever","temperature"]):
        return "Normal temp: 37C. Above 37.5C = Fever!"
    else:
        return "I can help with diabetes, BP, pH and fever!"

if prompt := st.chat_input("Type your question..."):
    st.chat_message("user").write(prompt)
    st.session_state.messages.append(
        {"role": "user", "content": prompt})
    response = get_response(prompt)
    st.chat_message("assistant").write(response)
    st.session_state.messages.append(
        {"role": "assistant", "content": response})
