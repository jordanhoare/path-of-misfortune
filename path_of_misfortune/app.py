import streamlit as st

from path_of_misfortune.models.gems import SkillGem

skill_gems = SkillGem.from_json()

for gem in skill_gems:
    st.write(gem)
