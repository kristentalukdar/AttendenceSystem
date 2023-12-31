import streamlit as st
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder

st.set_page_config(page_title='Attendence System', layout='wide')

st.header('Attendance System Using Face Recongnition')

with st.spinner("Loading Models and Connecting to Redis DB....."):
    import face_rec
st.success('Model Loaded Sucessfully')
st.success('Redis DB Connection Successfull')