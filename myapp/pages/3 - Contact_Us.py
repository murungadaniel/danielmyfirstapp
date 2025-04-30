# Import basic libraries
import streamlit as st
from datetime import datetime
import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Page configuration
st.set_page_config(
    page_title="Contact ZeaWatch Technologies",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS - simplified to avoid rendering issues
st.markdown("""
<style>
    /* Base styling */
    .main-header {
        color: #2e7d32;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .sub-header {
        color: #388e3c;
        font-size: 1.8rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    .section-divider {
        margin: 2rem 0;
        border-top: 1px solid #e0e0e0;
    }
    
    .contact-info-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
    }
    
    .contact-info-item {
        display: flex;
        align-items: flex-start;
        margin-bottom: 1.5rem;
    }
    
    .contact-info-icon {
        color: #2e7d32;
        font-size: 1.5rem;
        margin-right: 1rem;
        min-width: 24px;
    }
    
    .contact-info-text h3 {
        margin: 0;
        color: #2e7d32;
        font-size: 1.1rem;
    }
    
    .contact-info-text p {
        margin: 0.3rem 0 0 0;
        color: #555;
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Button styling */
    .stButton > button {
        background-color: #2e7d32;
        color: white;
        font-weight: bold;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 4px;
    }
    
    .stButton > button:hover {
        background-color: #1b5e20;
    }
    
    /* Social icons */
    .social-icons {
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin-top: 1rem;
    }
    
    .social-icon {
        font-size: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown('<h1 class="main-header">Contact ZeaWatch Technologies</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-size: 1.2rem; max-width: 800px; margin: 0 auto 2rem auto; color: #555;">Have questions about our crop disease detection system? We\'re here to help farmers and agricultural professionals protect their harvests.</p>', unsafe_allow_html=True)
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# Main content
st.markdown('<h2 class="sub-header">Get In Touch</h2>', unsafe_allow_html=True)

# Create columns for form and contact info
left_column, right_column = st.columns([3, 2])

with left_column:
    # Using Streamlit's native form components instead of HTML
    with st.container():
        st.subheader("Send Us a Message")
        
        # Form fields using Streamlit components
        name = st.text_input("Full Name", placeholder="John Doe")
        email = st.text_input("Email Address", placeholder="john@example.com")
        phone = st.text_input("Phone Number (Optional)", placeholder="+1 (555) 123-4567")
        
        inquiry_type = st.selectbox(
            "Inquiry Type",
            options=[
                "Select inquiry type",
                "General Inquiry",
                "Technical Support",
                "Sales & Pricing",
                "Partnership Opportunities",
                "Feedback & Suggestions"
            ],
            index=0
        )
        
        crop_type = st.selectbox(
            "Crop Type (Optional)",
            options=[
                "Select your main crop",
                "Tomato",
                "Potato",
                "Corn",
                "Rice",
                "Wheat",
                "Other"
            ],
            index=0
        )
        
        message = st.text_area("Your Message", placeholder="Please describe your inquiry or how we can help you...", height=150)
        
        # Using technology checkbox
        using_tech = st.radio(
            "Are you currently using any crop monitoring technology?",
            options=["Yes", "No"],
            horizontal=True
        )
        if st.button("Send Message", type="primary"):
            if not name or not email or not message:
                st.error("Please fill in all required fields (name, email, and message).")
            else:
                try:
                    # Create email
                    msg = MIMEMultipart()
                    sender_email = "murungadaniel2002@gmail.com"  # Replace with your Gmail
                    app_password = "tpiwxcrqkwkszmgq"  # Replace with your app password
                    recipient_email = "murungadaniel2002@gmail.com"
                    
                    msg['From'] = f"ZeaWatch Contact Form <{sender_email}>"
                    msg['To'] = recipient_email
                    msg['Subject'] = f"New Contact Form: {inquiry_type} from {name}"
                    msg['Reply-To'] = email  # Set reply-to as the user's email
                    
                    # Email body with HTML formatting
                    html = f"""
                    <html>
                    <body style="font-family: Arial, sans-serif; line-height: 1.6;">
                        <h2 style="color: #2e7d32;">New Contact Form Submission</h2>
                        <table style="border-collapse: collapse; width: 100%;">
                            <tr>
                                <td style="padding: 8px; border: 1px solid #ddd; font-weight: bold;">Name:</td>
                                <td style="padding: 8px; border: 1px solid #ddd;">{name}</td>
                            </tr>
                            <tr>
                                <td style="padding: 8px; border: 1px solid #ddd; font-weight: bold;">Email:</td>
                                <td style="padding: 8px; border: 1px solid #ddd;">{email}</td>
                            </tr>
                            <tr>
                                <td style="padding: 8px; border: 1px solid #ddd; font-weight: bold;">Phone:</td>
                                <td style="padding: 8px; border: 1px solid #ddd;">{phone if phone else "Not provided"}</td>
                            </tr>
                            <tr>
                                <td style="padding: 8px; border: 1px solid #ddd; font-weight: bold;">Inquiry Type:</td>
                                <td style="padding: 8px; border: 1px solid #ddd;">{inquiry_type}</td>
                            </tr>
                            <tr>
                                <td style="padding: 8px; border: 1px solid #ddd; font-weight: bold;">Crop Type:</td>
                                <td style="padding: 8px; border: 1px solid #ddd;">{crop_type}</td>
                            </tr>
                            <tr>
                                <td style="padding: 8px; border: 1px solid #ddd; font-weight: bold;">Using Technology:</td>
                                <td style="padding: 8px; border: 1px solid #ddd;">{using_tech}</td>
                            </tr>
                        </table>
                        <h3 style="color: #2e7d32; margin-top: 20px;">Message:</h3>
                        <p style="background-color: #f9f9f9; padding: 10px; border-left: 4px solid #2e7d32;">{message}</p>
                    </body>
                    </html>
                    """
                    
                    # Attach HTML content
                    part = MIMEText(html, "html")
                    msg.attach(part)
                    
                    # Connect to SMTP server
                    with smtplib.SMTP("smtp.gmail.com", 587) as server:
                        server.starttls()
                        server.login(sender_email, app_password)
                        server.send_message(msg)
                    
                    st.success("Thank you! Your message has been sent successfully. We'll get back to you soon.")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
                    st.error("Please check your email settings and try again.")

with right_column:
    # Contact information
    st.markdown('<div class="contact-info-card">', unsafe_allow_html=True)
    
    # Phone
    st.markdown("""
    <div class="contact-info-item">
        <div class="contact-info-icon">📞</div>
        <div class="contact-info-text">
            <h3>Phone</h3>
            <p>+1 (555) 123-4567</p>
            <p style="font-size: 0.9rem; color: #777;">Mon-Fri, 8am-5pm</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Email
    st.markdown("""
    <div class="contact-info-item">
        <div class="contact-info-icon">✉️</div>
        <div class="contact-info-text">
            <h3>Email</h3>
            <p>support@zeawatch.com</p>
            <p style="font-size: 0.9rem; color: #777;">We'll respond within 24 hours</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Office
    st.markdown("""
    <div class="contact-info-item">
        <div class="contact-info-icon">📍</div>
        <div class="contact-info-text">
            <h3>Office</h3>
            <p>123 AgriTech Boulevard</p>
            <p>Farmington, CA 95432</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Hours
    st.markdown("""
    <div class="contact-info-item">
        <div class="contact-info-icon">🕒</div>
        <div class="contact-info-text">
            <h3>Hours</h3>
            <p>Monday - Friday: 8am - 5pm</p>
            <p>Saturday: 9am - 1pm (Support only)</p>
            <p>Sunday: Closed</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Social media icons
    st.markdown("""
    <div class="social-icons">
        <span class="social-icon">📱</span>
        <span class="social-icon">📷</span>
        <span class="social-icon">🐦</span>
        <span class="social-icon">💼</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# FAQ Section
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
st.markdown('<h2 class="sub-header" style="text-align: center;">Frequently Asked Questions</h2>', unsafe_allow_html=True)

faq_col1, faq_col2 = st.columns(2)

with faq_col1:
    with st.expander("How accurate is the crop disease detection?"):
        st.write("Our AI-powered system achieves over 95% accuracy in identifying common crop diseases. The system is continuously trained on new data to improve accuracy for rare conditions.")
    
    with st.expander("What crops does your system support?"):
        st.write("Currently, we support disease detection for tomato, potato, corn, rice, and wheat crops. We're expanding our database to include more crops based on user demand and regional agricultural needs.")

with faq_col2:
    with st.expander("Do I need internet access to use the app?"):
        st.write("Yes, an internet connection is required for the full functionality of our system. However, we're developing an offline mode for basic detection capabilities in areas with limited connectivity.")
    
    with st.expander("Is there a mobile app available?"):
        st.write("Yes, we offer mobile apps for both iOS and Android devices, allowing farmers to take photos directly in the field and receive instant disease identification and treatment recommendations.")

# View all FAQs button
st.markdown("""
<div style="text-align: center; margin-top: 1.5rem;">
    <a href="#" style="display: inline-block; padding: 0.75rem 1.5rem; background-color: #2e7d32; color: white; border-radius: 6px; text-decoration: none; font-weight: 600; transition: all 0.3s;">
        View All FAQs
    </a>
</div>
""", unsafe_allow_html=True)

# Map section
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# Placeholder for map
st.markdown("""
<div style="width: 100%; height: 300px; background-color: #f1f8e9; display: flex; align-items: center; justify-content: center; border-radius: 6px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
    <div style="text-align: center;">
        <span style="font-size: 2rem; color: #2e7d32;">📍</span>
        <p style="color: #2e7d32; font-weight: 600; margin-top: 0.5rem;">Interactive Map Would Be Displayed Here</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
st.markdown(f"""
<div style="text-align: center; padding: 2rem 0; color: #666; font-size: 0.9rem;">
    <p>© {datetime.now().year} ZeaWatch Technologies. All rights reserved.</p>
    <div style="display: flex; justify-content: center; gap: 2rem; margin-top: 1rem;">
        <a href="#" style="color: #2e7d32; text-decoration: none;">Privacy Policy</a>
        <a href="#" style="color: #2e7d32; text-decoration: none;">Terms of Service</a>
        <a href="#" style="color: #2e7d32; text-decoration: none;">Sitemap</a>
    </div>
</div>
""", unsafe_allow_html=True)
