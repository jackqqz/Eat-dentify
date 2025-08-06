import streamlit as st
import random

# import from other files
from utils.style import light_theme, dark_theme
from utils.constants import food_facts
from utils.data_structures import RestaurantResult

from tabs.restaurant import display_restaurant
from tabs.meal import display_meal
from tabs.chatbot import food_suggestion_chatbot
from tabs.foodguide import display_foodguide
from tabs.sidebar import display_sidebar
from tabs.profile import display_profile
from PIL import Image
from streamlit_theme import st_theme

st.set_page_config(page_title="Eat-dentify", page_icon="🍽️", layout="wide", initial_sidebar_state='expanded')

def main():
    """
    Main function for the Eat-dentify Streamlit application.
    
    This function sets up and runs the complete Eat-dentify web application with the following features:
    - Dynamic theme switching (light/dark mode)
    - Multi-tab interface with 6 main sections:
        * Restaurant: Find and explore restaurant options
        * Meal: Meal planning and nutrition information
        * FoodBot: AI-powered food suggestion chatbot
        * FoodGuide: Comprehensive food and nutrition guide
        * Profile: User profile management and login system
        * Manual: Application documentation and user guide
    - Session state management for user data persistence
    - Sidebar for user input and navigation
    - Random food facts display when no search results are available
    
    The application maintains user login state, location preferences, search results,
    and other session data throughout the user's interaction.
    """

    if st_theme()['base'] == "light":  
        light_theme()
    else:
        dark_theme()
    
    no_sidebar_style = """
        <style>
            div[data-testid="stSidebarNav"] {display: none;}
        </style>
    """
    st.markdown(no_sidebar_style, unsafe_allow_html=True)

    # Create tabs
    # Create tabs with both full labels and emoji-only labels
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "🏠 Restaurant",
        "🍔 Meal",
        "🍝 FoodBot",
        "📑 FoodGuide",
        "🔐 Profile",
        "📚 Manual"
    ])

    # lang_chain_bundle = initialize_langchain()
    # buffer_chain = lang_chain_bundle["buffer_chain"]
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'username' not in st.session_state:
        st.session_state.username = None
    if 'user_remarks' not in st.session_state:
        st.session_state.user_remarks = ""
    if 'previous_location' not in st.session_state:
        st.session_state.previous_location = None
    if 'password' not in st.session_state:
        st.session_state.password = None
    if 'results' not in st.session_state:
        st.session_state.results = RestaurantResult({}, [])
    
    # Sidebar for user input
    with st.sidebar:
        display_sidebar()

    follow_up = None

    # random facts

    # tab1 - Restaurant
    with tab1:
        display_restaurant()

        if not st.session_state.results:
            st.info(f"**Did you know?**\n\n {random.choice(food_facts)}")

    # tab2 - Meal
    with tab2:
        display_meal()

        if not st.session_state.results:
            st.info(f"**Did you know?**\n\n {random.choice(food_facts)}")


    # tab3 - Chatbot
    with tab3:
        food_suggestion_chatbot()

    # tab4 - Food Guide
    with tab4:
        display_foodguide()
      
    with tab5:
        display_profile()

    with tab6:
        
        # save image in session_state to make loading faster
        if 'manual_thumbnail' not in st.session_state:
            st.session_state.manual_thumbnail = Image.open(".streamlit/Eat-dentify_manual.png")

        st.image(st.session_state.manual_thumbnail)
        
        st.write("---")
        st.link_button("Direct me to manual", "https://learned-gooseberry-bd8.notion.site/Eat-dentify-1df1d6ade62e40358b1096e0f1fdbce9/?embed=True")

        
    
if __name__ == "__main__":
    main()