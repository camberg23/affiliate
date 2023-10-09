import streamlit as st
import requests
import openai
from langchain.chat_models import ChatOpenAI
from langchain import OpenAI, PromptTemplate, LLMChain
openai.api_key = st.secrets['OPENAI_API_KEY']


def recommend_books(personality_type):
    recommendations = {
        'INTJ': [
            ('Thinking, Fast and Slow by Daniel Kahneman', 'https://www.amazon.com/dp/B005Z9GAJG/?tag=affiliatet01f-20'),
            ('The Da Vinci Code by Dan Brown', 'https://www.amazon.com/dp/B0000D1BWY/?tag=affiliatet01f-20'),
            ('1984 by George Orwell', 'https://www.amazon.com/dp/B0BW4YL2WL/?tag=affiliatet01f-20')
        ],
        'INTP': [
            ('The Martian by Andy Weir', 'https://www.amazon.com/dp/B082BHWQCJ/?tag=affiliatet01f-20'),
            ('Flatland: A Romance of Many Dimensions by Edwin A. Abbott', 'https://www.amazon.com/dp/B007XFY0TM/?tag=affiliatet01f-20'),
            ('The Big Short by Michael Lewis', 'https://www.amazon.com/dp/B003CN7E42/?tag=affiliatet01f-20')
        ],
        'ENTJ': [
            ('The 7 Habits of Highly Effective People by Stephen R. Covey', 'https://www.amazon.com/dp/B086DD5KSJ/?tag=affiliatet01f-20'),
            ('The 48 Laws of Power by Robert Greene', 'https://www.amazon.com/dp/B00X0TKUS0/?tag=affiliatet01f-20'),
            ('The Lean Startup by Eric Ries', 'https://www.amazon.com/dp/B005MM7HY8/?tag=affiliatet01f-20')
        ],
        'ENTP': [
            ('The Tipping Point by Malcolm Gladwell', 'https://www.amazon.com/dp/B000OYD8T2/?tag=affiliatet01f-20'),
            ('Freakonomics by Steven D. Levitt & Stephen J. Dubner', 'https://www.amazon.com/dp/B01E60XNK8/?tag=affiliatet01f-20'),
            ('The Innovators by Walter Isaacson', 'https://www.amazon.com/dp/B00M9KICAY/?tag=affiliatet01f-20')
        ],
        'INFJ': [
            ('The Book Thief by Markus Zusak', 'https://www.amazon.com/dp/B000J20TZA/?tag=affiliatet01f-20'),
            ('The Alchemist by Paulo Coelho', 'https://www.amazon.com/dp/B000BO2D3C/?tag=affiliatet01f-20'),
            ('Man\'s Search for Meaning by Viktor E. Frankl', 'https://www.amazon.com/dp/B0006IU470/?tag=affiliatet01f-20')
        ],
        'INFP': [
            ('The Little Prince by Antoine de Saint-Exupéry', 'https://www.amazon.com/dp/B0023AP7T4/?tag=affiliatet01f-20'),
            ('The Fault in Our Stars by John Green', 'https://www.amazon.com/dp/B09VQ72PVG/?tag=affiliatet01f-20'),
            ('Pride and Prejudice by Jane Austen', 'https://www.amazon.com/dp/B0842RJBGG/?tag=affiliatet01f-20')
        ],
        'ENFJ': [
            ('The Power of Habit by Charles Duhigg', 'https://www.amazon.com/dp/B007EJSMC8/?tag=affiliatet01f-20'),
            ('How to Win Friends and Influence People by Dale Carnegie', 'https://www.amazon.com/dp/B0006IU7JK/?tag=affiliatet01f-20'),
            ('The Five Love Languages by Gary Chapman', 'https://www.amazon.com/dp/B079B7PJMV/?tag=affiliatet01f-20')
        ],
        'ENFP': [
            ('Eat, Pray, Love by Elizabeth Gilbert', 'https://www.amazon.com/dp/B000FDFY9O/?tag=affiliatet01f-20'),
            ('The Hitchhiker\'s Guide to the Galaxy by Douglas Adams', 'https://www.amazon.com/dp/B0009JKV9W/?tag=affiliatet01f-20'),
            ('Big Magic: Creative Living Beyond Fear by Elizabeth Gilbert', 'https://www.amazon.com/dp/B00U08ECQA/?tag=affiliatet01f-20')
        ],
        'ISTJ': [
            ('The Organized Mind by Daniel J. Levitin', 'https://www.amazon.com/dp/B00MH43RWK/?tag=affiliatet01f-20'),
            ('The Tipping Point by Malcolm Gladwell', 'https://www.amazon.com/dp/B000OYD8T2/?tag=affiliatet01f-20'),
            ('Unbroken by Laura Hillenbrand', 'https://www.amazon.com/dp/B004CJN7TG/?tag=affiliatet01f-20')
        ],
        'ISFJ': [
            ('The Help by Kathryn Stockett', 'https://www.amazon.com/dp/B001SIHRUY/?tag=affiliatet01f-20'),
            ('Where the Crawdads Sing by Delia Owens', 'https://www.amazon.com/dp/B07FSXPMHY/?tag=affiliatet01f-20'),
            ('The Guernsey Literary and Potato Peel Pie Society by Mary Ann Shaffer & Annie Barrows', 'https://www.amazon.com/dp/B001FVJIN8/?tag=affiliatet01f-20')
        ],
        'ESTJ': [
            ('Drive by Daniel H. Pink', 'https://www.amazon.com/dp/B0032COUMC/?tag=affiliatet01f-20'),
            ('The 7 Habits of Highly Effective People by Stephen R. Covey', 'https://www.amazon.com/dp/B086DD5KSJ/?tag=affiliatet01f-20'),
            ('The Subtle Art of Not Giving a F*ck by Mark Manson', 'https://www.amazon.com/dp/B01I29Y344/?tag=affiliatet01f-20')
        ],
        'ESFJ': [
            ('The Happiness Project by Gretchen Rubin', 'https://www.amazon.com/dp/B0032COUXQ/?tag=affiliatet01f-20'),
            ('Little Fires Everywhere by Celeste Ng', 'https://www.amazon.com/dp/B074F3BX79/?tag=affiliatet01f-20'),
            ('Daring Greatly by Brené Brown', 'https://www.amazon.com/dp/B07DX6TNR1/?tag=affiliatet01f-20')
        ],
        'ISTP': [
            ('Into the Wild by Jon Krakauer', 'https://www.amazon.com/dp/B000UW50NK/?tag=affiliatet01f-20'),
            ('Zen and the Art of Motorcycle Maintenance by Robert M. Pirsig', 'https://www.amazon.com/dp/60839872/?tag=affiliatet01f-20'),
            ('The Da Vinci Code by Dan Brown', 'https://www.amazon.com/dp/B0000D1BWY/?tag=affiliatet01f-20')
        ],
        'ISFP': [
            ('Eat, Pray, Love by Elizabeth Gilbert', 'https://www.amazon.com/dp/B000FDFY9O/?tag=affiliatet01f-20'),
            ('The Time Traveler\'s Wife by Audrey Niffenegger', 'https://www.amazon.com/dp/B093D99L1M/?tag=affiliatet01f-20'),
            ('The Catcher in the Rye by J.D. Salinger', 'https://www.amazon.com/dp/316769177/?tag=affiliatet01f-20')
        ],
        'ESTP': [
            ('The Wolf of Wall Street by Jordan Belfort', 'https://www.amazon.com/dp/B000WGUIX6/?tag=affiliatet01f-20'),
            ('Born to Run by Christopher McDougall', 'https://www.amazon.com/dp/B0028TY1D8/?tag=affiliatet01f-20'),
            ('The 4-Hour Workweek by Timothy Ferriss', 'https://www.amazon.com/dp/B0031KN6T8/?tag=affiliatet01f-20')
        ],
        'ESFP': [
            ('Me Before You by Jojo Moyes', 'https://www.amazon.com/dp/B00ANR0Y3S/?tag=affiliatet01f-20'),
            ('Bossypants by Tina Fey', 'https://www.amazon.com/dp/B004V6APR2/?tag=affiliatet01f-20'),
            ('The Rosie Project by Graeme Simsion', 'https://www.amazon.com/dp/B00DEKLXXQ/?tag=affiliatet01f-20')
        ]
    }
    return recommendations.get(personality_type, [])

