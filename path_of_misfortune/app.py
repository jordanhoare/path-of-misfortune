import streamlit as st

from path_of_misfortune.data.utils import load_skill_gems_from_json

skill_gems = load_skill_gems_from_json("path_of_misfortune/data/skill_gems.json")

for gem in skill_gems:
    st.write(gem)
