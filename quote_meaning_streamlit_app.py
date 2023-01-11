import streamlit as st
import numpy as np
from PIL import Image
from quote import image_to_text,quote_meaning,generte_quote_meaning_image


st.set_page_config(
    
     layout="wide",
    #  initial_sidebar_state="expanded", 
 )
st.title(body='Quote to meaning AI !')

uploaded_file = st.file_uploader("Select a Quote Image")
if uploaded_file is not None:
    # To read file as bytes:
    
    image = Image.open(uploaded_file)
    st.write('Processing your image ....')
    image_array = np.asarray(image)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('selected image :')
        st.image(image_array)
    with col2:
        quote=image_to_text(image_array)
        st.subheader('Quote:')
        st.write(quote)
        meaning=quote_meaning(quote)
        st.subheader('Quote meaning:')
        st.write(meaning)
    # st.subheader('Generating image based on quote...')
    # generated_image=generte_quote_meaning_image(quote)
    # st.image(generated_image)

