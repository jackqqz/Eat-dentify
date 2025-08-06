import streamlit as st
import math
from utils.google_map_api import get_review_and_photo, gmaps_text_search, _get_photo_url, get_location_info
from utils.restaurant_ai import get_review_summary
from utils.data_structures import Input
# from tabs.sidebar import get_results
from utils.data_structures import Input, Restaurant, RestaurantResult


def display_meal():
    """
    Display AI-suggested meals from restaurant search results in a two-column layout.
    
    Filters and displays meal recommendations from restaurants in the session state:
    - Filters out restaurants that don't have valid meal suggestions ('None' meals)
    - Creates a responsive two-column grid layout for meal display
    - Shows each meal in an expandable card with:
        * Meal name as the header
        * Detailed meal description
        * Citation information with restaurant source
        * Wikipedia search link for additional information
    
    Only displays content when valid meal results are available.
    """

    results = st.session_state.results.get_list()
    results = [
        place for place in results
        if 'None' not in place.get_meal()
    ]

    if len(results) > 0:
        st.subheader("AI-Suggested Meal")
        with st.spinner(text="displaying meal..."):
            ml1, ml2 = st.columns(2)
            for index in range(len(results)):
                each_restaurant: Restaurant = results[index]
                current_col = ml1 if index % 2 == 0 else ml2

                meal = each_restaurant.get_meal()
            
                with current_col:
                    with st.expander(meal, expanded=True):
                        st.markdown(f"## {meal}")
                        st.markdown(f'**Description** \n ')
                        st.markdown(each_restaurant.get_meal_description())
                        st.markdown(f'**Citation**')
                        st.write(f'\n:green-background[{each_restaurant.get_meal_citation()}]')
                        st.markdown(f'-- {each_restaurant.get_name()}')
                        st.markdown(f"""
                            <div style="display: flex; gap: 20px; margin: 10px 0;">
                                <a href="https://en.wikipedia.org/w/index.php?search={meal}" target="_blank" style="text-decoration: none; color: #1D90FF; padding: 5px 10px; border: 1px solid #1D90FF; border-radius: 5px; display: inline-flex; align-items: center;">
                                    Search on Wikipedia
                                </a>
                            </div>
                            <div style="height: 20px;"></div>
                        """, unsafe_allow_html=True)


