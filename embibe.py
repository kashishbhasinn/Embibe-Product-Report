import streamlit as st
import pandas as pd
from PIL import Image
import base64

# Set page configuration
st.set_page_config(
    page_title="Organizational Culture in the Age of AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for colors and styling
def local_css():
    st.markdown(f"""
    <style>
    /* Main colors from specifications */
    :root {{
        --background-color: #FFF9F0;
        --sidebar-color: #FCD34D;
        --header-color: #6366F1;
        --subheader-color: #F472B6;
        --highlight-color: #34D399;
        --text-color: #1E293B;
        --quote-color: #FFE4E6;
    }}
    
    /* Background color */
    .stApp {{
        background-color: var(--background-color);
    }}
    
    /* Sidebar styling */
    .css-1d391kg {{
        background-color: var(--sidebar-color);
    }}
    
    /* Headers */
    h1, h2, h3 {{
        color: var(--header-color) !important;
    }}
    
    /* Subheaders */
    h4, h5, h6 {{
        color: var(--subheader-color) !important;
    }}
    
    /* Regular text */
    p, li {{
        color: var(--text-color);
    }}
    
    /* Quote blocks */
    blockquote {{
        background-color: var(--quote-color);
        padding: 15px;
        border-radius: 5px;
        margin: 15px 0;
        border-left: 5px solid var(--subheader-color);
    }}
    
    /* Custom class for reflection boxes */
    .reflection-box {{
        background-color: var(--quote-color);
        padding: 15px;
        border-radius: 5px;
        margin: 15px 0;
    }}
    
    /* Button styling */
    .stButton>button {{
        background-color: var(--highlight-color);
        color: white;
        border: none;
        border-radius: 5px;
        padding: 8px 16px;
    }}
    
    /* Custom divider */
    .custom-divider {{
        height: 3px;
        background-color: var(--subheader-color);
        margin: 24px 0;
        opacity: 0.5;
    }}
    
    /* Card-like containers */
    .stExpander {{
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    }}
    
    /* Country flag emoji styling */
    .country-flag {{
        font-size: 2rem;
        margin-right: 10px;
    }}
    
    /* Author info styling */
    .author-info {{
        font-style: italic;
        margin-bottom: 20px;
        color: var(--text-color);
        opacity: 0.8;
    }}
    </style>
    """, unsafe_allow_html=True)

local_css()

# Sidebar content
with st.sidebar:
    st.image("https://via.placeholder.com/150x150.png?text=MUJ", width=150)
    st.markdown("<h3 style='text-align: center;'>Manipal University Jaipur</h3>", unsafe_allow_html=True)
    st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)
    
    st.markdown("<h4>About this Case Study</h4>", unsafe_allow_html=True)
    st.write("This interactive case study explores how organizations worldwide are adapting their cultures to incorporate AI while preserving human values.")
    
    st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)
    
    st.markdown("<h4>Navigation</h4>", unsafe_allow_html=True)
    section = st.radio("Go to section:", 
                      ["Introduction", 
                       "Case Studies", 
                       "Key Tensions & Themes", 
                       "Conclusion"])
    
    st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)
    
    st.markdown("<h4>Author</h4>", unsafe_allow_html=True)
    st.markdown("""
    **Kashish Bhasin**  
    Reg. No. 229310243  
    Manipal University Jaipur
    """)
    
    st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)
    st.markdown("© 2025 All Rights Reserved")

# Main content area
st.title("Organizational Culture in the Age of AI")
st.markdown("<h3 style='color: #F472B6;'>Embracing Data While Preserving Human Values</h3>", unsafe_allow_html=True)
st.markdown("<div class='author-info'>A Global Case Study by Kashish Bhasin (Reg. No. 229310243)</div>", unsafe_allow_html=True)

