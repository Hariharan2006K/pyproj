import streamlit as st
import pandas as pd

def render():
    st.title("Project Dashboard 📊")
    st.write("Visualizing the impact of our safety education program based on the research data.")
    
    data = {
        'Metric': ['Drill Participation', 'Hazard Knowledge Score', 'Evacuation Speed', 'Quiz Engagement'],
        'Before the project (%)': [38, 45, 40, 50],
        'After the project (%)': [82, 78, 85, 88]
    }
    
    df = pd.DataFrame(data)
    
    st.write("### Research Results Summary")
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.write("---")
    st.write("### Performance Improvement")
    st.write("The bar chart represents the measurable improvements across the institutional metrics.")
    
    chart_data = df.set_index('Metric')
    try:
        st.bar_chart(chart_data)
    except TypeError:
        st.bar_chart(chart_data)
        
    st.write("---")
    st.write("### Key Project Metrics")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Drill Participation", value="82%", delta="44% Increase")
    with col2:
        st.metric(label="Hazard Knowledge", value="78%", delta="33% Increase")
    with col3:
        st.metric(label="Quiz Engagement", value="88%", delta="38% Increase")
