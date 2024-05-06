import streamlit as st
from pages.data import *
import pandas as pd


st.set_page_config(
    page_title="GeoGenix",
    page_icon="🌍",
    initial_sidebar_state="collapsed"
)


def insertNew(Inphase,Outphase,Longitude,Lattitude,Elevation):

    md.dataset["Inphase"]+=[Inphase]
    md.dataset["Outphase"]+=[Outphase]
    md.dataset["Longitude"]+=[Longitude]
    md.dataset["Lattitude"]+=[Lattitude]
    md.dataset["Elevation"]+=[Elevation]
    md.DATA= dataset
    st.write(DATA)
    df = pd.DataFrame(md.dataset)
    st.write(df)


st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)
st.write("# 🌍 GeoGenix")
st.write("## Profile Metadata")
st.write("Name: ",SurveyName)
st.write("Longitude: ",Longitude,"    Lattitude: ",Lattitude,"Elevation :",Elevation)


st.divider()


inphase = st.number_input("Inphase Value",key='inphase')
outphase = st.number_input("Outphase Value",key='outphase')
longitude = st.number_input("Longitude",key='longitude')
lattitude = st.number_input("Lattitude",key='lattitude')
elevation = st.number_input("Elevation",key='elevation')
def clear_all_text_inputs():
    add_data(inphase,outphase,longitude,lattitude,elevation)
    #st.write(dataset)
    st.session_state['inphase'] = None  # Clear inphase text input
    # Clear other text input elements:
    st.session_state['outphase'] = None  # Clear outphase number input
    st.session_state['longitude'] = None  # Clear longitude number input
    st.session_state['lattitude'] = None  # Clear latitude number input
    st.session_state['elevation'] = None  # Clear elevation number input

st.markdown("""
            <style>
                div[data-testid="column"] {
                    width: fit-content !important;
                    flex: unset;
                }
                div[data-testid="column"] * {
                    width: fit-content !important;
                }
            </style>
            """, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    insert_button = st.button("Add Dataset", type='primary', key='insert_button', on_click=clear_all_text_inputs)
with col2:
    if (st.button("Datasheet View")):
        st.switch_page("pages/export_data.py")


