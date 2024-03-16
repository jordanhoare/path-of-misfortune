import streamlit as st

from app.models import Ascendancy


def ascendancy_card(ascendancy: Ascendancy) -> None:
    with st.container(border=True):
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(ascendancy.image_url)

        with col2:
            st.write(ascendancy.ascendancy)
