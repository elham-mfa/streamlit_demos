import streamlit as st

def game_page():
    st.title("Multiple Choice Quiz")

    questions = [
        "What is the capital of France?",
        "Who painted the Mona Lisa?",
        "What is the largest planet in our solar system?",
        "In what year did World War II end?",
        "What is the chemical symbol for gold?",
        "Who wrote the play Romeo and Juliet?",
        "What is the square root of 144?",
        "Which gas is essential for human life?",
        "What is the name of the longest river in the world?",
        "How many sides does a hexagon have?"
    ]

    answers = [
        "Paris",
        "Leonardo da Vinci",
        "Jupiter",
        "1945",
        "Au",
        "William Shakespeare",
        "12",
        "Oxygen",
        "Nile River",
        "6"
    ]

    options = [
        ["Paris", "London", "Berlin"],
        ["Leonardo da Vinci", "Michelangelo", "Raphael"],
        ["Jupiter", "Saturn", "Mars"],
        ["1945", "1939", "1942"],
        ["Au", "Ag", "Fe"],
        ["William Shakespeare", "Charles Dickens", "Jane Austen"],
        ["12", "13", "14"],
        ["Oxygen", "Carbon Dioxide", "Nitrogen"],
        ["Nile River", "Amazon River", "Yangtze River"],
        ["6", "7", "8"]
    ]

    score = 0
    for i in range(len(questions)):
        st.header(f"Question {i+1}: {questions[i]}")
        col1, col2, col3 = st.columns(3)
        option1 = col1.radio("", options[i][0])
        option2 = col2.radio("", options[i][1])
        option3 = col3.radio("", options[i][2])
        if option1 == answers[i]:
            score += 1
            st.success("Correct!")
        else:
            st.error(f"Incorrect. The correct answer is {answers[i]}")

    st.header(f"Your final score is {score}/{len(questions)}")

if __name__ == "__main__":
    game_page()