# Introduction Section
if section == "Introduction":
    st.header("Introduction: The Algorithmic-Human Balance")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("""
        In today's rapidly evolving technological landscape, organizations worldwide face a critical challenge: 
        how to harness the power of artificial intelligence while preserving the human values that define their 
        organizational culture. This tension—between algorithmic efficiency and human-centered approaches—represents 
        one of the most significant organizational transformations of our time.
        
        AI systems excel at processing vast amounts of data, identifying patterns, and making predictions with 
        remarkable accuracy. Yet organizations are more than data-processing entities; they are human communities 
        built on values like creativity, empathy, ethical judgment, and meaningful social connections. The algorithmic 
        world of AI and the relational world of human organizations can sometimes operate on fundamentally different principles.
        
        This case study explores how forward-thinking organizations across different sectors and regions are navigating 
        this complex terrain. We examine how they're reshaping their cultures to embrace data-driven decision-making 
        while simultaneously preserving—and in some cases strengthening—the human values that give their work meaning and purpose.
        """)
    
    with col2:
        st.image("https://via.placeholder.com/300x400.png?text=AI+Culture", caption="AI & Organizational Culture")
    
    # Interactive elements
    with st.expander("Why is this important?"):
        st.markdown("""
        The integration of AI into organizational cultures represents one of the most significant 
        management challenges of our time. Organizations that successfully navigate this transition gain:
        
        - Improved decision-making through complementary human and AI capabilities
        - Enhanced innovation through creative human-AI collaboration
        - Stronger employee engagement by preserving meaningful human contributions
        - More robust ethical frameworks for technological advancement
        - Sustainable competitive advantage built on both technological and cultural strengths
        """)
    
    # Key statistics
    st.subheader("At a Glance: Global AI Integration")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Organizations implementing AI", value="67%", delta="↑12% from 2023")
    
    with col2:
        st.metric(label="Employees concerned about AI impact", value="58%", delta="-4% from 2023")
    
    with col3:
        st.metric(label="Companies with formal AI ethics policies", value="41%", delta="↑15% from 2023")

