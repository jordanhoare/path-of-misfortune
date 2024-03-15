import random

import streamlit as st

from path_of_misfortune.models.ascendancy import Ascendancy
from path_of_misfortune.models.gems import SkillGem
from path_of_misfortune.ui import ascendancy_card, skill_card

ascendancies = Ascendancy.from_json()
skill_gems = SkillGem.from_json()

st.title("Path of Misfortune")

if st.button("Roll"):
    ascendancy = random.choice(ascendancies)
    skills: list[SkillGem] = random.sample(skill_gems, 3)

    ascendancy_card(ascendancy)
    st.write("Skills:")
    for skill in skills:
        skill_card(skill)

    st.balloons()


else:
    st.write("Press the button to start!")
