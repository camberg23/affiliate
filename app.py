import streamlit as st

def recommend_books(personality_type):
    recommendations = {
        'TypeA': [('Book Title 1', 'your_affiliate_link1'), ('Book Title 2', 'your_affiliate_link2')],
        'TypeB': [('Book Title 3', 'your_affiliate_link3'), ('Book Title 4', 'your_affiliate_link4')]
    }
    return recommendations.get(personality_type, [])

st.title('Personality-Based Book Recommender')
personality = st.selectbox('Select your personality type:', ['TypeA', 'TypeB', 'TypeC'])
recommended_books = recommend_books(personality)

if recommended_books:
    st.write('Recommended books for you:')
    for book, link in recommended_books:
        st.write(f"[{book}]({link})")
else:
    st.write("Sorry, no recommendations available for your type.")
