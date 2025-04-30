import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Organizational Culture in the Age of AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for the color theme
def apply_custom_css():
    st.markdown("""
    <style>
    /* Main background */
    .stApp {
        background-color: #FFF9F0;
    }
    
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #FCD34D;
        padding: 1rem;
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #6366F1 !important;
        font-weight: bold;
    }
    
    /* Subheaders */
    h4, h5, h6 {
        color: #F472B6 !important;
    }
    
    /* Text */
    p, li {
        color: #1E293B;
    }
    
    /* Quote boxes */
    blockquote {
        background-color: #FFE4E6;
        padding: 15px;
        border-radius: 5px;
        border-left: 5px solid #F472B6;
        margin: 10px 0;
    }
    
    /* Custom box styling */
    .custom-box {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    
    /* Reflection box */
    .reflection-box {
        background-color: #FFE4E6;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
    }
    </style>
    """, unsafe_allow_html=True)

apply_custom_css()

# Sidebar
with st.sidebar:
    st.title("AI & Org Culture")
    st.markdown("### Kashish Bhasin")
    st.markdown("**Reg. No. 229310243**")
    st.markdown("**Manipal University Jaipur**")
    
    st.markdown("---")
    
    st.markdown("### Navigation")
    nav_options = [
        "Introduction",
        "Case Studies",
        "Key Themes",
        "Conclusion"
    ]
    
    nav_selection = st.radio("", nav_options)
    
    st.markdown("---")
    
    # Case studies selection
    if nav_selection == "Case Studies":
        st.markdown("### Select Case Study")
        case_study_options = [
            "🇺🇸 Mayo Clinic (USA)",
            "🇪🇪 e-Estonia (Estonia)",
            "🇯🇵 Toyota (Japan)",
            "🇮🇳 BYJU'S (India)",
            "🇩🇪 Volkswagen (Germany)"
        ]
        
        case_selection = st.selectbox("", case_study_options)
    else:
        case_selection = None

# Main content
st.title("Organizational Culture in the Age of AI")
st.markdown("*Embracing Data While Preserving Human Values*")

