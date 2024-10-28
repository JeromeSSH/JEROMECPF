import streamlit as st
from streamlit_mermaid import st_mermaid

def show_methodology_page():
    st.set_page_config(
        page_title="Methodology - CPF Information Hub",
        page_icon="📊",
        layout="wide"
    )

    st.title("Methodology & Implementation")
    st.write("""
    This page provides a detailed overview of how the CPF Information Hub processes queries 
    and generates responses. We employ a sophisticated multi-layered approach combining 
    different AI technologies and data sources.
    """)

    # Data Flow Overview
    st.header("Data Flow & Processing")
    st.write("""
    Our system uses a comprehensive approach to process queries and generate accurate responses. 
    Here's a detailed breakdown of how information flows through our system.
    """)

    # Main Query Processing Flowchart
    st.subheader("Query Processing Workflow")
    query_flow = """
    flowchart TD
        A[User Query] --> B{Is CPF Related?}
        B -->|Yes| C[CrewAI Processing]
        B -->|No| D[Return Error Message]
        C --> E{CrewAI Success?}
        E -->|Yes| F[Generate CrewAI Response]
        E -->|No| G[OpenAI Fallback]
        F --> H[Format Response]
        G --> H
        H --> I[Display Results]
        I --> J[Update History]
    """
    st_mermaid(query_flow)

    # CrewAI Implementation
    st.header("CrewAI Implementation")
    crew_flow = """
    flowchart TD
        A[User Query] --> B[Research Agent]
        B --> C[Advisor Agent]
        C --> D[Writer Agent]
        B --> E[Web Scraping]
        E --> F[Content Processing]
        F --> C
        D --> G[Final Response]
    """
    st_mermaid(crew_flow)

    # Detailed Implementation
    st.header("Detailed Implementation")
    
    # Content Retrieval
    with st.expander("Content Retrieval Process"):
        st.write("""
        ### Web Scraping & Content Processing
        1. **URL Identification**:
           - Analyze query keywords
           - Match with relevant CPF URLs
           - Prioritize most relevant sources
        
        2. **Content Extraction**:
           - Fetch webpage content
           - Remove unnecessary HTML elements
           - Clean and format text
        
        3. **Content Processing**:
           - Truncate to manageable size
           - Preserve semantic meaning
           - Maintain source attribution
        """)

    # AI Processing
    with st.expander("AI Processing Pipeline"):
        st.write("""
        ### Multi-Agent System
        1. **Research Agent**:
           - Analyzes user query
           - Searches relevant sources
           - Extracts key information
        
        2. **Advisor Agent**:
           - Evaluates research findings
           - Applies policy knowledge
           - Ensures accuracy
        
        3. **Writer Agent**:
           - Formats information
           - Creates clear responses
           - Maintains consistency
        
        ### OpenAI Fallback System
        - Triggers when CrewAI fails
        - Uses GPT-4 for processing
        - Maintains accuracy standards
        """)

    # Error Handling
    with st.expander("Error Handling & Quality Control"):
        st.write("""
        ### Error Management
        1. **Input Validation**:
           - Query relevance checking
           - Keyword validation
           - Source availability verification
        
        2. **Process Monitoring**:
           - CrewAI performance tracking
           - OpenAI fallback monitoring
           - Response quality assessment
        
        3. **Output Verification**:
           - Source attribution
           - Content accuracy checking
           - Response format validation
        """)

    # Data Flow Diagram
    st.header("System Architecture")
    architecture_flow = """
    flowchart TD
        A[User Interface] --> B[Query Processor]
        B --> C{Query Validator}
        C -->|Valid| D[CrewAI System]
        C -->|Invalid| E[Error Handler]
        D --> F{Processing Check}
        F -->|Success| G[Response Generator]
        F -->|Failure| H[OpenAI Fallback]
        H --> G
        G --> I[Response Formatter]
        I --> J[User Interface]
    """
    st_mermaid(architecture_flow)

    # Future CPF Projections Tool Implementation
    st.header("Future CPF Projections Tool Implementation")
    st.write("""
    This section outlines the implementation of the Future CPF Projections Tool, designed to provide users with comprehensive insights into their CPF savings trajectory.
    """)

    projection_flow = """
    flowchart TD
        A[User Input] --> B[Gather Current Account Balances]
        B --> C[Define Projection Parameters]
        C --> D[Calculate Contributions]
        D --> E[Estimate Growth Based on Rates]
        E --> F[Generate Projections Report]
        F --> G[Display Insights]
        G --> H[User Feedback Loop]
    """
    st_mermaid(projection_flow)

    st.header("Detailed Implementation of Singapore CPF Contribution Calculator and Future Projections")

    # Projections Calculation Process
    with st.expander("Projections Calculation Process"):
        st.write("""
        ### Steps to Generate Projections
        1. **Gather Current Account Balances**:
           - Users input their current CPF account balances to enhance accuracy.
       
        2. **Define Projection Parameters**:
           - Users specify current wages, expected increments, and contribution periods. This includes monthly wage input to ensure clarity in projections.
       
        3. **Calculate Contributions**:
           - Utilizing CPF contribution rates based on the user's age group, calculate expected contributions over time.
       
        4. **Estimate Growth Based on Rates**:
           - Apply the latest interest rates for Ordinary, Special, and MediSave Accounts to forecast growth, incorporating compound interest for more accurate projections.
       
        5. **Generate Projections Report**:
           - Create a report detailing projected balances, key insights, and whether users are on track to meet various CPF milestones (Basic Retirement Sum, Full Retirement Sum).
       
        6. **Display Insights**:
           - Present vital information, such as housing affordability estimates based on Ordinary Account accumulation, and when users might hit various CPF milestones.
        """)

    # User Feedback Mechanism
    with st.expander("User Feedback Mechanism"):
        st.write("""
        ### Feedback Integration
        - Users can provide feedback on the projections for continuous improvement.
        - Analyze feedback to adjust algorithms and improve accuracy and user experience.
        """)

    # Educational/Explanatory Features
    st.header("Educational/Explanatory Features")
    st.write("""
    The tool includes several educational elements designed to inform users about CPF concepts:
    - **Detailed Breakdowns**: Explains how each calculation is derived, including allocation to different accounts.
    - **Age-Specific Rates**: Displays applicable rates based on age group and explains why they differ.
    - **Tooltips/Expandable Sections**: Offers additional context on CPF concepts.
    - **Historical Comparisons**: Compares current contributions against previous year’s rates to highlight changes.
    """)

    # Financial Planning Features
    st.header("Financial Planning Features")
    st.write("""
    The Future Projections Tool enhances financial planning with:
    - **Future Savings Projections**: Based on current salary trajectories and contribution patterns.
    - **Milestone Tracking**: Users can see when they might reach significant CPF milestones.
    - **Retirement Adequacy Calculations**: Estimates retirement readiness based on current contributions.
    - **Housing Affordability Estimates**: Calculates potential housing affordability based on Ordinary Account accumulation.
    """)

    # Visual Enhancements
    st.header("Visual Enhancements")
    st.write("""
    To enhance user experience and understanding, the tool includes:
    - **Monthly Contribution Timeline Charts**: Visualize contributions over time.
    - **Account Balance Projections**: Interactive charts that show projected balances.
    - **Comparative Visualizations**: Compare individual projections with national averages.
    - **Progress Bars**: Indicate progress towards CPF milestones.
    """)

    # Key Insights and Recommendations
    st.header("Key Insights and Recommendations")
    st.write("""
    This tool provides users with vital insights regarding their CPF savings trajectory, helping them to:
    - Understand potential shortfalls in meeting retirement sums.
    - Make informed decisions about salary increments and contributions.
    - Strategize their financial planning based on projected growth.
    - Gain insights into property affordability and healthcare savings through MediSave.
    """)

    # Footer
    st.markdown("---")
    st.caption("CPF Information Hub - Technical Documentation")

if __name__ == "__main__":
    show_methodology_page()
