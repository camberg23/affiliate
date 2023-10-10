import streamlit as st
import pandas as pd

# Load the recommendation paragraphs CSV
df_recommendations = pd.read_csv('recommendation_paragraphs.csv')

# Streamlit code
st.title('Personality-Based Book Recommendations')

# Add default option for personality type
options = ['Select your type', 'INTJ', 'INTP', 'ENTJ', 'ENTP', 'INFJ', 'INFP', 'ENFJ', 'ENFP', 'ISTJ', 'ISFJ', 'ESTJ', 'ESFJ', 'ISTP', 'ISFP', 'ESTP', 'ESFP']
personality = st.selectbox('Select your personality type:', options)

# Display the "Submit" button only if the user has selected a valid personality type
if personality != 'Select your type':
    if st.button('Submit'):
        # Retrieve the recommendation paragraph for the selected personality type
        recommendation_paragraph = df_recommendations[df_recommendations['personality_type'] == personality]['recommendation_paragraph'].values[0]
        
        if recommendation_paragraph:
            st.markdown(f'### Here are some personalized book recs we think you might love as an {personality}:')
            st.markdown(recommendation_paragraph)
        else:
            st.write("Sorry, no recommendations available for your type.")
else:
    st.write("Please select a personality type to get book recommendations.")
