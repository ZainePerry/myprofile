# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 12:17:29 2025

@author: PRRZAI001
"""

import streamlit as st
import pandas as pd

# Title of the app
st.title("Zaine Perry Profile Page")

col1, col2 = st.columns(2)

# Collect basic information
with col1:
    name = "Zaine Perry"
    field = "Ocean & Atmosphere Science"
    institution = "University of Cape Town (UCT)"
    department = "Oceanography"
    level = "Masters Student"
    supervisor = "Dr Ramontsheng Rapolaki, Dr Sarah Roffe and Dr Moagabo Ragoasha"
    supervisor = "Dr Moagabo Ragoasha (UCT), Dr Ramontsheng Rapolaki (UFS, ARC, SAWS), Dr Sarah Roffe (UFS, ARC)"
    # supervisor = (
    # "Dr Moagabo Ragoasha <sup>(UCT)</sup>, "
    # "Dr Ramontsheng Rapolaki <sup>(UFS, ARC, SAWS)</sup>, "
    # "Dr Sarah Roffe <sup>(UFS, ARC)</sup>"
    # )

# Display basic profile information
    st.header("Researcher Overview")
    st.write(f"**Name:** {name}")
    st.write(f"**Level:** {level}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")
    st.write(f"**Department:** {department}")
    st.write(f"**Supervisors:** {supervisor}")

# enable = st.checkbox("Enable camera")
# picture = st.camera_input("Take a picture", disabled=not enable)

# if picture:
#     st.image(picture)
# st.image("C:\Users\PRRZAI001\Downloads\zaine.jpg", caption="Profile Picture", use_column_width=True)

# st.header("Profile Picture")
# uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# if uploaded_image is not None:
#     st.image(uploaded_image, caption="Profile Picture", use_column_width=True)
with col2:
     st.image("zaine.jpg", caption="Zaine Perry", use_container_width=1)

st.header("Thesis title:")
st.write("An analysis of tropical Cyclone Freddy's evolution and associated rainfall over south-eastern Africa using the WRF-CROCO coupled model simulation"
)
st.header("About")
st.write("My master's thesis looks at a coupled modelling approach using WRF-CROCO in simulating Tropical Cyclone Freddy over southern Africa. My thesis hopes to improve the understanding and enhance model accuracy in these fragile beasts that have both a strong atmospheric and oceanic component in the system."
)

# Abstract section
st.header("Abstract")
abstract_text = (
    "During February–March 2023, the record-breaking tropical cyclone (TC) Freddy caused widespread flooding and damages across southeastern "
    "Africa. While <5 % of TCs make landfall into southern Africa, TC Freddy made landfall twice and is the only TC in the past two decades that has "
    "tracked over 8000 km across the entire southern Indian Ocean. To understand why TC Freddy was so unique, this study investigated the evolution, "
    "track and atmospheric-oceanic mechanisms driving TC Freddy using the ERA5, CFSv2, OSTIA, NCEP-NCAR datasets and track data from "
    "various sources. It was found that SSTs were >27°C during TC Freddy’s lifetime, while TC Dingani and a split Mascarene High played a role in "
    "steering TC Freddy across the southern Indian Ocean. Leading up to the development of TC Freddy, conditions were favourable for TC genesis, as "
    "indicated by the levels of the Genesis Potential Parameter (GPP) and its modified version (GPPI), the tropical cyclone heat potential levels, and "
    "elevated SSTs. Ridging subtropical anticyclones and the Mascarene High alongside favourable steering flow and GPP (and GPPI) conditions "
    "resulted in Freddy’s double landfall in Mozambique. In assessing the tracks, it was found that there are discrepancies in the track of the commonly "
    "used IBTrACS when compared to ERA5 and RSMC tracks, which has implications for impact studies due to the underestimation of landfall "
    "considerations. This study reveals the unique characteristics and atmospheric-oceanic mechanisms driving TC Freddy, emphasising the importance "
    "of accurate representation of favourable conditions and track data for enhancing TC forecasting and impact assessments."
)

# Abstract section


st.write(abstract_text)
# st.header("Symposium abstract")

st.header("Publication(s)")
st.write("https://doi.org/10.1016/j.tcrr.2024.11.008")


# Add a contact section
st.header("Contact Information")
email = "PRRZAI001@myuct.ac.za"
st.write(f"You can reach {name} at {email}")
info = "https://science.uct.ac.za/department-oceanography"
st.write(f"**For more information on the department:** {info}")

