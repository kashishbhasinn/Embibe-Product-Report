import streamlit as st
from PIL import Image
import pandas as pd

# Custom Colors
PRIMARY_COLOR = "#0305DE"  # R-3, G-5, B-222
SECONDARY_COLOR = "#367CD7"  # R-54, G-124, B-215
TERTIARY_COLOR = "#72F4BD"  # R-114, G-244, B-189
BACKGROUND_COLOR = "#FCFCFC"  # R-252, G-252, B-252

# Page Configuration
st.set_page_config(page_title="Embibe AI-Powered Learning Platform", layout="wide", page_icon=":books:")
st.markdown(f"<style>body {{ background-color: {BACKGROUND_COLOR}; }}</style>", unsafe_allow_html=True)

# Header Section
st.title("AI-Powered Personalized Learning Platform for Embibe")
st.markdown(f"<h3 style='color:{PRIMARY_COLOR};'>Revolutionizing Education Through Personalization</h3>", unsafe_allow_html=True)

# Challenge Section
st.header("Challenge")
st.write("Many school students struggle with standardized teaching approaches, which fail to address individual learning speeds, knowledge gaps, and unique preferences. Teachers and parents lack actionable insights to help these students succeed, resulting in disengagement and missed growth opportunities.")

st.subheader("Supporting Data")
data = {"Metric": ["Students feeling disconnected", "Improvement in retention with personalization", "Improvement in parent/teacher engagement"],
        "Percentage": ["84%", "30%", "40%"]}
df = pd.DataFrame(data)
st.table(df)

# User Pain Points Section
st.header("User Pain Points")
st.markdown("### Students")
st.write("Struggle to keep up with a one-size-fits-all approach, lack feedback on weak areas and progress over time.")

st.markdown("### Teachers")
st.write("Difficulty identifying students' needs and providing personalized guidance.")

st.markdown("### Parents")
st.write("Limited visibility into their child’s progress and uncertainty about how to support their education.")

# Potential Solutions Section
st.header("Potential Solutions")
solutions = {
    "Solution": ["AI-Powered Personalized Platform", "Engaging Visual Learning Tools", "Data-Driven Dashboards"],
    "Pros": ["Improves engagement and learning outcomes.", "Increases student interest and retention.", "Provides transparency and improves collaboration."],
    "Cons": ["High initial investment.", "Complex implementation.", "Data privacy concerns."]
}
solutions_df = pd.DataFrame(solutions)
st.table(solutions_df)

# Metrics and Testing Section
st.header("Metrics and Testing")
st.write("To measure the platform's success, the following metrics will be used:")
st.markdown("- **Student Performance:** Improvement in test scores (Target: +15% within 3 months)")
st.markdown("- **Engagement:** Daily active usage time (Target: 20 minutes per session)")
st.markdown("- **Retention:** User retention after 3 months (Target: 80%)")
st.markdown("- **Teacher/Parent Satisfaction:** Feedback score (Target: 4.5+/5)")

# Product Roadmap Section
st.header("Product Roadmap")
st.markdown("### Phase 1: MVP Development (Month 1-3)")
st.write("Build adaptive learning features, teacher dashboards, and initial gamification.")

st.markdown("### Phase 2: Advanced Features (Month 4-6)")
st.write("Add AI recommendation engines, gamification with AR/VR, and beta testing in pilot schools.")

st.markdown("### Phase 3: Scale and Optimize (Month 7-12)")
st.write("Expand to more schools, enhance analytics, and improve scalability.")

# Launch Plan Section
st.header("Launch Plan")
st.markdown("### Pre-Launch (Month 1-6)")
st.write("Conduct user research, build marketing campaigns, and prepare onboarding materials.")

st.markdown("### During Launch (Month 7-8)")
st.write("Host demo sessions for pilot schools, provide 24/7 support, and run social media campaigns.")

st.markdown("### Post-Launch (Month 9-12)")
st.write("Analyze pilot data, expand user base, and roll out advanced AR/VR modules.")

# Visualization Example
st.header("Visualization: Top 10 Cryptocurrencies")
data = {
    "Cryptocurrency": ["Bitcoin", "Ethereum", "Tether", "BNB", "XRP", "Cardano", "Solana", "Dogecoin", "Polygon", "Litecoin"],
    "Market Cap (in Billion $)": [900, 450, 83, 65, 60, 45, 40, 20, 18, 10]
}
df_crypto = pd.DataFrame(data)
st.bar_chart(df_crypto.set_index("Cryptocurrency"))

# Long-Term Evolution Section
st.header("Long-Term Evolution")
st.write("In the long term, the platform will evolve by enhancing AI models for predictive analytics, expanding globally with curriculum customization, and integrating with the broader EdTech ecosystem.")

# Footer
st.markdown(f"<h4 style='color:{SECONDARY_COLOR};'>© 2025 by Kashish Bhasin</h4>", unsafe_allow_html=True)
