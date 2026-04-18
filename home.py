import streamlit as st

def render():
    st.title("Disaster Preparedness Project 🌍")
    
    st.markdown("""
    ### Welcome to our project!
    This is the **Disaster Preparedness and Response Education System (DPRES)**. I built this for my end-semester project to explore the most effective ways to teach students about natural disasters.
    
    Standard safety drills can sometimes have low engagement. So, for this project, I incorporated a **gamified learning system**. Research shows that introducing interactive elements boosts drill participation tremendously—from just 38% to 82%.
    
    ### Project Modules
    *   **Learn Hazards 📚:** Read our concise guides on what to do during Earthquakes, Floods, Tsunamis, and Volcanoes.
    *   **Safety Quiz 📝:** A comprehensive 20-question test to evaluate hazard knowledge.
    *   **Project Dashboard 📊:** Data visualizations showcasing our findings on student learning improvements.
    *   **Alert Demo 🚨:** A simulated emergency broadcast button located in the sidebar.
    """)
    st.image("https://images.unsplash.com/photo-1549421272-9ccdf14db1c6?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80", caption="Preparedness saves lives.")
