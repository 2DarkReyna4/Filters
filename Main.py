from cProfile import label

import streamlit as st
from PIL import ImageEnhance as IE
from PIL import Image as I
from io import BytesIO

st.title("Filters")
st.subheader("Applying Filters to Image")

file=st.file_uploader("Upload an image",type=['jpg','jpeg','png'])
if file:
    img=I.open(file)
    img = I.open(file).convert('RGB')

    A=img.copy()

    st.image(A,caption="Original Image",use_container_width=True)
    b = st.slider("Brightness", 0.0, 10.0, 1.0, 0.1)
    c = st.slider("Contrast", 0.0, 10.0, 1.0, 0.1)
    s = st.slider("Sharpness", 0.0, 10.0, 1.0, 0.1)
    co= st.slider("Color", 0.0, 3.0, 1.0, 0.1)


    enhanced_image = IE.Contrast(A).enhance(c)
    enhanced_image = IE.Sharpness(enhanced_image).enhance(s)
    enhanced_image = IE.Color(enhanced_image).enhance(co)
    enhanced_image = IE.Brightness(enhanced_image).enhance(b)
    enhanced_image = enhanced_image.convert('RGB')
    st.image(enhanced_image,caption="Enhanced image",use_container_width=True)

    st.download_button(
        label="Download Image",
        data=enhanced_image.tobytes(),
        file_name = "filtered image.png",
        mime="image/png"
    )

else:
    st.write("please upload a file")
