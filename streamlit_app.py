import os
import json
import requests
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
import tiktoken
from crewai import Agent, Task, Crew, Process
from crewai_tools import WebsiteSearchTool
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Load environment variables
load_dotenv()

# Initialize OpenAI client with flexible secret management
def get_openai_api_key():
    try:
        return st.secrets["OPENAI_API_KEY"]
    except Exception:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            st.error("No OpenAI API key found. Please set it in .streamlit/secrets.toml or as an environment variable.")
            st.stop()
        return api_key

# Initialize the OpenAI client
client = OpenAI(api_key=get_openai_api_key())

CPF_URLS = {
    "housing_policies": [
        "https://www.cpf.gov.sg/member/infohub/cpf-clarifies/policy-faqs/why-do-i-need-to-pay-interest-on-cpf-used-for-housing-after-property-sale",
"https://www.cpf.gov.sg/member/infohub/news/news-releases/cpf-members-to-enjoy-lower-premiums-for-home-protection-insurance",
"https://www.cpf.gov.sg/member/infohub/news/news-releases/cpf-members-to-enjoy-lower-premiums-for-home-protection-insurance-26-june-2018",
"https://www.cpf.gov.sg/member/infohub/news/news-releases/over-760000-cpf-members-to-receive-premium-rebates-under-home-protection-scheme",
"https://www.cpf.gov.sg/member/infohub/news/news-releases/cpf-board-awards-tender-on-sale-of-building-at-79-robinson-road-to-southernwood-property-pte-ltd",
"https://www.cpf.gov.sg/member/infohub/news/news-releases/premium-rebates-for-cpf-members-under-home-protection-scheme",
"https://www.cpf.gov.sg/member/infohub/news/forum-replies/eligibility-for-home-insurance-is-reassessed-in-certain-cases",
"https://www.cpf.gov.sg/member/infohub/news/cpf-related-announcements/more-flexibility-to-buy-a-home-for-life-while-safeguarding-retir",
"https://www.cpf.gov.sg/member/infohub/reports-and-statistics/cpf-statistics/home-ownership-statistics",
"https://www.cpf.gov.sg/member/infohub/reports-and-statistics/cpf-statistics/home-ownership-statistics/cumulative-cpf-savings-withdrawn-for-housing",
"https://www.cpf.gov.sg/member/infohub/reports-and-statistics/cpf-statistics/home-ownership-statistics/home-protection-scheme-participation",
"https://www.cpf.gov.sg/member/infohub/reports-and-statistics/cpf-statistics/home-ownership-statistics/home-protection-scheme-claims",
"https://www.cpf.gov.sg/member/infohub/reports-and-statistics/cpf-trends/home-financing",
"https://www.cpf.gov.sg/member/infohub/educational-resources/property-purchase-in-a-pandemic",
"https://www.cpf.gov.sg/member/infohub/educational-resources/financially-savvy-budgeting-tips-for-your-home",
"https://www.cpf.gov.sg/member/infohub/educational-resources/hdb-flat-eligibility-letter-what-to-know",
"https://www.cpf.gov.sg/member/infohub/educational-resources/3-benefits-of-the-home-protection-scheme",
"https://www.cpf.gov.sg/member/infohub/educational-resources/3-differences-between-hdb-loan-and-bank-loan",
"https://www.cpf.gov.sg/member/infohub/educational-resources/sales-proceeds-after-selling-your-home",
"https://www.cpf.gov.sg/member/infohub/educational-resources/protect-your-home-insurance-for-your-hdb-flat",
"https://www.cpf.gov.sg/member/infohub/educational-resources/make-work-from-home-work-for-you",
"https://www.cpf.gov.sg/member/infohub/educational-resources/keep-your-family-close-when-choosing-your-next-home",
"https://www.cpf.gov.sg/member/infohub/educational-resources/roll-smoothly-into-your-hdb-resale-flat-in-4-steps",
"https://www.cpf.gov.sg/member/infohub/educational-resources/how-to-avoid-regret-when-buying-your-dream-home",
"https://www.cpf.gov.sg/member/infohub/educational-resources/easy-tips-to-freshen-up-your-home",
"https://www.cpf.gov.sg/member/infohub/educational-resources/using-cpf-to-budget-for-house-and-renovations",
"https://www.cpf.gov.sg/member/infohub/educational-resources/a-heart-decision-buying-your-first-home",
"https://www.cpf.gov.sg/member/infohub/educational-resources/hdb-option-fee-and-housing-expenses-you-should-know",
"https://www.cpf.gov.sg/member/infohub/educational-resources/home-improvement-programme-what-to-know",
"https://www.cpf.gov.sg/member/infohub/be-ready/budget-for-my-home",
"https://www.cpf.gov.sg/member/ds/dashboards/home-ownership",
"https://www.cpf.gov.sg/member/home-ownership",
"https://www.cpf.gov.sg/member/home-ownership/using-your-cpf-to-buy-a-home",
"https://www.cpf.gov.sg/member/home-ownership/using-your-cpf-to-buy-a-home/considerations-when-using-cpf-to-buy-property",
"https://www.cpf.gov.sg/member/home-ownership/using-your-cpf-to-buy-a-home/apply-to-use-cpf-for-your-property",
"https://www.cpf.gov.sg/member/home-ownership/using-your-cpf-to-buy-a-home/cpf-refund-when-selling-or-transferring-property",
"https://www.cpf.gov.sg/member/home-ownership/using-your-cpf-to-buy-a-home/retain-20000-in-your-oa-if-you-are-taking-a-housing-loan",
"https://www.cpf.gov.sg/member/home-ownership/protecting-against-losing-your-home",
"https://www.cpf.gov.sg/member/home-ownership/protecting-against-losing-your-home/claiming-under-the-home-protection-scheme",
"https://www.cpf.gov.sg/member/home-ownership/protecting-against-losing-your-home/single-premium-home-protection-scheme-cover",
"https://www.cpf.gov.sg/member/home-ownership/plan-your-housing-journey",
"https://www.cpf.gov.sg/member/home-ownership/plan-your-housing-journey/upgrading-your-home",
"https://www.cpf.gov.sg/member/home-ownership/plan-your-housing-journey/upgrading-your-home/housing-case-study",
"https://www.cpf.gov.sg/member/tnc/information-for-exemption-from-home-protection-scheme",
"https://www.cpf.gov.sg/member/tnc/important-notes-on-home-protection-scheme",
"https://www.cpf.gov.sg/member/plan-with-cpf/home-ownership-planning",
"https://www.cpf.gov.sg/employer/infohub/reports-and-statistics/cpf-statistics/home-ownership-statistics",
"https://www.cpf.gov.sg/employer/infohub/reports-and-statistics/cpf-statistics/home-ownership-statistics/cumulative-cpf-savings-withdrawn-for-housing",
"https://www.cpf.gov.sg/employer/infohub/reports-and-statistics/cpf-statistics/home-ownership-statistics/home-protection-scheme-participation",
"https://www.cpf.gov.sg/employer/infohub/reports-and-statistics/cpf-statistics/home-ownership-statistics/home-protection-scheme-claims",
"https://www.cpf.gov.sg/employer/infohub/reports-and-statistics/cpf-trends/home-financing",
    ],
    "general_info": [
        "https://www.cpf.gov.sg/"
    ]
}

