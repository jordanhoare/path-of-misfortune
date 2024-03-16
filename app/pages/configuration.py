import streamlit as st


def update_skill_count() -> None:
    st.session_state.skill_count = st.session_state["skill_count_input"]


skill_count = st.number_input(
    "Number of skills",
    min_value=1,
    max_value=10,
    value=st.session_state.skill_count,
    key="skill_count_input",
    on_change=update_skill_count,
)
