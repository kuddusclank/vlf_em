
import streamlit as st
import pages.data as md;

st.set_page_config(
    page_title="GeoGenix Digital Datasheet",
    page_icon="👋",
    initial_sidebar_state="collapsed"
)

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

st.write("# Welcome To GeoGenix ! 👋")
st.write("  ### Very Low Frequency Electromagnetic Survey Digital Datasheet")

st.markdown(
    """
   Welcome to Geogenix, your go-to resource for geophysical exploration and insights. 
   Our mission is to bridge the gap between theory and practice, providing geoscientists, 
   researchers, and enthusiasts with valuable information and tools. 
    ### Want to more tools?
    - Check out [GeoGenix HomePage](https://geogenix.000webhostapp.com/)
  
"""
)
def switching():
    st.balloons()

st.subheader("VLF-EM Survey↭")
SurveyName = st.text_input("Interval Name")
Longitude = st.number_input(label= "Logitude ", placeholder="Degree Decimal",min_value=0.00)
Lattitude=st.number_input("Lattitude", placeholder="Degree Decimal",min_value=0.00)
Elevation=st.number_input("Elevation", placeholder="Metres",min_value=0.00)
Interval_Spacing=st.number_input("Spacing Interval",min_value=0)
if(st.button("Proceed",type='primary')):
    md.SurveyName=SurveyName
    md.Longitude=Longitude
    md.Lattitude=Lattitude
    md.Intervals=Interval_Spacing
    md.Elevation=Elevation
    md.dataset={"Station":[],"Inphase":[],"Outphase":[],"Longitude":[],"Lattitude":[],"Elevation":[]}
    md.Station=0
    md.config()
    st.switch_page("pages/input_data.py")

    