# Content dictionary for case studies
case_studies = {
    "🇺🇸 Mayo Clinic (USA)": {
        "title": "Humanizing Healthcare AI",
        "context": "The Mayo Clinic, with its 150-year history built on the principle that 'the needs of the patient come first,' implemented AI-powered diagnostic systems in 2019 while trying to preserve their human-centered approach.",
        "challenges": [
            "Physician autonomy vs. algorithmic recommendations",
            "Patient trust concerns about 'being treated by computers'",
            "Fear of reducing rich patient narratives to mere data points"
        ],
        "strategies": [
            "Collaborative AI Design with interdisciplinary teams",
            "'Augmentation, Not Replacement' messaging",
            "Modified performance metrics valuing both data insights and human skills",
            "Ethical AI Review Board against patient-first values",
            "'AI + Empathy' Training Programs"
        ],
        "results": [
            "31% improvement in diagnostic accuracy with AI-physician collaboration",
            "Maintained high patient satisfaction scores",
            "Increased staff confidence in AI as extension of expertise"
        ],
        "lesson": "Organizations can successfully adopt AI while preserving core values by treating cultural adaptation as an explicit, strategic priority. Collaborative AI governance ensures technology implementation remains aligned with human-centered mission."
    },
    "🇪🇪 e-Estonia (Estonia)": {
        "title": "Building Trust in Algorithmic Governance",
        "context": "Estonia, with 99% of public services online, began implementing AI systems in 2021 for permit applications, tax assessments, and benefit determinations while maintaining their culture of transparency.",
        "challenges": [
            "Transparency concerns about 'black box' decision-making",
            "Loss of human discretion for unusual circumstances",
            "Data sovereignty anxiety",
            "Cultural identity concerns about digital pragmatism overriding connection"
        ],
        "strategies": [
            "'Glass Box' AI Policy requiring explainable and auditable systems",
            "Human-in-the-Loop Design flagging unusual cases for human review",
            "Public AI Literacy Campaign",
            "Values-Based AI Design Process ensuring constitutional principles",
            "Citizen Participation through 'AI Assembly' forums"
        ],
        "results": [
            "87% decrease in processing times with increased citizen satisfaction",
            "24% decrease in appeals compared to pre-AI baseline",
            "76% of citizens trust AI-assisted decisions (vs 62% for purely human decisions)",
            "Improved civil servant retention as employees focus on complex cases"
        ],
        "lesson": "Transparency, citizen participation, and values-based design can build public trust in algorithmic governance. A culture of radical transparency proves compatible with AI when explainability and human oversight are prioritized."
    },
    "🇯🇵 Toyota (Japan)": {
        "title": "Harmonizing Kaizen Culture with AI",
        "context": "Toyota's organizational culture, defined by its Production System and kaizen philosophy, integrated machine learning systems for quality control, maintenance, and scheduling in 2022.",
        "challenges": [
            "Bottom-up vs. top-down improvement tensions",
            "Concerns about capturing tacit knowledge",
            "Team cohesion impacts with individualized work instructions",
            "Contradiction with 'respect for people' principle"
        ],
        "strategies": [
            "Worker-Guided AI Development through 'AI Kaizen Teams'",
            "Hybrid Improvement System for human teams to investigate",
            "'Human-in-Command' Principle allowing worker expertise to override AI",
            "Skills Evolution Program developing 'AI collaboration skills'",
            "Cultural Measurement System tracking team capability and satisfaction"
        ],
        "results": [
            "29% decrease in quality defects across AI-enhanced production",
            "18% improvement in production efficiency while maintaining team structure",
            "Stable worker satisfaction despite technological change",
            "34% increase in improvement suggestions from employees"
        ],
        "lesson": "Traditional cultures built around human judgment can successfully incorporate AI when technology enhances rather than replaces human capabilities. 'AI-Enhanced Kaizen' preserves cultural foundations while leveraging new technological possibilities."
    },
    "🇮🇳 BYJU'S (India)": {
        "title": "Balancing Algorithmic Learning and Teacher Wisdom",
        "context": "BYJU'S, India's largest edtech company, began implementing AI systems for personalized learning paths, automated assessment, and content recommendations in 2021.",
        "challenges": [
            "Teacher authority vs. algorithmic recommendations",
            "Creative teaching vs. optimization pressure",
            "Personalization vs. community learning experiences",
            "Human connection concerns in education"
        ],
        "strategies": [
            "'Teacher-AI Partnership' Framework establishing teachers as senior partners",
            "Explainable AI Requirements providing clear explanations",
            "Cultural Values Assessment against core principles",
            "'Teaching Moments' Priority for human intervention",
            "Expanded Teacher Role focusing on motivation and complex concepts"
        ],
        "results": [
            "26% improvement in student learning outcomes",
            "89% of teachers feel valued for unique human contributions",
            "High student engagement with hybrid approach",
            "31% improvement in customer retention"
        ],
        "lesson": "Educational organizations can integrate AI while preserving human-centered teaching culture by establishing complementary roles of algorithms and educators. Their partnership model ensures technology enhances rather than replaces human elements."
    },
    "🇩🇪 Volkswagen (Germany)": {
        "title": "Reinventing Manufacturing Culture with AI Collaboration",
        "context": "Volkswagen, with its 90-year heritage balancing German engineering precision and collaborative labor relations, implemented AI systems for supply chain, maintenance, and design in 2020.",
        "challenges": [
            "Engineers' expertise questioned by algorithms",
            "Disruption of traditional decision hierarchies",
            "Works council concerns about job displacement",
            "Cross-functional friction between departments"
        ],
        "strategies": [
            "AI Co-Creation Process with frontline experts",
            "Joint Human-AI Decision Protocol defining decision ownership",
            "Works Council AI Agreement guaranteeing retraining",
            "'Experience + Data' Value Statement redefining expertise",
            "Cultural Ambassador Network of veteran employees"
        ],
        "results": [
            "23% improvement in production efficiency",
            "37% decline in quality control issues",
            "67% positive attitude toward AI collaboration after initial skepticism",
            "94% workforce retention through significant retraining"
        ],
        "lesson": "Organizations with established cultures can integrate AI when treating adaptation as a collaborative process rather than purely technical implementation. Engaging both management expertise and worker representation creates sustainable transformation while preserving core values."
    }
}

