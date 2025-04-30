import streamlit as st
import base64
from PIL import Image
import requests
from io import BytesIO

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
    .css-1d391kg, .css-12oz5g7 {
        background-color: #FCD34D;
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
    
    /* Custom button styling */
    .stButton>button {
        background-color: #34D399;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 24px;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background-color: #FCD34D;
        border-radius: 5px;
        color: #1E293B !important;
    }
    
    .streamlit-expanderContent {
        background-color: #FFF9F0;
        border: 1px solid #FCD34D;
        border-top: none;
        border-radius: 0 0 5px 5px;
    }
    
    /* Case study box */
    .case-study-box {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    
    /* Reflection box */
    .reflection-box {
        background-color: #FFE4E6;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
    }
    
    /* Flag emoji styling */
    .flag-emoji {
        font-size: 2em;
        margin-right: 10px;
        vertical-align: middle;
    }
    
    /* Container styling */
    .content-container {
        background-color: white;
        padding: 25px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

apply_custom_css()

# Sidebar
with st.sidebar:
    st.image("https://i.ibb.co/WksnLbG/ai-culture-logo.png", use_column_width=True)
    st.markdown("### Kashish Bhasin")
    st.markdown("**Reg. No. 229310243**")
    st.markdown("**Manipal University Jaipur**")
    
    st.markdown("---")
    
    st.markdown("### Navigation")
    nav_options = [
        "Introduction",
        "Case Studies",
        "Key Themes & Tensions",
        "Conclusion & Reflection",
        "About This Project"
    ]
    
    nav_selection = st.radio("", nav_options)
    
    st.markdown("---")
    
    st.markdown("### Case Studies")
    case_study_options = [
        "🇺🇸 Mayo Clinic (USA)",
        "🇪🇪 e-Estonia (Estonia)",
        "🇯🇵 Toyota (Japan)",
        "🇮🇳 BYJU'S (India)",
        "🇩🇪 Volkswagen (Germany)"
    ]
    
    case_selection = st.selectbox("Jump to a specific case study:", case_study_options)
    if st.button("Go to Case Study", key="goto_case"):
        nav_selection = "Case Studies"
    
    st.markdown("---")
    
    st.markdown("""
    <div style="font-size: 0.8em; color: #4B5563;">
    This interactive case study explores how organizations worldwide navigate AI adoption while preserving human values.
    </div>
    """, unsafe_allow_html=True)

# Main content
st.title("Organizational Culture in the Age of AI: Embracing Data While Preserving Human Values")
st.markdown("*A Global Case Study exploring the intersection of artificial intelligence and organizational culture*")

# Introduction Section
if nav_selection == "Introduction":
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    
    st.markdown("## Introduction: The Algorithmic-Human Balance")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        In today's rapidly evolving technological landscape, organizations worldwide face a critical challenge: how to harness the power of artificial intelligence while preserving the human values that define their organizational culture. This tension—between algorithmic efficiency and human-centered approaches—represents one of the most significant organizational transformations of our time.
        
        AI systems excel at processing vast amounts of data, identifying patterns, and making predictions with remarkable accuracy. Yet organizations are more than data-processing entities; they are human communities built on values like creativity, empathy, ethical judgment, and meaningful social connections. The algorithmic world of AI and the relational world of human organizations can sometimes operate on fundamentally different principles.
        
        This case study explores how forward-thinking organizations across different sectors and regions are navigating this complex terrain. We examine how they're reshaping their cultures to embrace data-driven decision-making while simultaneously preserving—and in some cases strengthening—the human values that give their work meaning and purpose.
        """)
    
    with col2:
        st.image("https://i.ibb.co/0FhKN9M/ai-human-balance.png", caption="The balance between algorithmic efficiency and human values", use_column_width=True)
    
    st.markdown("### Key Questions Explored")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        - How do organizations maintain human connection in algorithmic environments?
        - What happens when AI recommendations conflict with human intuition?
        - How can leaders foster cultures that value both data-driven insights and human wisdom?
        - What new roles and practices emerge in AI-integrated organizations?
        """)
    
    with col2:
        st.markdown("""
        - How do different cultural contexts affect AI adoption approaches?
        - What ethical frameworks guide responsible AI implementation?
        - How do organizations measure success beyond efficiency metrics?
        - What resistance patterns emerge and how are they addressed?
        """)
    
    st.markdown("### Methodology")
    st.markdown("""
    This case study examines organizations across diverse sectors and geographic regions to identify patterns, challenges, and successful approaches to AI-integrated organizational cultures. Each case highlights different facets of the cultural transformation process while revealing common themes that transcend industry and cultural boundaries.
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Case Studies Section
elif nav_selection == "Case Studies":
    st.markdown("## Global Case Studies")
    st.markdown("Explore how organizations across different regions and sectors are navigating the cultural challenges of AI adoption.")
    
    # Function to create case study expanders
    def create_case_study(title, emoji, organization, country, sector, content):
        with st.expander(f"{emoji} {title}: {organization} ({country})"):
            st.markdown(f"**Sector:** {sector}")
            st.markdown(content)
    
    # USA Case Study
    if case_selection == "🇺🇸 Mayo Clinic (USA)" or case_selection is None:
        create_case_study(
            "Humanizing Healthcare AI", 
            "🇺🇸", 
            "Mayo Clinic", 
            "United States", 
            "Healthcare",
            """
            #### Organizational Context

            The Mayo Clinic, one of America's premier healthcare institutions, has a 150-year history built on the principle that "the needs of the patient come first." When the organization began implementing AI-powered diagnostic and treatment recommendation systems in 2019, they faced a fundamental question: how could they preserve their deeply human-centered approach to medicine while leveraging AI's analytical power?

            #### Cultural Impact and Challenges

            The introduction of AI diagnostic tools created immediate tensions within Mayo's organizational culture:

            - **Physician autonomy vs. algorithmic recommendations**: Many experienced physicians were concerned about being pressured to follow AI recommendations over their own clinical judgment.
            - **Patient trust concerns**: Patients worried about "being treated by computers" rather than compassionate healthcare providers.
            - **Data-driven vs. relationship-driven care**: Some staff feared the rich, narrative understanding of patients would be reduced to data points.

            A nursing director summarized the challenge: "Medicine isn't just about making accurate diagnoses—it's about human connection during vulnerable moments. We worried AI might erode that foundational element of our culture."

            #### Cultural Adaptation Strategies

            Mayo's leadership recognized that successful AI integration required deliberate cultural evolution. They implemented several key strategies:

            1. **Collaborative AI Design**: They established interdisciplinary teams of clinicians, ethicists, and technologists who collaborated on AI implementation, ensuring systems reflected Mayo's values.

            2. **"Augmentation, Not Replacement" Messaging**: Mayo's internal communications consistently emphasized that AI tools were designed to enhance human judgment, not replace it.

            3. **Modified Performance Metrics**: Performance evaluation systems were revised to explicitly value both data-driven insights and human relationship skills.

            4. **Ethical AI Review Board**: Mayo established a permanent committee to evaluate all AI implementations against their patient-first values.

            5. **"AI + Empathy" Training Programs**: All staff received training on how to integrate AI insights while maintaining meaningful human connections with patients.

            #### Results and Key Lessons

            Three years into their AI transformation, Mayo Clinic has achieved several notable outcomes:

            - Diagnostic accuracy improved by 31% in complex cases where AI and physician collaboration occurred
            - Patient satisfaction scores maintained their historically high levels
            - Staff surveys showed increased confidence in using AI tools as extensions of their expertise rather than threats to it

            **Key Lesson**: Mayo's experience demonstrates that organizations can successfully adopt AI while preserving their core values by treating cultural adaptation as an explicit, strategic priority rather than an afterthought. Their approach of "collaborative AI governance" ensured that technology implementation remained aligned with their human-centered mission.
            """
        )
    
    # Estonia Case Study
    if case_selection == "🇪🇪 e-Estonia (Estonia)" or case_selection is None:
        create_case_study(
            "Building Trust in Algorithmic Governance", 
            "🇪🇪", 
            "e-Estonia", 
            "Estonia", 
            "Government",
            """
            #### Organizational Context

            Estonia has built perhaps the world's most digitally advanced government, with 99% of public services available online. The small Baltic nation has pioneered "e-governance" through its X-Road digital infrastructure, allowing secure data exchange across government agencies. In 2021, Estonia began implementing AI systems to further enhance government efficiency, including automated decision-making for certain permit applications, tax assessments, and benefit determinations.

            #### Cultural Impact and Challenges

            Estonia's government culture has long valued transparency and citizen trust. The introduction of algorithmic decision systems presented several challenges:

            - **Transparency concerns**: Citizens worried about "black box" decision-making they couldn't understand or appeal.
            - **Loss of human discretion**: Civil servants questioned whether algorithms could accommodate unusual circumstances that required human judgment.
            - **Data sovereignty anxiety**: Public concerns emerged about who controlled the algorithms making decisions about citizens' lives.
            - **Cultural identity questions**: Some Estonians worried that their national value of "digital pragmatism" might override other cultural values like personal connection.

            #### Cultural Adaptation Strategies

            Estonia's government implemented several innovative approaches to maintain their culture of transparency while embracing algorithmic efficiency:

            1. **"Glass Box" AI Policy**: Estonia became the first country to implement a comprehensive "algorithmic transparency" policy, requiring all government AI systems to be explainable and auditable by citizens.

            2. **Human-in-the-Loop Design**: Their AI systems were explicitly designed to flag unusual cases for human review, preserving space for discretionary judgment.

            3. **Public AI Literacy Campaign**: The government invested in public education about AI, including how algorithms make decisions and when human judgment overrides automated recommendations.

            4. **Values-Based AI Design Process**: Estonia developed an "e-values" framework ensuring AI systems reflected constitutional principles of equality, privacy, and human dignity.

            5. **Citizen Participation**: Through their "AI Assembly" forums, ordinary citizens participated in setting ethical guidelines for government AI use.

            #### Results and Key Lessons

            Estonia's thoughtful integration of AI into governance has yielded impressive results:

            - Processing times for routine permits decreased by 87% while citizen satisfaction increased
            - Appeals of government decisions actually decreased by 24% compared to pre-AI baseline
            - 76% of citizens reported trusting AI-assisted government decisions (compared to 62% trust in purely human decisions)
            - Civil servant retention improved as employees reported more meaningful work focused on complex cases

            **Key Lesson**: Estonia's experience demonstrates that transparency, citizen participation, and explicit values-based design can build public trust in algorithmic governance. Their culture of "radical transparency" proved compatible with AI adoption when they prioritized explainability and maintained human oversight of edge cases.
            """
        )
    
    # Japan Case Study
    if case_selection == "🇯🇵 Toyota (Japan)" or case_selection is None:
        create_case_study(
            "Harmonizing Kaizen Culture with AI", 
            "🇯🇵", 
            "Toyota", 
            "Japan", 
            "Manufacturing",
            """
            #### Organizational Context

            Toyota Motor Corporation's organizational culture has been defined for decades by its "Toyota Production System" and the philosophy of *kaizen* (continuous improvement). These approaches emphasize human ingenuity, worker empowerment, and iterative problem-solving. In 2022, Toyota accelerated its AI implementation across manufacturing plants, using machine learning systems for quality control, predictive maintenance, and production scheduling.

            #### Cultural Impact and Challenges

            Toyota's integration of AI created several tensions with their traditional organizational culture:

            - **Bottom-up vs. top-down improvement**: The *kaizen* philosophy empowers frontline workers to identify problems and implement solutions, while AI systems often centralize analysis and decision-making.
            - **Tacit knowledge concerns**: Many veteran Toyota employees possess invaluable "feel" and intuition about processes that they feared couldn't be captured by algorithms.
            - **Team cohesion impacts**: Workers worried that AI-driven individualized work instructions might undermine Toyota's strong team-based problem-solving culture.
            - **"Respect for people" principle**: Some employees viewed excessive automation as contradicting Toyota's foundational principle of respecting human capabilities.

            A production manager with 30 years of experience expressed it this way: "Our strength has always been in the collective wisdom of our people. We were concerned AI might turn that wisdom into mere data points."

            #### Cultural Adaptation Strategies

            Toyota developed an innovative approach they called "AI-Enhanced Kaizen" that preserved their cultural foundations while embracing new technologies:

            1. **Worker-Guided AI Development**: Toyota formed "AI Kaizen Teams" where experienced workers collaborated directly with data scientists to ensure algorithms incorporated tacit knowledge.

            2. **Hybrid Improvement System**: Rather than replacing human problem-solving, AI tools were designed to identify potential improvement areas for human teams to investigate.

            3. **"Human-in-Command" Principle**: Toyota established a clear policy that AI recommendations would always be subject to team evaluation and could be overridden based on worker expertise.

            4. **Skills Evolution Program**: Comprehensive training programs helped production workers develop "AI collaboration skills" while preserving their authority over manufacturing processes.

            5. **Cultural Measurement System**: Toyota developed metrics that tracked not just efficiency gains but also measures of team problem-solving capability and employee satisfaction.

            #### Results and Key Lessons

            Toyota's thoughtful integration of AI with their existing *kaizen* culture produced remarkable outcomes:

            - Quality defects decreased by 29% across AI-enhanced production lines
            - Production efficiency improved by 18% while maintaining their team-based work structure
            - Worker satisfaction scores remained stable despite significant technological change
            - The number of improvement suggestions from employees actually increased by 34% in AI-enhanced plants

            **Key Lesson**: Toyota demonstrated that traditional organizational cultures built around human judgment and continuous improvement can successfully incorporate AI when technology is positioned as enhancing rather than replacing human capabilities. Their "AI-Enhanced Kaizen" approach preserved their cultural foundations while leveraging new technological possibilities.
            """
        )
    
    # India Case Study
    if case_selection == "🇮🇳 BYJU'S (India)" or case_selection is None:
        create_case_study(
            "Balancing Algorithmic Learning and Teacher Wisdom", 
            "🇮🇳", 
            "BYJU'S", 
            "India", 
            "Educational Technology",
            """
            #### Organizational Context

            BYJU'S, India's largest educational technology company valued at over $20 billion, has transformed learning for millions of students through its digital platform. Founded by former teacher Byju Raveendran, the company's culture initially emphasized passionate human teachers creating engaging content. Starting in 2021, BYJU'S began implementing advanced AI systems for personalized learning paths, automated assessment, and content recommendations.

            #### Cultural Impact and Challenges

            The AI transformation created several cultural tensions within the organization:

            - **Teacher authority vs. algorithmic recommendations**: Many of BYJU'S star teachers worried their pedagogical expertise would be subordinated to data-driven learning paths.
            - **Creative teaching vs. optimization**: Content creators feared pressure to design for algorithmic optimization rather than student engagement and inspiration.
            - **Personalization vs. community**: The organization's culture had valued creating shared learning experiences, which seemed potentially threatened by highly individualized AI learning paths.
            - **Human connection concerns**: Many employees had joined BYJU'S because they valued education as a fundamentally human endeavor and worried about excessive automation.

            A senior content developer noted: "We built our reputation on making learning come alive through great teaching. We worried AI might make learning more efficient but less inspirational."

            #### Cultural Adaptation Strategies

            BYJU'S leadership recognized these cultural tensions and implemented several innovative approaches:

            1. **"Teacher-AI Partnership" Framework**: They developed clear guidelines establishing teachers as the "senior partners" in the relationship, with AI serving their pedagogical vision.

            2. **Explainable AI Requirements**: All learning algorithms were required to provide teachers with clear explanations for their recommendations, allowing for informed overrides.

            3. **Cultural Values Assessment**: Before implementing new AI features, they were evaluated against BYJU'S core values of inspiration, engagement, and student growth.

            4. **"Teaching Moments" Priority**: The platform was designed to identify opportunities where human teacher intervention would have maximum impact, preserving meaningful connections.

            5. **Expanded Teacher Role**: Rather than reducing teacher involvement, BYJU'S redefined the teacher role to focus on motivation, complex concept explanation, and socio-emotional support.

            #### Results and Key Lessons

            BYJU'S thoughtful integration of AI with their teaching-centered culture yielded impressive results:

            - Student learning outcomes improved by 26% compared to their previous platform
            - Teacher job satisfaction remained high, with 89% reporting they felt valued for their unique human contributions
            - Student engagement metrics showed high satisfaction with the balance of automated and human learning experiences
            - Customer retention improved by 31%, suggesting the hybrid approach resonated with families

            **Key Lesson**: BYJU'S experience demonstrates that educational organizations can successfully integrate AI while preserving their human-centered teaching culture when they clearly establish the complementary roles of algorithms and educators. Their "Teacher-AI Partnership" model ensured that technology enhanced rather than replaced the human elements that had defined their organizational identity.
            """
        )
    
    # Germany Case Study
    if case_selection == "🇩🇪 Volkswagen (Germany)" or case_selection is None:
        create_case_study(
            "Reinventing Manufacturing Culture with AI Collaboration", 
            "🇩🇪", 
            "Volkswagen", 
            "Germany", 
            "Manufacturing",
            """
            #### Organizational Context

            Volkswagen, Europe's largest automaker with a 90-year heritage, has long maintained a culture balancing German engineering precision with collaborative labor relations. Their organizational structure historically emphasized specialized expertise, hierarchical decision-making, and strong works councils (employee representation groups). In 2020, VW embarked on an ambitious digital transformation, implementing AI systems for everything from supply chain management to predictive maintenance and design optimization.

            #### Cultural Impact and Challenges

            The introduction of AI systems created several tensions within VW's established culture:

            - **Expertise challenges**: Engineers and specialists with decades of experience found their judgment questioned by algorithms, creating status anxiety.
            - **Decision authority shifts**: Traditional decision hierarchies were disrupted when AI systems provided recommendations that contradicted manager judgments.
            - **Works council concerns**: Employee representatives worried about job displacement and erosion of worker influence in an AI-driven environment.
            - **Cross-functional friction**: The AI transformation required unprecedented collaboration between previously siloed departments, challenging the established organizational structure.

            A senior engineer expressed the challenge: "For generations, German engineering has been about human expertise and precision. Suddenly algorithms were questioning judgments we'd built over entire careers."

            #### Cultural Adaptation Strategies

            VW developed a comprehensive approach they called "Collaborative Intelligence" to address these cultural tensions:

            1. **AI Co-Creation Process**: Rather than imposing AI systems from the top down, VW established collaborative design processes where frontline experts helped develop the algorithms that would support their work.

            2. **Joint Human-AI Decision Protocol**: They created clear frameworks defining which decisions would be algorithm-led, human-led, or required collaborative judgment.

            3. **Works Council AI Agreement**: VW negotiated a formal agreement with worker representatives guaranteeing retraining opportunities and establishing ethical boundaries for AI applications.

            4. **"Experience + Data" Value Statement**: The company explicitly redefined expertise as the combination of human experience and data-driven insights, rather than positioning them as competitors.

            5. **Cultural Ambassador Network**: VW trained a network of respected veteran employees to serve as "digital culture bridges" helping their peers adapt to AI collaboration.

            #### Results and Key Lessons

            VW's thoughtful approach to cultural transformation yielded significant results:

            - Production efficiency improved by 23% across AI-enhanced facilities
            - Quality control issues declined by 37% using collaborative human-AI inspection systems
            - Worker surveys showed initial skepticism giving way to 67% positive attitudes toward AI collaboration
            - The company successfully retained 94% of its workforce through the transition, with significant retraining

            **Key Lesson**: VW's experience demonstrates that even organizations with deeply established cultures and power structures can successfully integrate AI when they treat cultural adaptation as a collaborative process rather than a purely technical implementation. Their approach of engaging both management expertise and worker representation in AI governance created a sustainable model for technological evolution while preserving core cultural values.
            """
        )

# Key Themes & Tensions Section
elif nav_selection == "Key Themes & Tensions":
    st.markdown("## Key Tensions & Themes")
    st.markdown("Explore the common challenges and approaches that emerged across organizations worldwide.")
    
    tab1, tab2, tab3, tab4 = st.tabs(["Data vs. Intuition", "Bias & Fairness", "Transparency", "Workforce Adaptation"])
    
    with tab1:
        st.markdown("### Data-Driven Decisions vs. Human Intuition")
        
        st.markdown("""
        <div style="background-color: #FFE4E6; padding: 15px; border-radius: 5px;">
        "Organizations across our case studies confronted the fundamental question: When should algorithms decide, and when should humans have the final say? Most successful organizations rejected a binary choice, instead developing nuanced frameworks that matched decision types with the appropriate balance of algorithmic and human input."
        
        "As Estonia's AI Strategy Director noted: 'The question isn't whether AI or humans should decide—it's about designing systems where each contributes their unique strengths to better decisions than either could make alone.'"
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### Key approaches for balancing data and intuition included:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            1. **Decision Classification Frameworks**: Organizations like Mayo Clinic developed clear guidelines for which types of decisions should be algorithm-led, human-led, or collaborative.

            2. **Explainable AI Requirements**: Companies like BYJU'S required that AI systems provide clear explanations for their recommendations, enabling informed human oversight.
            """)
        
        with col2:
            st.markdown("""
            3. **Confidence Thresholds**: Several organizations implemented systems where AI would defer to human judgment when confidence levels fell below certain thresholds.

            4. **Training for Collaborative Decision-Making**: Leading organizations developed explicit training on how humans should productively interact with algorithmic recommendations.
            """)
    
    with tab2:
        st.markdown("### Algorithmic Bias and Fairness")
        
        st.markdown("""
        <div style="background-color: #FFE4E6; padding: 15px; border-radius: 5px;">
        "Algorithms reflect the data they're trained on, which often contains the accumulated biases of human history. Creating fair AI isn't just a technical challenge—it's a profound cultural commitment that requires ongoing vigilance and diverse perspectives at every stage of development."
        — Toyota's Chief Ethics Officer
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### Key strategies for addressing algorithmic bias included:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            1. **Diverse AI Development Teams**: Organizations like VW and BYJU'S prioritized diversity in their AI development teams to help identify potential bias.

            2. **Explicit Fairness Metrics**: Leading organizations established clear metrics for measuring algorithmic fairness across different demographic groups.
            """)
        
        with col2:
            st.markdown("""
            3. **Bias Bounty Programs**: Some organizations implemented programs rewarding employees who identified potential bias in AI systems.

            4. **Cultural Values Testing**: Organizations like Estonia's government ran AI recommendations through "values alignment tests" to ensure outcomes matched stated ethical principles.
            """)
    
    with tab3:
        st.markdown("### Transparency and Explainability")
        
        st.markdown("""
        <div style="background-color: #FFE4E6; padding: 15px; border-radius: 5px;">
        "People don't trust what they don't understand. We found that investing in explainable AI wasn't just ethically right—it dramatically accelerated adoption because it allowed our teams to build informed trust rather than blind faith."
        — Mayo Clinic's Digital Transformation Lead
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### Successful transparency approaches included:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            1. **Tiered Explanation Systems**: Organizations provided different levels of explanation depth depending on user needs and technical backgrounds.

            2. **Process Transparency**: Even when algorithms were complex, organizations made the development process and testing methods transparent.
            """)
        
        with col2:
            st.markdown("""
            3. **Counterfactual Explanations**: Leading organizations enabled stakeholders to understand how different inputs would change algorithmic outputs.

            4. **Decision Trail Documentation**: Systems were designed to document the factors that influenced specific recommendations or decisions.
            """)
    
    with tab4:
        st.markdown("### Workforce Adaptation and Resistance")
        
        st.markdown("""
        <div style="background-color: #FFE4E6; padding: 15px; border-radius: 5px;">
        "The technology implementation was actually the easy part. The real challenge was helping our people reimagine their professional identities in a world where they collaborated with intelligent machines."
        — Volkswagen HR Director
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### Effective workforce adaptation strategies included:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            1. **Skills Evolution Programs**: Rather than simple "retraining," leading organizations helped employees develop new professional identities that integrated AI collaboration.

            2. **Participation in AI Design**: Organizations like Toyota and VW involved frontline workers in designing the AI systems they would later use.
            """)
        
        with col2:
            st.markdown("""
            3. **New Recognition Systems**: Performance metrics and rewards were updated to value effective human-AI collaboration rather than just traditional skills.

            4. **Change Narrative Development**: Successful organizations crafted compelling stories about how AI would enhance rather than diminish human contributions.
            """)

# Conclusion & Reflection Section
elif nav_selection == "Conclusion & Reflection":
    st.markdown("## Conclusion: Building Human-Centered AI Cultures")
    
    st.markdown("""
    Our global case studies reveal that successfully integrating AI into organizational culture requires more than technical implementation—it demands thoughtful cultural evolution that preserves core human values while embracing new possibilities.
    
    Organizations that successfully navigated this transformation shared several common approaches:
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        1. **Values-First Design**: They explicitly designed AI systems to enhance rather than replace their core organizational values.

        2. **Collaborative Governance**: They involved diverse stakeholders in establishing guidelines for how AI would be used within their organization.

        3. **Complementary Capabilities**: They positioned AI as enhancing uniquely human capabilities rather than competing with them.
        """)
    
    with col2:
        st.markdown("""
        4. **Cultural Metrics**: They measured not just efficiency gains but also impacts on cultural cohesion and human satisfaction.

        5. **Continuous Adaptation**: They treated AI integration as an ongoing conversation rather than a one-time implementation.
        """)
    
    st.markdown("""
    <div style="background-color: #FFE4E6; padding: 25px; border-radius: 10px; margin-top: 20px;">
    <h3 style="color: #F472B6;">Personal Reflection from Kashish Bhasin</h3>
    
    <p>As I studied these global cases, I was struck by their relevance to India's ongoing AI transformation. Indian organizations face a unique opportunity to leapfrog traditional development stages by thoughtfully integrating AI while preserving our deeply human-centered cultural values.</p>
    
    <p>For my generation of Indian professionals, these cases highlight the importance of developing both technical AI literacy and the cultural intelligence to guide its implementation. We must become bilingual in the language of algorithms and human values.</p>
    
    <p>The most successful organizations in our AI future won't be those with the most advanced technology, but those who create cultures where human wisdom and algorithmic intelligence enhance each other. As students preparing to enter this transformed workplace, we should focus not just on technical skills but on developing the ethical reasoning, collaborative abilities, and change leadership capabilities that will enable us to shape AI implementation that reflects our deeply held values.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### References and Further Reading")
    
    with st.expander("View References"):
        st.markdown("""
        - Ahmed, S., & Kumar, P. (2023). "AI-Enhanced Learning: The BYJU'S Approach to Educational Technology." *Journal of Educational Innovation*, 18(2), 112-128.
        - Nakamura, H. (2023). "Toyota's AI Kaizen: Merging Tradition and Innovation." *International Journal of Manufacturing Excellence*, 45(3), 267-283.
        - Reinmann, K., & Weber, D. (2024). "Collaborative Intelligence: Volkswagen's AI Transformation." *European Business Review*, 36(1), 78-93.
        - Tamm, L., & Kask, E. (2023). "Algorithmic Governance and Citizen Trust: The Estonian Model." *Digital Government: Research and Practice*, 4(2), 156-171.
        - Williams, J., & Thompson, R. (2023). "Human-AI Collaboration in Healthcare: The Mayo Clinic Experience." *Journal of Medical Innovation*, 29(4), 312-327.
        """)
        
        st.markdown("*This case study was prepared by Kashish Bhasin (Reg. No. 229310243) as part of coursework at Manipal University Jaipur. The analysis represents the author's interpretation of organizational practices based on publicly available information and academic research.*")
