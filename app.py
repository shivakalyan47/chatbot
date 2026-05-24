import streamlit as st
from chat import get_gemini_response

# Page Config with rich title and 
st.set_page_config(
    page_title="Engineering Graphics Assistant | BMS College",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom premium styling via CSS
st.markdown("""
    <style>
        /* Modern title gradient */
        .main-header {
            font-size: 2.5rem;
            font-weight: 800;
            background: linear-gradient(135deg, #FF4B4B, #FF8E53);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.2rem;
        }
        
        .sub-header {
            font-size: 1.1rem;
            color: #888888;
            margin-bottom: 2rem;
            font-weight: 400;
        }
        
        /* Sidebar premium feel */
        .sidebar-title {
            font-size: 1.3rem;
            font-weight: 700;
            color: #FF4B4B;
            margin-bottom: 1rem;
        }
        
        /* Highlight sections */
        .badge {
            background-color: #ffebeb;
            color: #ff4b4b;
            padding: 0.2rem 0.6rem;
            border-radius: 10px;
            font-size: 0.8rem;
            font-weight: 600;
            display: inline-block;
            margin-bottom: 1rem;
        }
        
        [data-theme="dark"] .badge {
            background-color: #2b1f1f;
            color: #ff6b6b;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar with BMS College branding and Engineering Graphics info
with st.sidebar:
    st.markdown('<div class="sidebar-title">📐 BMSCE Graphics Lab</div>', unsafe_allow_html=True)
    st.markdown(
        "Welcome to the virtual **Engineering Graphics (22ME12 / 22ME22)** lab! "
        "I am your dedicated instructor from BMS College of Engineering. "
        "Here to guide you through first-year engineering graphics in the simplest way possible."
    )
    
    st.markdown("---")
    st.markdown("### 📚 Key Topics to Learn")
    st.markdown("- **Projections of Points & Lines**")
    st.markdown("- **Projections of Plane Surfaces**")
    st.markdown("- **Projections of Solids**")
    st.markdown("- **Development of Lateral Surfaces**")
    st.markdown("- **Isometric Projections & Drawings**")
    
    st.markdown("---")
    st.markdown("### 💡 Quick Prompts")
    st.info("Try asking these:")
    st.caption("• *\"What is the difference between First Angle and Third Angle Projection?\"*")
    st.caption("• *\"Explain how to project a hexagonal prism resting on one of its edges.\"*")
    st.caption("• *\"Give me a practice exercise on projection of lines.\"*")
    
    st.markdown("---")
    st.caption("Developed with ❤️ for 1st Year Engineering Students.")

# Main app layout
st.markdown('<div class="badge">BMSCE Virtual Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="main-header">Engineering Graphics Tutor</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Learn projections, solids, and isometric views in a simple, step-by-step way with interactive exercises.</div>', unsafe_allow_html=True)

# Initialize session state chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display current chat logs
for content in st.session_state.chat_history:
    role = "user" if content.role == "user" else "assistant"
    with st.chat_message(role):
        st.markdown(content.parts[0].text)

# Chat Input at the bottom
if prompt := st.chat_input("Ask your graphics instructor..."):
    # Display user's new message immediately
    with st.chat_message("user"):
        st.markdown(prompt)
        
    # Get response with a clean premium spinner/typing indicator
    with st.chat_message("assistant"):
        with st.spinner("Writing on the blackboard..."):
            try:
                response = get_gemini_response(prompt, st.session_state.chat_history)
                st.markdown(response)
            except Exception as e:
                st.error(f"Something went wrong: {e}")
