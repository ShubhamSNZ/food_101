import streamlit as st

st.set_page_config(
    page_title="Food-101 Classifier",
    page_icon="📷",
    layout="wide"
)

st.title("About 🔍")
st.markdown("""
**Objective:** Built an image classification model to identify 101 different food categories from the Food101 dataset using deep learning techniques.

**Key Achievements:**
- Implemented a transfer learning pipeline with EfficientNetB0 for fine-tuning.            
- Achieved efficient training with callbacks like EarlyStopping, ModelCheckpoint and ReduceLROnPlateau.
            
**Technologies** used:
- **TensorFlow/Keras** for deep learning.
- **Streamlit** for creating this web app.
- **Seaborn/Matplotlib** for data visualization.
            
**Outcome:** Delivered a robust model capable of classifying food images with high accuracy
""")