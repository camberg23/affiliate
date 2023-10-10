import streamlit as st
import pandas as pd

# Load the recommendation paragraphs CSV
df_recommendations = pd.read_csv('recommendation_paragraphs.csv')

# Streamlit code
st.title('Personality-Based Book Recommendations')

# Create two columns for the dropdown and the button
col1, col2 = st.columns([3, 1])

# Add the dropdown to the first column
options = ['Select your type', 'INTJ', 'INTP', 'ENTJ', 'ENTP', 'INFJ', 'INFP', 'ENFJ', 'ENFP', 'ISTJ', 'ISFJ', 'ESTJ', 'ESFJ', 'ISTP', 'ISFP', 'ESTP', 'ESFP']
personality = col1.selectbox('Select your personality type:', options)

# Display the "Recommend" button in the second column
if col2.button('Recommend'):
    # Retrieve the recommendation paragraph for the selected personality type
    recommendation_paragraph = df_recommendations[df_recommendations['personality_type'] == personality]['recommendation_paragraph'].values[0]
    
    if recommendation_paragraph:
        st.markdown(f'### Here are some personalized book recs we think you might love as an {personality}:')
        st.markdown(recommendation_paragraph)
    else:
        st.write("Sorry, no recommendations available for your type.")
elif personality == 'Select your type':
    st.write("Please select a personality type to get book recommendations.")
