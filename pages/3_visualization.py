import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def plot_heatmap(classes, confidences):
    """Plot a heatmap of class confidences (scaled to percentages)."""
    confidences_percent = [conf for conf in confidences]  # Scale to 0–100
    plt.figure(figsize=(8, 4))
    sns.heatmap(
        [confidences_percent],
        annot=True,
        fmt=".2f",
        xticklabels=classes,
        yticklabels=["Confidence"],
        cmap="coolwarm",
        cbar=False
    )
    plt.xticks(rotation=45, ha='right')
    st.pyplot(plt)  # type:ignore

# Main function for Heatmap Visualization Page
def main():
    st.set_page_config(
    page_title="Food-101 Classifier",
    page_icon="📷",
    layout="wide"
)
    st.title("Confidence Heatmap Visualization")
    st.write("""
        This page visualizes the confidence levels for the top predictions 
        generated on the **Classifier** page. Please ensure you have completed 
        predictions on the previous page to see meaningful data.
    """)

    # Retrieve stored results
    if "top_classes" in st.session_state and "top_confidences" in st.session_state:
        top_classes = st.session_state["top_classes"]
        top_confidences = st.session_state["top_confidences"]

        st.write("### Top Predictions with Confidence Heatmap")
        st.write("**Predicted Classes:**")
        for cls, conf in zip(top_classes, top_confidences):
            st.write(f"- {cls}: {conf:.2f}%")

        st.write("### Confidence Heatmap")
        plot_heatmap(top_classes, top_confidences)
    else:
        st.warning("No predictions found. Please run the classifier on the previous page first.")

if __name__ == "__main__":
    main()
