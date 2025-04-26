import streamlit as st
import base64

# Set page config for a cleaner look
st.set_page_config(
    page_title="Kashish Bhasin | District by Zomato",
    page_icon="👔",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main {
        background-color: #f8f8f8;
        padding: 0;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .header-container {
        background-color: #E23744;
        color: white;
        padding: 2rem 1.5rem;
        border-radius: 0 0 20px 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .section-card {
        background-color: white;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.08);
    }
    .cta-footer {
        background-color: #1A1A1A;
        color: white;
        padding: 15px;
        border-radius: 15px;
        text-align: center;
        margin-top: 20px;
        font-style: italic;
    }
    .btn-download {
        background-color: #E23744;
        color: white;
        padding: 10px 25px;
        border-radius: 30px;
        border: none;
        font-weight: 600;
        margin-right: 10px;
        cursor: pointer;
        text-decoration: none;
        display: inline-block;
    }
    .btn-contact {
        background-color: #1A1A1A;
        color: white;
        padding: 10px 25px;
        border-radius: 30px;
        border: none;
        font-weight: 600;
        cursor: pointer;
        text-decoration: none;
        display: inline-block;
    }
    h1 {
        margin: 0;
        font-size: 2.2rem;
    }
    .subtext {
        font-size: 1rem;
        opacity: 0.85;
        margin-top: 5px;
    }
    .section-heading {
        color: #000000;
        font-size: 1.5rem;
        font-weight: 700;
        border-bottom: 2px solid #f2f2f2;
        padding-bottom: 8px;
        margin-bottom: 15px;
    }
    .skill-tag {
        background-color: #f2f2f2;
        color: #000000;
        padding: 5px 12px;
        border-radius: 20px;
        margin-right: 8px;
        margin-bottom: 8px;
        display: inline-block;
        font-size: 0.85rem;
        font-weight: 500;
    }
    .skills-section {
        margin-top: 20px;
    }
    .skills-heading {
        font-weight: 600;
        color: #000000;
        font-size: 1.1rem;
        margin-bottom: 10px;
    }
    .achievement {
        border-left: 3px solid #E23744;
        padding-left: 15px;
        margin-bottom: 15px;
    }
    .achievement-title {
        font-weight: 600;
        margin-bottom: 5px;
        color: #000000;
    }
    .achievement-detail {
        font-size: 0.9rem;
        color: #000000;
    }
</style>
""", unsafe_allow_html=True)

# Header section
st.markdown("""
<div class="header-container">
    <h1>Hi, I'm Kashish Bhasin</h1>
    <p class="subtext">Product + Tech Enthusiast applying to build the Fashion Vertical at District by Zomato</p>
</div>
""", unsafe_allow_html=True)

# Main content in columns for responsive design
col1, col2 = st.columns([3, 2])

with col1:
    # Why Me Section
    st.markdown("""
    <div class="section-card">
        <div class="section-heading">Why Me</div>
        <div class="achievement">
            <div class="achievement-title">Perfect blend of Business & Tech</div>
            <div class="achievement-detail">
                Led cross-functional teams of 10+ specialists in product development with 
                experience managing stakeholders across UI/UX, development, and engineering teams.
            </div>
        </div>
        <div class="achievement">
            <div class="achievement-title">Experience in Supply & Onboarding</div>
            <div class="achievement-detail">
                Built onboarding pipelines that improved efficiency by 50% and conducted 
                market analysis driving 65% sales growth at Dr. Oetker India.
            </div>
        </div>
        <div class="achievement">
            <div class="achievement-title">Account Management Skills</div>
            <div class="achievement-detail">
                Managed product roadmaps and strategic relationships with multiple stakeholders, ensuring 
                timely delivery of features while optimizing for user experience.
            </div>
        </div>
        
        <div class="skills-section">
            <div class="skills-heading">Key Skills:</div>
            <span class="skill-tag">Stakeholder Management</span>
            <span class="skill-tag">Supply Onboarding</span>
            <span class="skill-tag">Key Account Management</span>
            <span class="skill-tag">Market Analysis</span>
            <span class="skill-tag">Data Analytics</span>
            <span class="skill-tag">Product Strategy</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    # Tech Meets Fashion Section
    st.markdown("""
    <div class="section-card">
        <div class="section-heading">Tech Meets Fashion</div>
        <div class="achievement">
            <div class="achievement-title">AI-Powered Personalization</div>
            <div class="achievement-detail">
                Developed smart recommendation systems that improved user engagement by 40%, 
                applicable to personalized fashion discovery.
            </div>
        </div>
        <div class="achievement">
            <div class="achievement-title">Visual Analysis & Recognition</div>
            <div class="achievement-detail">
                Built image classification systems with 80% accuracy that could enhance 
                fashion cataloging and trend analysis.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Resume & Contact Section
    st.markdown("""
    <div class="section-card" style="text-align: center;">
        <div class="section-heading" style="text-align: center;">Let's Connect</div>
        <a href="mailto:kashishbhasinn@gmail.com" class="btn-download">Download CV</a>
        <a href="https://linkedin.com/in/kashish-bhasin" class="btn-contact">Let's Talk</a>
        <p style="margin-top: 15px; font-size: 0.9rem; color: #000000;">
            <b>+91 9811149303</b> | kashishbhasinn@gmail.com
        </p>
    </div>
    """, unsafe_allow_html=True)

# Call to Action Footer
st.markdown("""
<div class="cta-footer">
    Ready to stitch data with design. Let's build fashion @ District by Zomato.
</div>
""", unsafe_allow_html=True)
