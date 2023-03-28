import streamlit as st

sito = st.text_input('Inserisci il nome del sito del quale vuoi avere informazioni (es. jesap.it)')

completo = "https\/\/:" + sito
if sito:
    st.write(completo)