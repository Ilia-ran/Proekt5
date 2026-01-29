import streamlit as st

st.title("Упражнения със Streamlit")

st.header("Упражнение 1")
answer = st.text_input("Обичаш ли Python? (да / не)")

if answer.lower() == "да":
    st.write("Супер!")
elif answer.lower() == "не":
    st.write("Ще го харесаш!")
  
st.header("Упражнение 2")
number = st.number_input("Въведи число", step=1)

if number > 10:
    st.write("Голямо число")
else:
    st.write("Малко число")

st.header("Упражнение 3 - Мини тест")
user_answer = st.number_input("Колко е 5 × 5?", step=1)

if st.button("Провери"):
    if user_answer == 25:
        st.success("Вярно!")
    else:
        st.error("Грешно!")
