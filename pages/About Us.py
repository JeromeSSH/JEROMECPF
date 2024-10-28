import streamlit as st

def show_about_page():
    st.set_page_config(
        page_title="About - CPF Information Hub",
        page_icon="ℹ️",
        layout="wide"
    )

    st.title("About CPF Information Hub")

    # Project Overview
    st.header("Project Overview")
    st.write("""
    The CPF Information Hub is a comprehensive platform designed to provide Singapore residents 
    with accurate, AI-powered information about Central Provident Fund policies and calculations. 
    Our platform combines advanced AI technology with official CPF resources to deliver reliable, 
    up-to-date information about CPF policies, especially focusing on housing-related queries.
    """)

    # Project Scope
    with st.expander("Project Scope"):
        st.write("""
        ### Use Case 1
        - Intelligent query processing for CPF-related questions
        - Focus on housing policies and regulations
        - Real-time data extraction from official CPF sources
        - AI-powered analysis using both CrewAI and OpenAI technologies

        ### Use Case 2
        - Integration of CPF calculator functionalities
        - Personal CPF portfolio analysis
        - Retirement planning tools
        - Enhanced data visualization features
        """)

    # Project Objectives
    with st.expander("Key Objectives"):
        st.write("""
        1. **Accessibility**: Make CPF information easily accessible to all Singaporeans
        2. **Accuracy**: Ensure high accuracy of information through:
            - Direct integration with official CPF sources
            - AI-powered verification systems
            - Regular updates to maintain current information
        3. **User Experience**: Provide a seamless, intuitive interface for users to:
            - Get quick answers to CPF queries
            - Access detailed policy information
            - Understand complex CPF concepts easily
        4. **Reliability**: Implement robust systems for:
            - Data verification
            - Source tracking
            - Error handling
        """)

    # Data Sources
    with st.expander("Data Sources"):
        st.write("""
        ### Primary Sources
        - Official CPF Website (www.cpf.gov.sg)
        - CPF Policy FAQs
        - CPF News Releases
        - CPF Statistical Reports
        - CPF Board Annual Reports
        """)

    # Features
    st.header("Key Features")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Core Features")
        st.write("""
        - 🤖 AI-Powered Query Processing
        - 📊 Real-time Information Retrieval
        - 🏠 Housing Policy Analysis
        - 📱 User-Friendly Interface
        - 🔍 Smart Search Functionality
        """)

    with col2:
        st.subheader("Technical Capabilities")
        st.write("""
        - ⚡ Dual AI System (CrewAI + OpenAI)
        - 🔄 Real-time Data Updates
        - 🛡️ Error Handling & Fallbacks
        - 📈 Query Performance Analytics
        - 🔗 Source Verification System
        """)

    # Technology Stack
    st.header("Technology Stack")
    tech_col1, tech_col2, tech_col3 = st.columns(3)

    with tech_col1:
        st.markdown("### Frontend")
        st.write("""
        - Streamlit
        - HTML/CSS
        - JavaScript
        """)

    with tech_col2:
        st.markdown("### Backend")
        st.write("""
        - Python
        - CrewAI
        - OpenAI API
        """)

    with tech_col3:
        st.markdown("### Tools & Libraries")
        st.write("""
        - BeautifulSoup4
        - Requests
        - Pandas
        """)

    # Contact Information
    st.header("Contact & Support")
    st.write(""" 
    For questions, feedback, or support, please contact us at:
    - 📧 Email: Jerome_See@mom.gov.sg
    - 💬 Live Chat: Available during business hours
    """)

    # Fun Fact
    with st.expander("Fun Fact about Project"):
        st.write(""" 
        Was halfway done with the project and went for a holiday to China for 9 days after Prompt Royale Open. 
        Came home to 2 dead alienware laptops. 
        1 dead SSD and 1 CPU failure.
        Had to start all over. 
        Also, RIP laptops.
        """)

    # Footer
    st.markdown("---")
    st.caption("CPF Information Hub - Empowering Singaporeans with accurate CPF information")

if __name__ == "__main__":
    show_about_page()
