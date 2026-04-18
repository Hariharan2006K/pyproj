import streamlit as st

def render():
    st.title("Learn About Hazards 📚")
    st.write("Browse the tabs below to learn essential safety guidelines for different natural disasters.")
    
    tabs = st.tabs(["Earthquakes", "Tsunamis", "Volcanoes", "Fires", "Cyclones"])
    
    with tabs[0]:
        st.header("Earthquakes")
        st.write("""
        **What to do:**
        - **Drop to the floor.**
        - **Cover your head and neck** under a sturdy desk or table.
        - **Hold on tight** until the shaking stops.
        
        *School safety note:* It is critical to bolt down tall bookshelves and cabinets to prevent them from tipping over during a seismic event.
        """)
        
    with tabs[1]:
        st.header("Tsunamis")
        st.write("""
        **What to do:**
        - If you feel a strong earthquake near the coast, **evacuate to high ground immediately.**
        - Do not stop to gather belongings. 
        - Stay away from the shore until official authorities declare it is safe.
        
        *School safety note:* Coastal schools must have predefined evacuation routes leading to elevated areas or structurally reinforced upper floors.
        """)
        
    with tabs[2]:
        st.header("Volcanoes")
        st.write("""
        **What to do:**
        - **Stay indoors.** Volcanic ash is highly hazardous to the respiratory system.
        - Close all windows, doors, and ventilation systems to keep ash out.
        - Only evacuate if officially instructed to do so by authorities.
        
        *School safety note:* Emergency supply kits should include N95 masks for staff and students in high-risk zones.
        """)

    with tabs[3]:
        st.header("Fires")
        st.write("""
        **What to do:**
        - **Evacuate immediately.** Leave all personal belongings behind.
        - If there is heavy smoke, **crawl low on the floor** where the air is safer to breathe.
        - If clothes catch fire: **Stop, Drop, and Roll.**
        
        *School safety note:* Ensure the designated evacuation assembly point is far enough from the building to avoid secondary hazards.
        """)
        
    with tabs[4]:
        st.header("Cyclones & Storms")
        st.write("""
        **What to do:**
        - Stay far away from windows and glass doors, which can shatter from high winds.
        - Take shelter in an interior hallway or a room without windows on the lowest floor.
        - Bring loose outdoor objects inside before the storm arrives.
        
        *School safety note:* Campuses should identify and clearly mark designated severe weather shelter areas.
        """)