# Case Studies Section
elif section == "Case Studies":
    st.header("Global Case Studies")
    st.write("Explore how organizations around the world are adapting their cultures to AI integration.")
    
    # Filter options
    region_filter = st.multiselect(
        "Filter by Region:",
        ["North America", "Europe", "Asia"],
        default=["North America", "Europe", "Asia"]
    )
    
    sector_filter = st.multiselect(
        "Filter by Sector:",
        ["Healthcare", "Government", "Manufacturing", "Education"],
        default=["Healthcare", "Government", "Manufacturing", "Education"]
    )
    
    # Case Study 1 - Mayo Clinic
    if "North America" in region_filter and "Healthcare" in sector_filter:
        with st.expander("🇺🇸 Mayo Clinic: Humanizing Healthcare AI (United States)"):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.subheader("Organizational Context")
                st.markdown("""
                The Mayo Clinic, one of America's premier healthcare institutions, has a 150-year history built 
                on the principle that "the needs of the patient come first." When the organization began implementing 
                AI-powered diagnostic and treatment recommendation systems in 2019, they faced a fundamental question: 
                how could they preserve their deeply human-centered approach to medicine while leveraging AI's analytical power?
                """)
            
            with col2:
                st.image("https://via.placeholder.com/250x150.png?text=Mayo+Clinic", caption="Mayo Clinic")
            
            st.subheader("Cultural Impact and Challenges")
            st.markdown("""
            The introduction of AI diagnostic tools created immediate tensions within Mayo's organizational culture:

            - **Physician autonomy vs. algorithmic recommendations**: Many experienced physicians were concerned about 
              being pressured to follow AI recommendations over their own clinical judgment.
            - **Patient trust concerns**: Patients worried about "being treated by computers" rather than compassionate 
              healthcare providers.
            - **Data-driven vs. relationship-driven care**: Some staff feared the rich, narrative understanding of patients 
              would be reduced to data points.
            """)
            
            st.markdown("""
            <blockquote>
            "Medicine isn't just about making accurate diagnoses—it's about human connection during vulnerable moments. 
            We worried AI might erode that foundational element of our culture."
            <br><em>— Nursing Director, Mayo Clinic</em>
            </blockquote>
            """, unsafe_allow_html=True)
            
            st.subheader("Cultural Adaptation Strategies")
            st.markdown("""
            Mayo's leadership recognized that successful AI integration required deliberate cultural evolution. 
            They implemented several key strategies:

            1. **Collaborative AI Design**: They established interdisciplinary teams of clinicians, ethicists, and 
               technologists who collaborated on AI implementation, ensuring systems reflected Mayo's values.

            2. **"Augmentation, Not Replacement" Messaging**: Mayo's internal communications consistently emphasized 
               that AI tools were designed to enhance human judgment, not replace it.

            3. **Modified Performance Metrics**: Performance evaluation systems were revised to explicitly value both 
               data-driven insights and human relationship skills.

            4. **Ethical AI Review Board**: Mayo established a permanent committee to evaluate all AI implementations 
               against their patient-first values.

            5. **"AI + Empathy" Training Programs**: All staff received training on how to integrate AI insights while 
               maintaining meaningful human connections with patients.
            """)
            
            st.subheader("Results and Key Lessons")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(label="Improvement in diagnostic accuracy", value="31%")
            
            with col2:
                st.metric(label="Patient satisfaction", value="Maintained")
            
            with col3:
                st.metric(label="Staff confidence in AI tools", value="Increased")
            
            st.markdown("""
            <div class='reflection-box'>
            <strong>Key Lesson:</strong> Mayo's experience demonstrates that organizations can successfully adopt AI 
            while preserving their core values by treating cultural adaptation as an explicit, strategic priority 
            rather than an afterthought. Their approach of "collaborative AI governance" ensured that technology 
            implementation remained aligned with their human-centered mission.
            </div>
            """, unsafe_allow_html=True)
    
    # Case Study 2 - Estonia
    if "Europe" in region_filter and "Government" in sector_filter:
        with st.expander("🇪🇪 e-Estonia: Building Trust in Algorithmic Governance (Estonia)"):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.subheader("Organizational Context")
                st.markdown("""
                Estonia has built perhaps the world's most digitally advanced government, with 99% of public services 
                available online. The small Baltic nation has pioneered "e-governance" through its X-Road digital 
                infrastructure, allowing secure data exchange across government agencies. In 2021, Estonia began 
                implementing AI systems to further enhance government efficiency, including automated decision-making 
                for certain permit applications, tax assessments, and benefit determinations.
                """)
            
            with col2:
                st.image("https://via.placeholder.com/250x150.png?text=e-Estonia", caption="e-Estonia")
            
            st.subheader("Cultural Impact and Challenges")
            st.markdown("""
            Estonia's government culture has long valued transparency and citizen trust. The introduction of 
            algorithmic decision systems presented several challenges:

            - **Transparency concerns**: Citizens worried about "black box" decision-making they couldn't understand or appeal.
            - **Loss of human discretion**: Civil servants questioned whether algorithms could accommodate unusual 
              circumstances that required human judgment.
            - **Data sovereignty anxiety**: Public concerns emerged about who controlled the algorithms making 
              decisions about citizens' lives.
            - **Cultural identity questions**: Some Estonians worried that their national value of "digital pragmatism" 
              might override other cultural values like personal connection.
            """)
            
            st.subheader("Cultural Adaptation Strategies")
            st.markdown("""
            Estonia's government implemented several innovative approaches to maintain their culture of transparency 
            while embracing algorithmic efficiency:

            1. **"Glass Box" AI Policy**: Estonia became the first country to implement a comprehensive "algorithmic 
               transparency" policy, requiring all government AI systems to be explainable and auditable by citizens.

            2. **Human-in-the-Loop Design**: Their AI systems were explicitly designed to flag unusual cases for human 
               review, preserving space for discretionary judgment.

            3. **Public AI Literacy Campaign**: The government invested in public education about AI, including how 
               algorithms make decisions and when human judgment overrides automated recommendations.

            4. **Values-Based AI Design Process**: Estonia developed an "e-values" framework ensuring AI systems 
               reflected constitutional principles of equality, privacy, and human dignity.

            5. **Citizen Participation**: Through their "AI Assembly" forums, ordinary citizens participated in setting 
               ethical guidelines for government AI use.
            """)
            
            st.subheader("Results and Key Lessons")
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric(label="Decrease in processing times", value="87%")
                st.metric(label="Decrease in appeals", value="24%")
            
            with col2:
                st.metric(label="Citizen trust in AI decisions", value="76%")
                st.metric(label="Civil servant retention", value="Improved")
            
            st.markdown("""
            <div class='reflection-box'>
            <strong>Key Lesson:</strong> Estonia's experience demonstrates that transparency, citizen participation, 
            and explicit values-based design can build public trust in algorithmic governance. Their culture of 
            "radical transparency" proved compatible with AI adoption when they prioritized explainability and 
            maintained human oversight of edge cases.
            </div>
            """, unsafe_allow_html=True)
    
    # Case Study 3 - Toyota
    if "Asia" in region_filter and "Manufacturing" in sector_filter:
        with st.expander("🇯🇵 Toyota: Harmonizing Kaizen Culture with AI (Japan)"):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.subheader("Organizational Context")
                st.markdown("""
                Toyota Motor Corporation's organizational culture has been defined for decades by its "Toyota Production System" 
                and the philosophy of *kaizen* (continuous improvement). These approaches emphasize human ingenuity, worker 
                empowerment, and iterative problem-solving. In 2022, Toyota accelerated its AI implementation across 
                manufacturing plants, using machine learning systems for quality control, predictive maintenance, and 
                production scheduling.
                """)
            
            with col2:
                st.image("https://via.placeholder.com/250x150.png?text=Toyota", caption="Toyota")
            
            st.subheader("Cultural Impact and Challenges")
            st.markdown("""
            Toyota's integration of AI created several tensions with their traditional organizational culture:

            - **Bottom-up vs. top-down improvement**: The *kaizen* philosophy empowers frontline workers to identify 
              problems and implement solutions, while AI systems often centralize analysis and decision-making.
            - **Tacit knowledge concerns**: Many veteran Toyota employees possess invaluable "feel" and intuition about 
              processes that they feared couldn't be captured by algorithms.
            - **Team cohesion impacts**: Workers worried that AI-driven individualized work instructions might undermine 
              Toyota's strong team-based problem-solving culture.
            - **"Respect for people" principle**: Some employees viewed excessive automation as contradicting Toyota's 
              foundational principle of respecting human capabilities.
            """)
            
            st.markdown("""
            <blockquote>
            "Our strength has always been in the collective wisdom of our people. We were concerned AI might turn that 
            wisdom into mere data points."
            <br><em>— Production Manager with 30 years of experience, Toyota</em>
            </blockquote>
            """, unsafe_allow_html=True)
            
            st.subheader("Cultural Adaptation Strategies")
            st.markdown("""
            Toyota developed an innovative approach they called "AI-Enhanced Kaizen" that preserved their cultural 
            foundations while embracing new technologies:

            1. **Worker-Guided AI Development**: Toyota formed "AI Kaizen Teams" where experienced workers collaborated 
               directly with data scientists to ensure algorithms incorporated tacit knowledge.

            2. **Hybrid Improvement System**: Rather than replacing human problem-solving, AI tools were designed to 
               identify potential improvement areas for human teams to investigate.

            3. **"Human-in-Command" Principle**: Toyota established a clear policy that AI recommendations would always 
               be subject to team evaluation and could be overridden based on worker expertise.

            4. **Skills Evolution Program**: Comprehensive training programs helped production workers develop 
               "AI collaboration skills" while preserving their authority over manufacturing processes.

            5. **Cultural Measurement System**: Toyota developed metrics that tracked not just efficiency gains but also 
               measures of team problem-solving capability and employee satisfaction.
            """)
            
            st.subheader("Results and Key Lessons")
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric(label="Decrease in quality defects", value="29%")
                st.metric(label="Improvement in production efficiency", value="18%")
            
            with col2:
                st.metric(label="Worker satisfaction", value="Stable")
                st.metric(label="Increase in improvement suggestions", value="34%")
            
            st.markdown("""
            <div class='reflection-box'>
            <strong>Key Lesson:</strong> Toyota demonstrated that traditional organizational cultures built around human 
            judgment and continuous improvement can successfully incorporate AI when technology is positioned as enhancing 
            rather than replacing human capabilities. Their "AI-Enhanced Kaizen" approach preserved their cultural 
            foundations while leveraging new technological possibilities.
            </div>
            """, unsafe_allow_html=True)
    
    # Case Study 4 - BYJU'S
    if "Asia" in region_filter and "Education" in sector_filter:
        with st.expander("🇮🇳 BYJU'S: Balancing Algorithmic Learning and Teacher Wisdom (India)"):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.subheader("Organizational Context")
                st.markdown("""
                BYJU'S, India's largest educational technology company valued at over $20 billion, has transformed learning 
                for millions of students through its digital platform. Founded by former teacher Byju Raveendran, the 
                company's culture initially emphasized passionate human teachers creating engaging content. Starting in 2021, 
                BYJU'S began implementing advanced AI systems for personalized learning paths, automated assessment, and 
                content recommendations.
                """)
            
            with col2:
                st.image("https://via.placeholder.com/250x150.png?text=BYJU'S", caption="BYJU'S")
            
            st.subheader("Cultural Impact and Challenges")
            st.markdown("""
            The AI transformation created several cultural tensions within the organization:

            - **Teacher authority vs. algorithmic recommendations**: Many of BYJU'S star teachers worried their pedagogical 
              expertise would be subordinated to data-driven learning paths.
            - **Creative teaching vs. optimization**: Content creators feared pressure to design for algorithmic optimization 
              rather than student engagement and inspiration.
            - **Personalization vs. community**: The organization's culture had valued creating shared learning experiences, 
              which seemed potentially threatened by highly individualized AI learning paths.
            - **Human connection concerns**: Many employees had joined BYJU'S because they valued education as a fundamentally 
              human endeavor and worried about excessive automation.
            """)
            
            st.markdown("""
            <blockquote>
            "We built our reputation on making learning come alive through great teaching. We worried AI might make learning 
            more efficient but less inspirational."
            <br><em>— Senior Content Developer, BYJU'S</em>
            </blockquote>
            """, unsafe_allow_html=True)
            
            st.subheader("Cultural Adaptation Strategies")
            st.markdown("""
            BYJU'S leadership recognized these cultural tensions and implemented several innovative approaches:

            1. **"Teacher-AI Partnership" Framework**: They developed clear guidelines establishing teachers as the 
               "senior partners" in the relationship, with AI serving their pedagogical vision.

            2. **Explainable AI Requirements**: All learning algorithms were required to provide teachers with clear 
               explanations for their recommendations, allowing for informed overrides.

            3. **Cultural Values Assessment**: Before implementing new AI features, they were evaluated against BYJU'S 
               core values of inspiration, engagement, and student growth.

            4. **"Teaching Moments" Priority**: The platform was designed to identify opportunities where human teacher 
               intervention would have maximum impact, preserving meaningful connections.

            5. **Expanded Teacher Role**: Rather than reducing teacher involvement, BYJU'S redefined the teacher role to 
               focus on motivation, complex concept explanation, and socio-emotional support.
            """)
            
            st.subheader("Results and Key Lessons")
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric(label="Improvement in learning outcomes", value="26%")
                st.metric(label="Teacher job satisfaction", value="89%")
            
            with col2:
                st.metric(label="Student engagement", value="High")
                st.metric(label="Improvement in customer retention", value="31%")
            
            st.markdown("""
            <div class='reflection-box'>
            <strong>Key Lesson:</strong> BYJU'S experience demonstrates that educational organizations can successfully 
            integrate AI while preserving their human-centered teaching culture when they clearly establish the complementary 
            roles of algorithms and educators. Their "Teacher-AI Partnership" model ensured that technology enhanced rather 
            than replaced the human elements that had defined their organizational identity.
            </div>
            """, unsafe_allow_html=True)
    
    # Case Study 5 - Volkswagen
    if "Europe" in region_filter and "Manufacturing" in sector_filter:
        with st.expander("🇩🇪 Volkswagen: Reinventing Manufacturing Culture with AI Collaboration (Germany)"):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.subheader("Organizational Context")
                st.markdown("""
                Volkswagen, Europe's largest automaker with a 90-year heritage, has long maintained a culture balancing German 
                engineering precision with collaborative labor relations. Their organizational structure historically emphasized 
                specialized expertise, hierarchical decision-making, and strong works councils (employee representation groups). 
                In 2020, VW embarked on an ambitious digital transformation, implementing AI systems for everything from supply 
                chain management to predictive maintenance and design optimization.
                """)
            
            with col2:
                st.image("https://via.placeholder.com/250x150.png?text=Volkswagen", caption="Volkswagen")
            
            st.subheader("Cultural Impact and Challenges")
            st.markdown("""
            The introduction of AI systems created several tensions within VW's established culture:

            - **Expertise challenges**: Engineers and specialists with decades of experience found their judgment questioned 
              by algorithms, creating status anxiety.
            - **Decision authority shifts**: Traditional decision hierarchies were disrupted when AI systems provided 
              recommendations that contradicted manager judgments.
            - **Works council concerns**: Employee representatives worried about job displacement and erosion of worker 
              influence in an AI-driven environment.
            - **Cross-functional friction**: The AI transformation required unprecedented collaboration between previously 
              siloed departments, challenging the established organizational structure.
            """)
            
            st.markdown("""
            <blockquote>
            "For generations, German engineering has been about human expertise and precision. Suddenly algorithms were 
            questioning judgments we'd built over entire careers."
            <br><em>— Senior Engineer, Volkswagen</em>
            </blockquote>
            """, unsafe_allow_html=True)
            
            st.subheader("Cultural Adaptation Strategies")
            st.markdown("""
            VW developed a comprehensive approach they called "Collaborative Intelligence" to address these cultural tensions:

            1. **AI Co-Creation Process**: Rather than imposing AI systems from the top down, VW established collaborative 
               design processes where frontline experts helped develop the algorithms that would support their work.

            2. **Joint Human-AI Decision Protocol**: They created clear frameworks defining which decisions would be 
               algorithm-led, human-led, or required collaborative judgment.

            3. **Works Council AI Agreement**: VW negotiated a formal agreement with worker representatives guaranteeing 
               retraining opportunities and establishing ethical boundaries for AI applications.

            4. **"Experience + Data" Value Statement**: The company explicitly redefined expertise as the combination of 
               human experience and data-driven insights, rather than positioning them as competitors.

            5. **Cultural Ambassador Network**: VW trained a network of respected veteran employees to serve as "digital 
               culture bridges" helping their peers adapt to AI collaboration.
            """)
            
            st.subheader("Results and Key Lessons")
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric(label="Improvement in production efficiency", value="23%")
                st.metric(label="Decrease in quality control issues", value="37%")
            
            with col2:
                st.metric(label="Positive attitudes toward AI", value="67%")
                st.metric(label="Workforce retention", value="94%")
            
            st.markdown("""
            <div class='reflection-box'>
            <strong>Key Lesson:</strong> VW's experience demonstrates that even organizations with deeply established cultures 
            and power structures can successfully integrate AI when they treat cultural adaptation as a collaborative process 
            rather than a purely technical implementation. Their approach of engaging both management expertise and worker 
            representation in AI governance created a sustainable model for technological evolution while preserving core 
            cultural values.
            </div>
            """, unsafe_allow_html=True)

