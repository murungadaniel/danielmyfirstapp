import streamlit as st
import streamlit as st
from PIL import Image

# App Header
st.title("🌽 Maize Crop Disease Detection")
st.markdown("---")
st.subheader("Helping Farmers Detect Crop Diseases with Ease")

st.markdown("""
Welcome to the Maize Crop Disease Detector!  
Upload a clear image of your maize leaf below to begin the diagnosis.
""")

# Start a "card"
st.markdown('<div class="card">', unsafe_allow_html=True)

st.header("📷 Upload Maize Leaf Image")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Maize Leaf", use_column_width=True)
    st.success("Image uploaded successfully! 🖼️")
    st.button("🔍 Analyze Image (Coming Soon)")
else:
    st.info("Please upload an image to proceed.")

# Close the "card"
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("© 2025 Smart Farming Solutions | Built with ❤️ for Farmers")
