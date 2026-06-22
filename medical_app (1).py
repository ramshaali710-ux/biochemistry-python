
import streamlit as st

st.set_page_config(
    page_title="Medical AI Assistant",
    page_icon="🏥",
    layout="centered"
)

st.title("🏥 Medical AI Assistant")
st.caption("Powered by Biochemistry + AI")

# Sidebar
with st.sidebar:
    st.header("About")
    st.info("Built by Ramsha — Biochemistry Graduate + AI Developer")
    st.success("Ask about: Diabetes, BP, pH, Fever, Medicines")
    st.warning("Always consult a real doctor!")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Hello! I am your AI Medical Assistant. I can help with diabetes, blood pressure, blood pH, fever and medicines. What would you like to know?"
    })

# Show messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Response function
def get_response(msg):
    msg = msg.lower()

    if any(w in msg for w in ["hello","hi","salam","hey"]):
        return "Hello! How can I help you today? Ask me about diabetes, blood pressure, pH or fever!"

    elif any(w in msg for w in ["diabetes","sugar","glucose","insulin"]):
        return """**Diabetes Information:**
- Type 1: Body makes no insulin
- Type 2: Body resists insulin
- Normal glucose: 4-7 mmol/L
- Diabetic: above 11 mmol/L
- Common medicines: Metformin, Insulin
- Tip: Exercise and healthy diet help!
⚠️ Please consult your doctor."""

    elif any(w in msg for w in ["blood pressure","bp","hypertension","pressure"]):
        return """**Blood Pressure Info:**
- Normal: 120/80 mmHg
- High: above 140/90 mmHg
- Low: below 90/60 mmHg
- Medicines: Amlodipine, Lisinopril
- Tip: Reduce salt and exercise daily!
⚠️ Please consult your doctor."""

    elif any(w in msg for w in ["ph","acid","alkaline","acidosis","alkalosis"]):
        return """**Blood pH Information:**
- Normal: 7.35 to 7.45
- Acidosis: below 7.35
- Alkalosis: above 7.45
- Measured by: ABG blood test
- Causes: kidney/lung problems
⚠️ Please consult your doctor."""

    elif any(w in msg for w in ["fever","temperature","hot","paracetamol"]):
        return """**Fever Information:**
- Normal temp: 37°C / 98.6°F
- Low fever: 37.5 - 38°C
- High fever: above 38°C
- Medicine: Paracetamol 500mg
- Tip: Drink plenty of water!
⚠️ See doctor if fever persists."""

    elif any(w in msg for w in ["metformin"]):
        return """**Metformin Information:**
- Type: Antidiabetic medicine
- Use: Type 2 Diabetes
- Dose: 500mg to 2000mg daily
- Side effects: Nausea, stomach upset
- Take: With food to reduce side effects
⚠️ Only take as prescribed by doctor."""

    elif any(w in msg for w in ["aspirin"]):
        return """**Aspirin Information:**
- Type: Pain reliever / Blood thinner
- Uses: Pain, fever, heart protection
- Dose: 75mg to 500mg
- Side effects: Stomach irritation
- Avoid: If you have stomach ulcers
⚠️ Only take as prescribed by doctor."""

    elif any(w in msg for w in ["thank","thanks","shukriya"]):
        return "You are welcome! Stay healthy! 😊 Feel free to ask anything!"

    elif any(w in msg for w in ["bye","goodbye","khuda hafiz"]):
        return "Goodbye! Take care of your health! 💊"

    else:
        return """I can help you with:
- 🩸 Diabetes and glucose
- ❤️ Blood pressure
- 🧪 Blood pH levels
- 🌡️ Fever and temperature
- 💊 Common medicines

Please ask about these topics!"""

# Chat input
if prompt := st.chat_input("Ask your medical question here..."):
    st.chat_message("user").write(prompt)
    st.session_state.messages.append(
        {"role": "user", "content": prompt})

    response = get_response(prompt)
    st.chat_message("assistant").write(response)
    st.session_state.messages.append(
        {"role": "assistant", "content": response})
