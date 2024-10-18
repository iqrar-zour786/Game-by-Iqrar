import streamlit as st
import random

# Title of the app
st.title("🎲 Guess the Number Game")

# Description
st.write("Try to guess the randomly generated number between 1 and 100!")

# Sidebar for range selection (optional feature)
lower_limit = st.sidebar.slider("Select Lower Limit", 1, 50, 1)
upper_limit = st.sidebar.slider("Select Upper Limit", 51, 100, 100)

# Initialize or reset game state using session state
if "number" not in st.session_state:
    st.session_state.number = random.randint(lower_limit, upper_limit)
    st.session_state.attempts = 0

# Input for user's guess
user_guess = st.number_input(
    f"Enter your guess between {lower_limit} and {upper_limit}",
    min_value=lower_limit,
    max_value=upper_limit,
    step=1,
)

# Button to submit guess
if st.button("Guess"):
    st.session_state.attempts += 1
    if user_guess < st.session_state.number:
        st.warning("Too low! Try again.")
    elif user_guess > st.session_state.number:
        st.warning("Too high! Try again.")
    else:
        st.success(f"🎉 Congratulations! You guessed it in {st.session_state.attempts} attempts.")
        # Reset game state
        if st.button("Play Again"):
            st.session_state.number = random.randint(lower_limit, upper_limit)
            st.session_state.attempts = 0

# Display number of attempts so far
st.write(f"Attempts: {st.session_state.attempts}")