# Key Tensions & Themes Section
elif section == "Key Tensions & Themes":
    st.header("Key Tensions & Themes")
    st.write("Explore the common challenges and approaches across different organizations.")
    
    # Theme 1
    with st.expander("Data-Driven Decisions vs. Human Intuition"):
        st.markdown("""
        <div class='reflection-box'>
        Organizations across our case studies confronted the fundamental question: When should algorithms decide, and when 
        should humans have the final say? Most successful organizations rejected a binary choice, instead developing nuanced 
        frameworks that matched decision types with the appropriate balance of algorithmic and human input.

        As Estonia's AI Strategy Director noted: "The question isn't whether AI or humans should decide—it's about designing 
        systems where each contributes their unique strengths to better decisions than either could make alone."
        </div>
        """, unsafe_allow_html=True)
        
        st.subheader("Key approaches for balancing data and intuition:")
        st.markdown("""
        1. **Decision Classification Frameworks**: Organizations like Mayo Clinic developed clear guidelines for which types 
           of decisions should be algorithm-led, human-led, or collaborative.

        2. **Explainable AI Requirements**: Companies like BYJU'S required that AI systems provide clear explanations for 
           their recommendations, enabling informed human oversight.

        3. **Confidence Thresholds**: Several organizations implemented systems where AI would defer to human judgment when 
           confidence levels fell below certain thresholds.

        4. **Training for Collaborative Decision-Making**: Leading organizations developed explicit training on how humans 
           should productively interact with algorithmic recommendations.
        """)
        
        # Visual representation
        decision_data = pd.DataFrame({
            'Decision Type': ['Routine/Repetitive', 'Data-Rich/Pattern-Based', 'Novel/Exceptional', 'Value-Laden/Ethical'],
            'AI Role': ['Primary', 'Primary with Human Oversight', 'Supporting', 'Advisory Only'],
            'Human Role': ['Oversight', 'Final Authority', 'Primary', 'Primary']
        })
        
        st.subheader("Decision Authority Framework")
        st.table(decision_data)
    
    # Theme 2
    with st.expander("Algorithmic Bias and Fairness"):
        st.markdown("""
        Organizations implementing AI systems quickly discovered that algorithms can perpetuate or even amplify existing biases. 
        Our case studies revealed several innovative approaches to addressing this challenge:
        """)
        
        st.markdown("""
        <div class='reflection-box'>
        "Algorithms reflect the data they're trained on, which often contains the accumulated biases of human history. Creating 
        fair AI isn't just a technical challenge—it's a profound cultural commitment that requires ongoing vigilance and 
        diverse perspectives at every stage of development."
        <br><em>— Toyota's Chief Ethics Officer</em>
        </div>
        """, unsafe_allow_html=True)
        
        st.subheader("Key strategies for addressing algorithmic bias:")
        st.markdown("""
        1. **Diverse AI Development Teams**: Organizations like VW and BYJU'S prioritized diversity in their AI development 
           teams to help identify potential bias.

        2. **Explicit Fairness Metrics**: Leading organizations established clear metrics for measuring algorithmic fairness 
           across different demographic groups.

        3. **Bias Bounty Programs**: Some organizations implemented programs rewarding employees who identified potential 
           bias in AI systems.

        4. **Cultural Values Testing**: Organizations like Estonia's government ran AI recommendations through "values 
           alignment tests" to ensure outcomes matched stated ethical principles.
        """)
        
        # Visual representation
        col1, col2 = st.columns(2)
        
        with col1:
            st.image("https://via.placeholder.com/400x300.png?text=Bias+Detection+Process", caption="Bias Detection Process")
        
        with col2:
            st.markdown("""
            #### Common Sources of Algorithmic Bias:
            
            - Historical data reflecting past discrimination
            - Underrepresentation of certain groups in training data
            - Proxy variables that correlate with protected characteristics
            - Context-insensitive algorithm design
