import streamlit as st
import random

# import from other files
from utils.style import style1
from utils.config import food_facts
from utils.data_structures import RestaurantResult

from tabs.restaurant import display_restaurant
from tabs.meal import display_meal
from tabs.chatbot import food_suggestion_chatbot
from tabs.foodguide import display_foodguide
from tabs.sidebar import display_sidebar
from tabs.profile import display_profile

st.set_page_config(page_title="Eat-dentify", page_icon="🍽️", layout="wide", initial_sidebar_state='expanded')

def main():
    style1()
    
    no_sidebar_style = """
        <style>
            div[data-testid="stSidebarNav"] {display: none;}
        </style>
    """
    st.markdown(no_sidebar_style, unsafe_allow_html=True)

    # Create tabs
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["🏠 Restaurant", "🍔 Meal", "🍝 FoodBot", "📑 FoodGuide", "🔐 Profile", "📚Manual"])

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
        # st.warning("This is a work in progress. Please check back later!")
        display_profile()

    with tab6:
        # iframe_src = "https://learned-gooseberry-bd8.notion.site/Eat-dentify-1df1d6ade62e40358b1096e0f1fdbce9/?embed=True"
        # iframe_src = "https://www.example.org"
        # st.components.v1.iframe(iframe_src, height=500, scrolling=True)
        st.image(".streamlit/Eat-dentify_manual.png")
        st.write("---")
        st.link_button("Direct me to manual", "https://learned-gooseberry-bd8.notion.site/Eat-dentify-1df1d6ade62e40358b1096e0f1fdbce9/?embed=True")
    
if __name__ == "__main__":
    main()