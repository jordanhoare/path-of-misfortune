import streamlit as st
from streamlit_extras.tags import tagger_component

from app.models import SkillGem


def skill_card(skill_gem: SkillGem) -> None:
    with st.container(border=True):
        col1, col2 = st.columns([1, 11])
        with col1:
            st.image(skill_gem.image_url, width=32)
        with col2:
            st.text(skill_gem.name)

        tagger_component("", [tag for tag in skill_gem.tags])  # noqa: C400,C416
