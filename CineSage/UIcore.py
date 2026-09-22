import streamlit as st
import sys
import os

from dotenv import load_dotenv, find_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

# Page configuration — call only once,
# before other Streamlit commands.
st.set_page_config(
    page_title="CineSage — Movie Intelligence Extraction",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load environment variables
load_dotenv(find_dotenv())

# Page configuration
st.set_page_config(
    page_title="CineSage — Movie Intelligence Extraction",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom High-End Cinema Styling (Dark Glassmorphism & Gold/Neon Accents)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Cinzel:wght@600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Main container background */
    .stApp {
        background: radial-gradient(circle at 50% -20%, #1f1d36 0%, #0d0e15 60%, #060709 100%);
        color: #f1f5f9;
    }

    /* Hero Banner */
    .hero-container {
        text-align: center;
        padding: 2.2rem 1rem 1.8rem 1rem;
        margin-bottom: 2rem;
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 20px;
        backdrop-filter: blur(12px);
        box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.7), 0 0 50px -20px rgba(234, 179, 8, 0.15);
    }

    .hero-title {
        font-family: 'Cinzel', serif;
        font-size: 3.2rem;
        font-weight: 800;
        letter-spacing: 2px;
        background: linear-gradient(135deg, #ffffff 20%, #facc15 60%, #eab308 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.4rem;
        text-shadow: 0 0 35px rgba(250, 204, 21, 0.25);
    }

    .hero-subtitle {
        color: #94a3b8;
        font-size: 1.05rem;
        font-weight: 400;
        max-width: 650px;
        margin: 0 auto;
        line-height: 1.5;
    }

    .hero-badge {
        display: inline-block;
        background: rgba(234, 179, 8, 0.1);
        color: #facc15;
        border: 1px solid rgba(234, 179, 8, 0.3);
        padding: 4px 14px;
        border-radius: 999px;
        font-size: 0.8rem;
        font-weight: 600;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 0.8rem;
    }

    /* Input Card Container */
    .input-card {
        background: rgba(22, 27, 38, 0.65);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 18px;
        padding: 1.8rem;
        backdrop-filter: blur(16px);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4);
        margin-bottom: 2rem;
    }

    /* Output Card */
    .output-card {
        background: linear-gradient(145deg, rgba(26, 32, 48, 0.75), rgba(16, 20, 31, 0.85));
        border: 1px solid rgba(250, 204, 21, 0.25);
        border-radius: 20px;
        padding: 2.2rem;
        backdrop-filter: blur(20px);
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7), 0 0 30px rgba(250, 204, 21, 0.1);
        margin-top: 1.5rem;
        animation: fadeIn 0.5s ease-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(12px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Streamlit Text Area Customization */
    .stTextArea textarea {
        background-color: rgba(13, 17, 26, 0.7) !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        border-radius: 12px !important;
        color: #f1f5f9 !important;
        font-size: 0.95rem !important;
        padding: 1rem !important;
        transition: all 0.3s ease !important;
    }

    .stTextArea textarea:focus {
        border-color: #facc15 !important;
        box-shadow: 0 0 15px rgba(250, 204, 21, 0.25) !important;
    }

    /* Action Button Customization */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #eab308 0%, #ca8a04 100%) !important;
        color: #0b0d13 !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        letter-spacing: 0.5px !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.65rem 2rem !important;
        box-shadow: 0 8px 20px rgba(234, 179, 8, 0.3) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        width: 100% !important;
    }

    div.stButton > button:first-child:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 12px 25px rgba(234, 179, 8, 0.45) !important;
        color: #000000 !important;
    }

    div.stButton > button:first-child:active {
        transform: translateY(0px) !important;
    }

    /* Footer styling */
    .cinema-footer {
        text-align: center;
        padding: 2rem 0 1rem 0;
        color: #64748b;
        font-size: 0.85rem;
    }
</style>
""", unsafe_allow_html=True)

# Hero Header
st.markdown("""
<div class="hero-container">
    <div class="hero-badge">AI Cinema Intelligence</div>
    <div class="hero-title">CINESAGE</div>
    <div class="hero-subtitle">
        Transform raw movie paragraphs into clean, structured cinematic intelligence with AI precision.
    </div>
</div>
""", unsafe_allow_html=True)

# Mistral AI Model & Prompt Setup (Identical to core.py)
model = ChatMistralAI(model="open-mistral-nemo")

prompt = ChatPromptTemplate.from_messages([
    ("system",
    """
    You are a professional Movie Informational Extraction Assistant.
    Your task:
    Extract useful structured information from a movie paragraph and present it in a clean readable format.
    Rules:
    - Do NOT add explanations
    - Do Not add extra commentary
    - Follow the exact format
    - If information is missing -> write NULL
    - Keep summary short (2-3 lines max)
    - Do NOT guess unkown facts

    Output format:

    Movie Title:
    Release Year:
    Genre:
    Director:
    Main Cast:
    Setting/Location:
    Plot:
    Themes:
    Ratings:
    Notable Features:

    Short Summary:
    """),
    ('human',
    """
    Extract information from this paragraph:
    {paragraph}
    """)
])

# Layout: Two columns for a balanced, spacious interface
col_main, col_spacer = st.columns([1, 0.02])

with col_main:
    st.markdown("#### 📝 Movie Paragraph Input")
    st.caption("Paste a movie synopsis, article snippet, or review below:")

    # Quick example helper
    default_text = ""
    if "example_loaded" not in st.session_state:
        st.session_state.example_loaded = False

    example_sample = (
        "Interstellar (2014) is a science fiction adventure drama film directed by Christopher Nolan. "
        "The movie stars Matthew McConaughey, Anne Hathaway, Jessica Chastain, Michael Caine, and Matt Damon. "
        "It is set in a future where Earth is becoming uninhabitable due to environmental disasters, forcing "
        "humanity to search for a new home. The story follows Cooper, a former NASA pilot, who travels through a "
        "wormhole with a team of astronauts to explore potentially habitable planets. The film explores themes of "
        "love, sacrifice, time, survival, human connection, and the relationship between science and humanity. "
        "It received an IMDb rating of approximately 8.7/10. Notable features include its stunning space visuals, "
        "scientific concepts involving black holes and relativity, Hans Zimmer's memorable soundtrack, and its emotional storytelling."
    )

    btn_col1, btn_col2 = st.columns([0.25, 0.75])
    with btn_col1:
        if st.button("🎬 Load Example", use_container_width=True):
            st.session_state.movie_input = example_sample
            st.rerun()

    user_input = st.text_area(
        label="Movie Paragraph",
        key="movie_input",
        height=180,
        placeholder="Paste your movie paragraph here (e.g., 'Inception (2010) directed by Christopher Nolan...')",
        label_visibility="collapsed"
    )

    extract_clicked = st.button("✨ Extract Movie Intelligence", use_container_width=True)

    if extract_clicked:
        if not user_input.strip():
            st.warning("⚠️ Please provide a movie paragraph to extract information.")
        else:
            with st.spinner("🎞️ Analyzing narrative and extracting structured insights..."):
                try:
                    final_prompt = prompt.invoke({"paragraph": user_input})
                    response = model.invoke(final_prompt)
                    
                    st.markdown("""
                    <div style="margin-top: 1.5rem; margin-bottom: 0.8rem; display: flex; align-items: center; gap: 8px;">
                        <span style="font-size: 1.2rem;">🍿</span>
                        <span style="font-family: 'Cinzel', serif; font-size: 1.3rem; font-weight: 700; color: #facc15; letter-spacing: 1px;">Structured Movie Intelligence</span>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Display structured content in a refined container
                    with st.container():
                        st.markdown(f"""
                        <div class="output-card">
                        """, unsafe_allow_html=True)
                        st.markdown(response.content)
                        st.markdown("</div>", unsafe_allow_html=True)
                        
                except Exception as e:
                    st.error(f"❌ Error during extraction: {str(e)}")

# Minimal Elegant Footer
st.markdown("""
<div class="cinema-footer">
    CineSage • Powered by LangChain & Mistral AI
</div>
""", unsafe_allow_html=True)