# Enhanced URL handling and content fetching functions
def identify_relevant_url(user_message, urls_dict=CPF_URLS):
    """
    Identify relevant URLs based on user query using keyword matching
    """
    relevant_urls = []
    keywords = user_message.lower().split()
    
    for category, urls in urls_dict.items():
        for url in urls:
            # Check if any keyword from the user message appears in the URL
            if any(keyword in url.lower() for keyword in keywords):
                relevant_urls.append(url)
    
    # If no specific URLs found, return general info URLs
    return relevant_urls if relevant_urls else urls_dict["general_info"]

def fetch_webpage_content(url, timeout=10):
    """
    Fetch and parse webpage content with improved error handling and content cleaning
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
        
        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove unwanted elements
        for element in soup(['script', 'style', 'nav', 'footer']):
            element.decompose()
        
        # Extract main content
        main_content = soup.find('main') or soup.find('article') or soup.find('div', {'class': ['content', 'main-content']})
        
        if main_content:
            # Clean and normalize text
            text = ' '.join(main_content.stripped_strings)
            return text
        return ' '.join(soup.stripped_strings)
    
    except requests.RequestException as e:
        st.warning(f"Error fetching content from {url}: {str(e)}")
        return ""

def get_relevant_content_from_urls(urls):
    """
    Fetch and process content from multiple URLs with improved content handling
    """
    content_list = []
    for url in urls:
        content = fetch_webpage_content(url)
        if content:
            # Process and clean content
            cleaned_content = ' '.join(content.split())  # Remove extra whitespace
            # Truncate content if too long (optional)
            max_length = 8000  # Adjust as needed
            if len(cleaned_content) > max_length:
                cleaned_content = cleaned_content[:max_length] + "..."
            
            content_list.append({
                "url": url,
                "content": cleaned_content
            })
    return content_list

# Create custom WebsiteSearchTool for CPF content
class CPFWebsiteSearchTool(WebsiteSearchTool):
    def __init__(self, base_urls=None):
        super().__init__(base_urls if base_urls else CPF_URLS["housing_policies"][0])
        self.all_urls = [url for urls in CPF_URLS.values() for url in urls]
    
    def search(self, query):
        """Enhanced search method for CPF website content"""
        relevant_urls = identify_relevant_url(query)
        content_list = get_relevant_content_from_urls(relevant_urls)
        
        # Combine and format content for the agent
        combined_content = "\n\n".join([
            f"Source: {item['url']}\n{item['content']}"
            for item in content_list
        ])
        
        return combined_content

# Create tools with enhanced CPF search capability
tool_cpf_search = CPFWebsiteSearchTool()

# CrewAI Agents with improved tools and capabilities
agent_researcher = Agent(
    role="CPF Research Analyst",
    goal="Conduct thorough research on CPF housing queries using official CPF sources",
    backstory="""You're a specialized researcher focusing on CPF housing policies and regulations.
    You have access to the latest CPF housing information and can analyze complex policy details.
    You always verify information from official CPF sources and provide accurate, up-to-date information.""",
    tools=[tool_cpf_search],
    allow_delegation=False,
    verbose=True
)

agent_advisor = Agent(
    role="CPF Housing Advisor",
    goal="Provide clear and accurate CPF housing advice",
    backstory="""You're an experienced CPF housing advisor who explains complex policies in simple terms.
    You ensure all advice is accurate and helpful for decision-making.""",
    allow_delegation=False,
    verbose=True
)

agent_writer = Agent(
    role="Content Writer",
    goal="Create clear and comprehensive responses to CPF housing queries",
    backstory="""You're a specialized writer who transforms complex CPF housing information into 
    clear, concise, and user-friendly responses.""",
    allow_delegation=False,
    verbose=True
)

# Function to create CrewAI tasks based on user query
def create_crew_tasks(user_query):
    task_research = Task(
        description=f"""
        1. Research the specific CPF housing query: {user_query}
        2. Identify relevant CPF policies and guidelines
        3. Gather supporting information from official CPF sources
        """,
        agent=agent_researcher,
        tools=[tool_cpf_search],
        async_execution=True
    )

    task_analyze = Task(
        description=f"""
        1. Analyze the research findings for the query: {user_query}
        2. Validate information accuracy
        3. Identify key points that address the user's question
        """,
        agent=agent_advisor,
        context=[task_research],
        async_execution=True
    )

    task_write = Task(
        description=f"""
        1. Create a clear and comprehensive response to: {user_query}
        2. Include relevant policy details and practical implications
        3. Structure the response for easy understanding
        """,
        agent=agent_writer,
        context=[task_research, task_analyze]
    )

    return [task_research, task_analyze, task_write]

# Function to process user query using CrewAI
def process_crew_query(user_query):
    tasks = create_crew_tasks(user_query)
    crew = Crew(
        agents=[agent_researcher, agent_advisor, agent_writer],
        tasks=tasks,
        verbose=True
    )
    return crew.kickoff()

# Enhanced process_user_message function
def process_user_message(user_input):
    with st.spinner('Processing your query...'):
        try:
            # Get CrewAI response
            crew_response = process_crew_query(user_input)
            
            # Get traditional response
            relevant_urls = identify_relevant_url(user_input)
            traditional_response = ""
            if relevant_urls:
                relevant_content = get_relevant_content_from_urls(relevant_urls)
                if relevant_content:
                    traditional_response = generate_response_based_on_content(user_input, relevant_content)
            
            # Combine responses with proper formatting
            combined_response = f"""
            ### AI Analysis
            {crew_response}
            
            ### Additional Information
            {traditional_response if traditional_response else 'No additional information found in traditional sources.'}
            """
            return combined_response
            
        except Exception as e:
            st.error(f"An error occurred while processing your query: {str(e)}")
            return "I apologize, but I encountered an error while processing your request. Please try again."


# Streamlit UI
st.set_page_config(
    layout="centered",
    page_title="Enhanced CPF Housing Information Hub",
    page_icon="🏠"
)

# Initialize session state
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []

st.title("Enhanced CPF Housing Information Hub")

# Sidebar
st.sidebar.header("About This Enhanced Version")
st.sidebar.info("""
This upgraded version combines traditional information retrieval with AI-powered
analysis using CrewAI. It provides more comprehensive and nuanced responses to
your CPF housing queries.
""")

st.sidebar.header("How It Works")
st.sidebar.write("""
1. Research Agent analyzes your query
2. Advisory Agent validates information
3. Writer Agent creates clear responses
4. Traditional system provides additional context
""")

# Main interface
st.write("### Ask Your CPF Housing Question")
st.write("Get comprehensive guidance powered by AI and official CPF sources:")

with st.form(key="query_form"):
    user_prompt = st.text_area(
        "Enter your question:",
        height=100,
        placeholder="e.g., How does CPF housing loan interest work?"
    )
    submit_button = st.form_submit_button("Get Answer")

    if submit_button and user_prompt:
        try:
            response = process_user_message(user_prompt)
            
            # Add to conversation history
            st.session_state.conversation_history.append({
                "question": user_prompt,
                "answer": response
            })
            
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Display conversation history
if st.session_state.conversation_history:
    st.write("### Previous Questions and Answers")
    for item in reversed(st.session_state.conversation_history):
        with st.expander(f"Q: {item['question'][:100]}..."):
            st.write("Question:", item["question"])
            st.markdown(item["answer"])

# Footer
st.write("---")
st.caption("Powered by OpenAI, CrewAI, and Streamlit")