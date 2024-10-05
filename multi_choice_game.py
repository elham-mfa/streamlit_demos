import streamlit as st
import json
from arabic_support import support_arabic_text


def run():
    st.set_page_config(
        page_title="Arabic Game",
        page_icon="❓",
    )

if __name__ == "__main__":
    run()

# Support Arabic text alignment in all components
support_arabic_text(all=True)


# Custom CSS for the buttons
st.markdown("""
<style>
div.stButton > button:first-child {
    display: block;
    margin: 0 auto;
body, html {
    direction: RTL;
    unicode-bidi: bidi-override;
    text-align: right;
}
p, div, input, label, h1, h2, h3, h4, h5, h6 {
    direction: RTL;
    unicode-bidi: bidi-override;
    text-align: right;
}
</style>
""", unsafe_allow_html=True)

# Initialize session variables if they do not exist
default_values = {'current_index': 0, 'current_question': 0, 'score': 0, 'selected_option': None, 'answer_submitted': False}
for key, value in default_values.items():
    st.session_state.setdefault(key, value)

# Load quiz data
with open('content/quiz_data.json', 'r', encoding='utf-8') as f:
    quiz_data = json.load(f)

def restart_quiz():
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.selected_option = None
    st.session_state.answer_submitted = False

def submit_answer():

    # Check if an option has been selected
    if st.session_state.selected_option is not None:
        # Mark the answer as submitted
        st.session_state.answer_submitted = True
        # Check if the selected option is correct
        if st.session_state.selected_option == quiz_data[st.session_state.current_index]['answer']:
            st.session_state.score += 10
    else:
        # If no option selected, show a message and do not mark as submitted
        st.warning("Please select an option before submitting.")

def next_question():
    st.session_state.current_index += 1
    st.session_state.selected_option = None
    st.session_state.answer_submitted = False

# Title and description
st.title("لعبة أقسام الكلام")

# Progress bar
progress_bar_value = (st.session_state.current_index + 1) / len(quiz_data)
st.metric(label="النتيجة", value=f"{st.session_state.score} / {len(quiz_data) * 10}")
st.progress(progress_bar_value)

# Display the question and answer options
question_item = quiz_data[st.session_state.current_index]
st.subheader(f"السؤال {st.session_state.current_index + 1}")
st.title(f"{question_item['sentence']} \n ما هو نوع قسم الكلام في كلمة **{question_item['word']}**")

st.markdown(""" ___""")

# Answer selection
options = question_item['options']
correct_answer = question_item['answer']

if st.session_state.answer_submitted:
    for i, option in enumerate(options):
        label = option
        if option == correct_answer:
            st.success(f"{label} (Correct answer)")
        elif option == st.session_state.selected_option:
            st.error(f"{label} (Incorrect answer)")
        else:
            st.write(label)
else:
    for i, option in enumerate(options):
        if st.button(option, key=i, use_container_width=True):
            st.session_state.selected_option = option

st.markdown(""" ___""")

# Submission button and response logic
if st.session_state.answer_submitted:
    if st.session_state.current_index < len(quiz_data) - 1:
        st.button('التالي', on_click=next_question)
    else:
        st.write(f"Quiz completed! Your score is: {st.session_state.score} / {len(quiz_data) * 10}")
        if st.button('إعادة', on_click=restart_quiz):
            pass
else:
    if st.session_state.current_index < len(quiz_data):
        st.button('أَجِب', on_click=submit_answer)
