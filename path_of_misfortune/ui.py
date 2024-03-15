import streamlit as st
from streamlit_extras.tags import tagger_component  # type: ignore

from path_of_misfortune.models.ascendancy import Ascendancy
from path_of_misfortune.models.gems import SkillGem


def skill_card(skill_gem: SkillGem) -> None:
    with st.container(border=True):
        col1, col2 = st.columns([1, 11])
        with col1:
            st.image(skill_gem.image_url, width=32)
        with col2:
            st.text(skill_gem.name)

        tagger_component("", [tag for tag in skill_gem.tags])  # noqa: C400,C416


def ascendancy_card(ascendancy: Ascendancy) -> None:
    with st.container(border=True):
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(ascendancy.image_url)

        with col2:
            st.write(ascendancy.ascendancy)
