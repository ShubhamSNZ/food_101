import streamlit as st

st.set_page_config(
    page_title="Food-101 Classifier",
    page_icon="📷",
    layout="wide"
)

st.title("Welcome to the EfficientNetB0 Image Classifier WebApp! 🚀")
st.markdown("""
This web app uses a pre-trained EfficientNetB0 model to classify images. Explore the features using the navigation on the left.


#### Features:
- Upload an image and classify it into one of the trained categories.
- View model architecture and insights.
- Download predictions and provide feedback.

Use the sidebar to navigate through the app!
""")