# Template for GPT-3.5 Turbo to generate personalized recommendations
book_recommendation_template = """
Your job is to recommend books to users based on their MBTI personality type. The goal is to explain why each book would be specifically suited to the user's personality.

Given the personality type {personality_type}, here are the book titles and authors:
{book_titles}

Based on the above data, please provide a paragraph explaining to the user what these books are and why they might be particularly suited to their personality type. Try to 'hook' them.

FORMATTING REQUIREMENTS: 
-Make sure to mention each book title and author clearly, without any added punctuation or quotation marks.
-Split your discussion of each book into a separate TINY paragraph (ONLY 2 sentences roughly) to keep it clean
-Do not introduce all books before discussing each one. Just introduce them serially.
-Do not make assertions about what the user likes and doesn't like. Instead, make predictions (e.g., you might appreciate..., you probably value...)
-Begin with a simple introductory sentence to make it clear what you are about to discuss and why.
-THE ENTIRE OUTPUT SHOULD AMOUNT TO NO MORE THAN 7 TO 8 SENTENCES

Example correct output of a book title and author:
The Martian by Andy Weir

Bad examples:
"The Martian" by Andy Weir
The Martian
The Martian, a book by Andy Weir

Your mini-paragraphs with book recommendations directed to the user:
"""

def get_book_recommendation_paragraph(personality, recommended_books):
    # Formatting only the book titles for the prompt
    book_titles = "\n".join([book.split(" by ")[0] for book, _ in recommended_books])  # Extract only the book title

    # Feed the data into the GPT-3.5 Turbo model
    chat_model = ChatOpenAI(openai_api_key=openai.api_key, model_name='gpt-3.5-turbo', temperature=0.25)
    chat_chain = LLMChain(prompt=PromptTemplate.from_template(book_recommendation_template), llm=chat_model)
    recommendation_paragraph = chat_chain.run(personality_type=personality, book_titles=book_titles)

    # Search for book titles in the GPT output and replace them with markdown links
    for book, link in recommended_books:
        title_only = book.split(" by ")[0]  # Extract only the book title
        if title_only in recommendation_paragraph:
            recommendation_paragraph = recommendation_paragraph.replace(title_only, f"[{title_only}]({link})")

    return recommendation_paragraph

# Streamlit code
st.title('Personality-Based Book Recommendations')

# Add default option for personality type
options = ['Select your type', 'INTJ', 'INTP', 'ENTJ', 'ENTP', 'INFJ', 'INFP', 'ENFJ', 'ENFP', 'ISTJ', 'ISFJ', 'ESTJ', 'ESFJ', 'ISTP', 'ISFP', 'ESTP', 'ESFP']
personality = st.selectbox('Select your personality type:', options)

# Display the "Submit" button only if the user has selected a valid personality type
if personality != 'Select your type':
    if st.button('Submit'):
        recommended_books = recommend_books(personality)

        if recommended_books:
            recommendation_paragraph = get_book_recommendation_paragraph(personality, recommended_books)
            st.markdown(f'### Here are some personalized book recs we think you might love as an {personality}:')
            st.markdown(recommendation_paragraph)
        else:
            st.write("Sorry, no recommendations available for your type.")
else:
    st.write("Please select a personality type to get book recommendations.")
