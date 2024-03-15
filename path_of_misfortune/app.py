import random

import streamlit as st

from path_of_misfortune.models.ascendancy import Ascendancy
from path_of_misfortune.models.gems import SkillGem
from path_of_misfortune.ui import ascendancy_card, skill_card

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

excluded_tags = {"Aura", "Link", "Travel", "Herald", "Stance", "Guard", "Mark"}

filtered_skill_gems = [
    gem
    for gem in skill_gems
    if gem.name not in remove_names
    and not gem.alternative_quality
    and not gem.vaal
    and not set(gem.tags).intersection(excluded_tags)
]

skill_count = int(
    st.number_input("Number of skills", min_value=1, max_value=10, value=3)
)

if st.button("Roll"):
    ascendancy = random.choice(ascendancies)

    available_skill_count = min(skill_count, len(filtered_skill_gems))
    skills: list[SkillGem] = random.sample(filtered_skill_gems, available_skill_count)

    ascendancy_card(ascendancy)
    st.write("Skills:")
    for skill in skills:
        skill_card(skill)

    st.balloons()
else:
    st.write("Press the button to start!")
