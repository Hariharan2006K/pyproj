import streamlit as st

def get_questions():
    return [
        {
            "q": "What is the very first thing you should do during an earthquake?",
            "options": ["Run outside immediately", "Drop, Cover, and Hold On", "Stand in a doorway", "Call emergency services"],
            "answer": "Drop, Cover, and Hold On"
        },
        {
            "q": "True or False: It is safe to use an elevator to evacuate during a fire.",
            "options": ["True", "False"],
            "answer": "False"
        },
        {
            "q": "How much moving water does it take to knock an adult down during a flood?",
            "options": ["6 inches", "12 inches", "2 feet", "3 feet"],
            "answer": "6 inches"
        },
        {
            "q": "What is the safest place to take shelter during a cyclone or hurricane?",
            "options": ["The top floor of a building", "An interior, windowless room on the lowest floor", "Inside a car", "Next to a strong window"],
            "answer": "An interior, windowless room on the lowest floor"
        },
        {
            "q": "During a severe heatwave, what is the best thing to drink to stay hydrated?",
            "options": ["Caffeinated energy drinks", "Sugary sodas", "Ice-cold fruit juice", "Water"],
            "answer": "Water"
        },
        {
            "q": "If your clothing accidentally catches on fire, what is the correct action to take?",
            "options": ["Run as fast as you can to find water", "Wave a jacket over the fire", "Stop, Drop, and Roll", "Call for help and wait"],
            "answer": "Stop, Drop, and Roll"
        },
        {
            "q": "What is the most effective way to escape a heavily smoke-filled hallway?",
            "options": ["Run quickly while covering your face", "Crawl low to the ground where the air is cleaner", "Walk slowly backwards", "Wait for the smoke to clear"],
            "answer": "Crawl low to the ground where the air is cleaner"
        },
        {
            "q": "If you are playing near the beach and feel a long, strong earthquake, what should you do immediately?",
            "options": ["Wait for a tsunami siren", "Move to higher ground immediately", "Hide under a sturdy beach chair", "Go into the water to avoid falling objects"],
            "answer": "Move to higher ground immediately"
        },
        {
            "q": "Why is it important to stay strictly indoors during a nearby volcanic eruption?",
            "options": ["To avoid falling lava bombs", "Because volcanic ash is highly dangerous to breathe", "To keep out of the extreme heat", "To protect yourself from loud noises"],
            "answer": "Because volcanic ash is highly dangerous to breathe"
        },
        {
            "q": "True or False: Driving an SUV through standing floodwaters is safe if the water isn't moving fast.",
            "options": ["True", "False"],
            "answer": "False"
        },
        {
            "q": "What is the primary purpose of maintaining a 'defensible space' around a school campus?",
            "options": ["To give athletes more space", "To slow the spread of a wildfire to the buildings", "To protect against floods", "To stop tornados"],
            "answer": "To slow the spread of a wildfire to the buildings"
        },
        {
            "q": "During an earthquake, why is it critical that heavy furniture is bolted to the walls in classrooms?",
            "options": ["To stop students from moving it", "To prevent it from tipping over and injuring someone", "To make cleaning easier", "To strengthen the structural integrity of the walls"],
            "answer": "To prevent it from tipping over and injuring someone"
        },
        {
            "q": "Why should you keep far away from windows during a severe storm or cyclone?",
            "options": ["Because lightning might strike the window", "Because the glass can shatter from high winds or flying debris", "Because it will be cold near the glass", "Because the rain will leak through"],
            "answer": "Because the glass can shatter from high winds or flying debris"
        },
        {
            "q": "True or False: During a school fire drill, you should leave your backpack and belongings behind.",
            "options": ["True", "False"],
            "answer": "True"
        },
        {
            "q": "What should you do if you are caught outdoors on a field during a severe thunderstorm?",
            "options": ["Hide under the tallest tree you can find", "Lay flat on the ground", "Seek shelter inside a sturdy building immediately", "Stand in a group to stay warm"],
            "answer": "Seek shelter inside a sturdy building immediately"
        },
        {
            "q": "How long should your emergency supply kit be prepared to last during a major disaster?",
            "options": ["12 hours", "24 hours", "At least 72 hours", "1 week"],
            "answer": "At least 72 hours"
        },
        {
            "q": "What does the 'Urban Heat Island' effect refer to?",
            "options": ["Islands in the ocean getting warmer", "Cities experiencing much hotter temperatures than surrounding rural areas due to concrete and human activity", "The overheating of a single classroom", "A new type of solar panel"],
            "answer": "Cities experiencing much hotter temperatures than surrounding rural areas due to concrete and human activity"
        },
        {
            "q": "True or False: During a heatwave, outdoor sports activities should be scheduled for the middle of the day to get them over with.",
            "options": ["True", "False"],
            "answer": "False"
        },
        {
            "q": "If an official evacuation order is issued due to an approaching cyclone, what is the best response?",
            "options": ["Wait to see if the weather actually gets bad", "Evacuate immediately using clearly marked safety routes", "Hide in the basement and wait", "Call the police to confirm"],
            "answer": "Evacuate immediately using clearly marked safety routes"
        },
        {
            "q": "Why is it extremely dangerous to touch downed power lines after a storm?",
            "options": ["They are dirty and full of germs", "They might electrocute you because they can still have a live current", "They belong to the electric company", "They will burn your skin from the heat of the storm"],
            "answer": "They might electrocute you because they can still have a live current"
        }
    ]

def render():
    st.title("Safety Quiz 📝")
    st.write("Test your comprehensive knowledge with this 20-question safety exam.")
    
    questions = get_questions()
    
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'quiz_submitted' not in st.session_state:
        st.session_state.quiz_submitted = False

    if not st.session_state.quiz_submitted:
        with st.form("quiz_form"):
            user_answers = []
            for i, q in enumerate(questions):
                st.markdown(f"**{i+1}. {q['q']}**")
                ans = st.radio(f"Select option for question {i+1}", q['options'], key=f"q_{i}", index=None, label_visibility="collapsed")
                user_answers.append(ans)
                st.markdown("---")
            
            submitted = st.form_submit_button("Submit Exam", type="primary")
            
            if submitted:
                if None in user_answers:
                    st.error("Please answer all 20 questions before submitting.")
                else:
                    score = 0
                    for i, ans in enumerate(user_answers):
                        if ans == questions[i]['answer']:
                            score += 1
                    
                    st.session_state.score = score
                    st.session_state.quiz_submitted = True
                    st.rerun()
    else:
        st.success(f"Exam Completed! Your final score: {st.session_state.score} / 20")
        
        # Display feedback based on score
        if st.session_state.score == 20:
            st.balloons()
            st.write("### Perfect Score!")
            st.write("Excellent job. You have mastered the disaster preparedness material.")
        elif st.session_state.score >= 15:
            st.write("### Great work!")
            st.write("You have a strong understanding of safety protocols.")
        elif st.session_state.score >= 10:
            st.write("### Good effort.")
            st.write("Review the Hazard Learning page to brush up on a few concepts.")
        else:
            st.write("### Keep studying!")
            st.write("We recommend reviewing the learning modules thoroughly to improve your safety knowledge.")
            
        st.write("---")
        if st.button("Retake Exam"):
            st.session_state.quiz_submitted = False
            st.session_state.score = 0
            st.rerun()
            
        st.info("Research shows that taking interactive exams like this one improves safety drill participation from 38% to 82%.")