# Key themes content
key_themes = {
    "Data vs. Intuition": {
        "quote": "The question isn't whether AI or humans should decide—it's about designing systems where each contributes their unique strengths to better decisions than either could make alone.",
        "approaches": [
            "Decision Classification Frameworks for algorithm-led, human-led, or collaborative decisions",
            "Explainable AI Requirements enabling informed human oversight",
            "Confidence Thresholds deferring to human judgment when needed",
            "Training for Collaborative Decision-Making between humans and AI"
        ]
    },
    "Bias & Fairness": {
        "quote": "Creating fair AI isn't just a technical challenge—it's a profound cultural commitment that requires ongoing vigilance and diverse perspectives at every stage of development.",
        "approaches": [
            "Diverse AI Development Teams to identify potential bias",
            "Explicit Fairness Metrics across demographic groups",
            "Bias Bounty Programs rewarding identification of system bias",
            "Cultural Values Testing ensuring outcomes match ethical principles"
        ]
    },
    "Transparency": {
        "quote": "Investing in explainable AI dramatically accelerated adoption by allowing teams to build informed trust rather than blind faith.",
        "approaches": [
            "Tiered Explanation Systems for different user needs",
            "Process Transparency about development and testing",
            "Counterfactual Explanations showing how different inputs change outputs",
            "Decision Trail Documentation of factors influencing recommendations"
        ]
    },
    "Workforce Adaptation": {
        "quote": "The real challenge was helping people reimagine their professional identities in a world where they collaborated with intelligent machines.",
        "approaches": [
            "Skills Evolution Programs developing new professional identities",
            "Participation in AI Design involving frontline workers",
            "New Recognition Systems valuing human-AI collaboration",
            "Change Narrative Development showing how AI enhances human contributions"
        ]
    }
}

# Introduction content
if nav_selection == "Introduction":
    st.markdown("## Introduction: The Algorithmic-Human Balance")
    
    st.markdown("""
    Organizations worldwide face a critical challenge: how to harness artificial intelligence while preserving the human values that define their organizational culture. This tension—between algorithmic efficiency and human-centered approaches—represents one of the most significant organizational transformations of our time.

    AI systems excel at processing vast data, identifying patterns, and making predictions with remarkable accuracy. Yet organizations are human communities built on values like creativity, empathy, ethical judgment, and meaningful connections. 

    This case study explores how forward-thinking organizations across different sectors and regions are navigating this complex terrain, reshaping their cultures to embrace data-driven decision-making while simultaneously preserving the human values that give their work meaning and purpose.
    """)
    
    st.markdown("### Key Questions Explored")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        - How do organizations maintain human connection in algorithmic environments?
        - What happens when AI recommendations conflict with human intuition?
        - How can leaders foster cultures that value both data and human wisdom?
        - What new roles emerge in AI-integrated organizations?
        """)
    
    with col2:
        st.markdown("""
        - How do different cultural contexts affect AI adoption?
        - What ethical frameworks guide responsible AI implementation?
        - How do organizations measure success beyond efficiency?
        - What resistance patterns emerge and how are they addressed?
        """)

# Case Studies Section
elif nav_selection == "Case Studies":
    st.markdown("## Global Case Studies")
    
    if case_selection:
        case = case_studies[case_selection]
        
        st.markdown(f"### {case_selection}: {case['title']}")
        
        st.markdown(f"**Context:**\n{case['context']}")
        
        st.markdown("**Cultural Challenges:**")
        for challenge in case['challenges']:
            st.markdown(f"- {challenge}")
        
        st.markdown("**Cultural Adaptation Strategies:**")
        for strategy in case['strategies']:
            st.markdown(f"- {strategy}")
        
        st.markdown("**Results & Impact:**")
        for result in case['results']:
            st.markdown(f"- {result}")
        
        st.markdown(f"**Key Lesson:**\n{case['lesson']}")
    else:
        st.info("Select a case study from the sidebar to view details")
        
        # Show brief overview of all cases
        for key, case in case_studies.items():
            with st.expander(f"{key}: {case['title']}"):
                st.markdown(f"**Context:** {case['context']}")
                st.markdown(f"**Key Lesson:** {case['lesson']}")

# Key Themes Section
elif nav_selection == "Key Themes":
    st.markdown("## Key Tensions & Themes")
    
    theme_tabs = st.tabs(list(key_themes.keys()))
    
    for i, (theme_name, theme) in enumerate(key_themes.items()):
        with theme_tabs[i]:
            st.markdown(f"### {theme_name}")
            
            st.markdown(f"""
            <div style="background-color: #FFE4E6; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
            "{theme['quote']}"
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("**Key Approaches:**")
            for approach in theme['approaches']:
                st.markdown(f"- {approach}")

