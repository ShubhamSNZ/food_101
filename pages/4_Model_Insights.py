import streamlit as st
from tensorflow.keras.models import load_model #type:ignore
from resources import model_file_path
import os

st.set_page_config(
    page_title="Food-101 Classifier",
    page_icon="📷",
    layout="wide"
)

# Title
st.title("Model Insights 📊")

# Load the model
try:
    model = load_model(model_file_path)
    st.markdown("### Model Architecture")
    
    # Save and display model architecture
    from tensorflow.keras.utils import plot_model #type:ignore
    
    def save_model_plot(model, file_path="model_architecture.png"):
        """Save the model architecture as an image."""
        try:
            plot_model(model, to_file=file_path, show_shapes=True, show_layer_names=True)
            return file_path
        except Exception as e:
            st.error(f"Error generating model plot: {str(e)}")
            return None

    model_plot_path = save_model_plot(model, "model_architecture.png")
    
    if model_plot_path and os.path.exists(model_plot_path):
        st.image(model_plot_path, caption="Food-101 Architecture", use_container_width=True)
    else:
        st.error("Unable to display the model architecture. Check your TensorFlow setup.")

except Exception as e:
    st.error(f"Error loading model: {str(e)}")
