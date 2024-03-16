import random

import streamlit as st

from app.models import Ascendancy, SkillGem
from app.ui import ascendancy_card, skill_card

if "skill_count" not in st.session_state:
    st.session_state["skill_count"] = 3


ascendancies = Ascendancy.from_json()
skill_gems = SkillGem.from_json()


st.title("Path of Misfortune")

remove_names = {
    "Portal",
    "Detonate Mines",
    "Flesh Offering",
    "Bone Offering",
    "Spirit Offering",
    "Brand Recall",
    "Snipe",
    "Berserk",
    "Arctic Armour",
}

excluded_tags = {
    "Aura",
    "Link",
    "Travel",
    "Herald",
    "Stance",
    "Guard",
    "Mark",
}  # TODO: curses

filtered_skill_gems = [
    gem
    for gem in skill_gems
    if gem.name not in remove_names
    and not gem.alternative_quality
    and not gem.vaal
    and not set(gem.tags).intersection(excluded_tags)
]


if st.button("Roll"):
    ascendancy = random.choice(ascendancies)

    available_skill_count = min(st.session_state.skill_count, len(filtered_skill_gems))
    skills: list[SkillGem] = random.sample(filtered_skill_gems, available_skill_count)

    ascendancy_card(ascendancy)
    st.write("Skills:")
    for skill in skills:
        skill_card(skill)

    st.balloons()
else:
    st.write("Press the button to start!")