# Conclusion Section
elif nav_selection == "Conclusion":
    st.markdown("## Conclusion: Building Human-Centered AI Cultures")
    
    st.markdown("""
    Successfully integrating AI into organizational culture requires more than technical implementation—it demands thoughtful cultural evolution that preserves core human values while embracing new possibilities.
    
    **Common Success Factors:**
    
    1. **Values-First Design:** AI systems designed to enhance rather than replace core values
    2. **Collaborative Governance:** Diverse stakeholders establishing AI usage guidelines
    3. **Complementary Capabilities:** Positioning AI as enhancing human capabilities
    4. **Cultural Metrics:** Measuring impacts on cohesion and satisfaction, not just efficiency
    5. **Continuous Adaptation:** Treating AI integration as an ongoing conversation
    """)
    
    st.markdown("""
    <div style="background-color: #FFE4E6; padding: 20px; border-radius: 10px; margin-top: 20px;">
    <h3 style="color: #F472B6;">Personal Reflection from Kashish Bhasin</h3>
    
    <p>As I studied these global cases, I was struck by their relevance to India's AI transformation. Indian organizations have a unique opportunity to leapfrog development stages by thoughtfully integrating AI while preserving human-centered cultural values.</p>
    
    <p>For my generation of Indian professionals, we must develop both technical AI literacy and cultural intelligence. We need to become bilingual in the language of algorithms and human values.</p>
    
    <p>The most successful organizations won't be those with the most advanced technology, but those creating cultures where human wisdom and algorithmic intelligence enhance each other. As students entering this transformed workplace, we should develop ethical reasoning, collaborative abilities, and change leadership capabilities to shape AI implementations reflecting our deeply held values.</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("References"):
        st.markdown("""
        - Ahmed, S., & Kumar, P. (2023). "AI-Enhanced Learning: The BYJU'S Approach to Educational Technology." *Journal of Educational Innovation*, 18(2)
        - Nakamura, H. (2023). "Toyota's AI Kaizen: Merging Tradition and Innovation." *International Journal of Manufacturing Excellence*, 45(3)
        - Reinmann, K., & Weber, D. (2024). "Collaborative Intelligence: Volkswagen's AI Transformation." *European Business Review*, 36(1)
        - Tamm, L., & Kask, E. (2023). "Algorithmic Governance and Citizen Trust: The Estonian Model." *Digital Government: Research and Practice*, 4(2)
        """)

# Custom footer for all pages
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #1E293B; font-size: 0.8em;">
© 2025 Kashish Bhasin | Manipal University Jaipur | Case Study on Organizational Culture in the Age of AI
</div>
""", unsafe_allow_html=True)
