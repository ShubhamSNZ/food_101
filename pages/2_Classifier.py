import streamlit as st
from tensorflow.keras.models import load_model #type:ignore
from tensorflow.keras.preprocessing.image import img_to_array #type:ignore
import numpy as np
from PIL import Image
from resources import model_file_path, class_names
import pandas as pd
st.set_page_config(
    page_title="Food-101 Classifier",
    page_icon="📷",
    layout="wide"
)

def load_model_func(model_path):
    try:
        return load_model(model_path)
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

def preprocess_image(image, target_size=(224, 224)):
    image = image.resize(target_size)
    image_array = img_to_array(image)
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

st.title("Image Classification 📷")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption="Uploaded Image", use_container_width=True)
    
    if st.button("Predict"):
        status_message = st.info("Classifying...")
        model = load_model_func(model_file_path)
        if model:
            processed_image = preprocess_image(image)
            predictions = model.predict(processed_image)
            
            top_indices = np.argsort(predictions[0])[::-1][:5]
            top_classes = [class_names[idx] for idx in top_indices]
            top_confidences = predictions[0][top_indices] * 100

            st.session_state["top_classes"] = top_classes
            st.session_state["top_confidences"] = top_confidences


            status_message.empty()
            
            st.success(f"Predicted class: {top_classes[0]} with confidence {top_confidences[0]:.2f}%")
            
            result_data = {"Class": top_classes, "Confidence (%)": top_confidences}
            result_df = pd.DataFrame(result_data)
            st.dataframe(result_df)
            
            csv = result_df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="Download Predictions as CSV",
                data=csv,
                file_name="predictions.csv",
                mime="text/csv"
            )
