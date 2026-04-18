import streamlit as st
import pandas as pd
import time

# --- CONFIGURATION & STYLING ---
st.set_page_config(page_title="ResilienceConnect", layout="wide")

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🛡️ ResilienceConnect")
menu = st.sidebar.radio("Navigation", ["Home", "Learning Modules", "Emergency Quiz", "Admin Dashboard"])

# --- 1. HOME PAGE ---
if menu == "Home":
    st.title("Disaster Preparedness & Response System")
    st.write("""
    India is prone to natural disasters like earthquakes and floods[cite: 12]. 
    This platform bridges the gap between policy and practice through digital education[cite: 19].
    """)
    st.image("https://via.placeholder.com/800x400.png?text=Safety+First", caption="Institutional Safety Initiative")

# --- 2. LEARNING MODULES (Region-Specific) ---
elif menu == "Learning Modules":
    st.header("📖 Knowledge Base")
    hazard = st.selectbox("Select a Hazard to Learn More:", ["Earthquake", "Flood", "Fire", "Cyclone"])
    
    content = {
        "Earthquake": "Drop, Cover, and Hold on. 58% of India is vulnerable[cite: 23].",
        "Flood": "Move to higher ground. Avoid walking or driving through floodwaters.",
        "Fire": "Crawl low under smoke and follow institutional evacuation routes[cite: 43].",
        "Cyclone": "Stay indoors and keep away from windows and glass doors."
    }
    st.info(content[hazard])

# --- 3. EMERGENCY QUIZ (Gamified Training) ---
elif menu == "Emergency Quiz":
    st.header("🎮 Gamified Training")
    st.write("Test your knowledge to increase institutional readiness[cite: 18].")
    
    q1 = st.radio("What is the safest action during an earthquake?", 
                  ["Run outside", "Drop, Cover, and Hold on", "Use the elevator"])
    
    if st.button("Submit Answer"):
        if q1 == "Drop, Cover, and Hold on":
            st.success("Correct! +10 Points to your profile.")
            st.balloons()
        else:
            st.error("Incorrect. Remember: Drop, Cover, and Hold on!")

# --- 4. ADMIN DASHBOARD (Analytics) ---
elif menu == "Admin Dashboard":
    st.header("📊 Institutional Preparedness Dashboard")
    st.write("Monitoring participation and awareness levels[cite: 17, 59].")
    
    # Simulating the data from the paper's results [cite: 84]
    data = {
        "Parameter": ["Awareness", "Response Knowledge", "Drill Participation"],
        "Before System (%)": [45, 40, 38],
        "After System (%)": [78, 75, 82]
    }
    df = pd.DataFrame(data)
    st.table(df)
    
    # Visualizing the improvement
    st.subheader("Progress Visualization")
    st.bar_chart(df.set_index("Parameter"))

# --- TRIGGER ALERT (Global Feature) ---
if st.sidebar.button("🚨 TRIGGER EMERGENCY ALERT"):
    st.toast("BROADCASTING: Simulated Fire Drill in Progress!", icon="🔥")
    time.sleep(1)
    st.warning("Please proceed to the nearest assembly point immediately.")