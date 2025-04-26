import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Kashish Bhasin | District by Zomato",
    page_icon="🧵",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        background-color: #f8f8f8;
    }
    .stApp {
        max-width: 1100px;
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
    <p class="subtext">Product + Tech Enthusiast | Applying to District by Zomato's Fashion Vertical</p>
</div>
""", unsafe_allow_html=True)

# Columns for layout
col1, col2 = st.columns([3, 2])

with col1:
    # Why Me Section
    st.markdown("""
    <div class="section-card">
        <div class="section-heading">Why Me</div>

        <div class="achievement">
            <div class="achievement-title">Business + Tech Fusion</div>
            <div class="achievement-detail">
                I bring experience from tech & operations at Dr. Oetker, IIM Bangalore, and Dodo—a GenAI startup—where I built and launched data pipelines, product stacks, and fashion-related analytics tools.
            </div>
        </div>

        <div class="achievement">
            <div class="achievement-title">Supply & Onboarding Ops</div>
            <div class="achievement-detail">
                I led supplier onboarding, improving turnaround time by 50%. My onboarding flows at Dr. Oetker helped scale 3X during festive sales.
            </div>
        </div>

        <div class="achievement">
            <div class="achievement-title">Relationship-First Approach</div>
            <div class="achievement-detail">
                With experience managing stakeholders across corporate, startup, and research settings, I understand how to build and maintain long-term collaborations.
            </div>
        </div>

        <div class="skills-section">
            <div class="skills-heading">Key Skills:</div>
            <div>
                <span class="skill-tag">Stakeholder Management</span>
                <span class="skill-tag">Supply Onboarding</span>
                <span class="skill-tag">Key Account Management</span>
                <span class="skill-tag">Product Strategy</span>
                <span class="skill-tag">Data Analysis</span>
                <span class="skill-tag">Trend Forecasting</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    # Tech Meets Fashion Section
    st.markdown("""
    <div class="section-card">
        <div class="section-heading">Tech Meets Fashion</div>

        <div class="achievement">
            <div class="achievement-title">GenAI for Fashion</div>
            <div class="achievement-detail">
                At Dodo, I built a recommendation engine for food & fashion using LangChain and vector databases. That same tech can power discovery on District’s platform.
            </div>
        </div>

        <div class="achievement">
            <div class="achievement-title">Visual AI</div>
            <div class="achievement-detail">
                I worked on image classification tools for trend detection, enabling fashion verticals to categorize SKUs by style & season.
            </div>
        </div>
    </div>

    <div class="section-card" style="text-align: center;">
        <div class="section-heading" style="text-align: center;">Let's Connect</div>
        <a href="https://drive.google.com/file/d/1yOURRESUMELINK" class="btn-download" target="_blank">View Resume</a>
        <a href="mailto:kashishbhasinn@gmail.com" class="btn-contact">Email Me</a>
        <p style="margin-top: 15px; font-size: 0.9rem; color: #000000;">
            <b>+91 9811149303</b> | <b>kashishbhasinn@gmail.com</b><br>
            <a href="https://linkedin.com/in/kashish-bhasin" target="_blank">LinkedIn</a>
        </p>
    </div>
    """, unsafe_allow_html=True)

# Footer CTA
st.markdown("""
<div class="cta-footer">
    Ready to stitch together design, data, and disruption. Let’s build fashion at District by Zomato 💅
</div>
""", unsafe_allow_html=True)
