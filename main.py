import streamlit as st

st.title('CHA₂DS₂-VASc Score Calculator')

st.write('Enter patient information below:')

age = st.slider('Age', 18, 100, 50)
gender = st.radio('Gender', ['Male', 'Female'])
chf = st.checkbox('Congestive Heart Failure')
hypertension = st.checkbox('Hypertension')
vasc_disease = st.checkbox('Vascular Disease')
diabetes = st.checkbox('Diabetes')
stroke_tia = st.checkbox('Stroke or TIA')
vascular_age = st.checkbox('Vascular Age ≥75 Years')

score = 0

if gender == 'Female':
    score += 1

if age >= 75:
    score += 2
elif age >= 65:
    score += 1

if chf:
    score += 1

if hypertension:
    score += 1

if vasc_disease:
    score += 1

if diabetes:
    score += 1

if stroke_tia:
    score += 2

if vascular_age:
    score += 1

st.write('The patient has a CHA₂DS₂-VASc score of:', score)
