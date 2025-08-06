import streamlit as st
import pandas as pd
from streamlit_geolocation import streamlit_geolocation
from utils.constants import restaurants
from utils.google_map_api import get_location_info

from utils.restaurant_ai import process_restaurant
from utils.data_structures import Input, Restaurant, RestaurantResult

def display_sidebar():
    """
    Display the interactive sidebar for restaurant search with comprehensive filtering options.
    
    Handles both authenticated and guest user experiences with appropriate
    feature availability and personalization options.
    """
    if st.session_state.logged_in:
        st.header("Welcome Back, " + st.session_state.username + " 👨‍🦰🍤🍙🥂")
        st.markdown(f"Your personal remark: **{st.session_state.user_remarks}**")
        st.write("---")
    
    st.header("Find Your Perfect Meal")
    budget = str(st.select_slider("Budget:", options=['$', '$$', '$$$'], value='$$'))
    min_rating, max_rating = st.slider("Rating Range:", 0.0, 5.0, (3.0, 5.0), 0.1)
    travel_time = st.slider("Travel Time (minutes):", 0, 120, 30, 1)

    st.write("---")

    cuisine = ",".join(st.multiselect("Cuisine Type: \n\n *:gray[multi-select]*", options=[''] + restaurants))
    craving = st.text_input("Specific Craving: \n\n *:gray[optional]*")
    remarks = st.text_area("Remark: \n\n *:gray[describe your scenario]*")
    if st.session_state.logged_in:
        searching_for_myself = st.checkbox("I am searching for myself \n\n *:gray[this considers your personal preferences when generating result]*")
        if searching_for_myself:
            remarks += str(st.session_state.user_remarks)
    
    # city = st.text_input("City:")

    st.write("---")
    location = streamlit_geolocation()
    city_input = None
    lat = location['latitude']
    lon = location['longitude']

    if lat is not None and lon is not None:
        df = pd.DataFrame({'lat': [lat], 'lon': [lon]})
        st.map(df)
        city, country = get_location_info(lat, lon)
        current_location = f"{city}, {country}" if city and country else None

        if current_location:
            st.write(f"Your current location: {current_location}")

            # Check if location has changed
            if current_location != st.session_state.previous_location:
                st.session_state.previous_location = current_location
                st.session_state.city_input = current_location

            # Use session state for city input
            city_input = st.text_input("City:", value=st.session_state.city_input)
        else:
            st.write("Couldn't determine your current location.")
            city_input = st.text_input("City:")
    else:
        st.write("Please enable location sharing in your browser settings.")
        city_input = st.text_input("City:")


    st.write("---")
    find_restaurants = st.button("Find Restaurants", key="find")
    if find_restaurants:

        st.toast("Searching for restaurants...")
        input_obj: Input = Input(int(min_rating), int(max_rating), city_input, budget, craving, cuisine, travel_time, remarks)
        process_result = process_restaurant(input_obj)
        try:
            st.session_state.results = process_result if process_result else st.session_state.results
        except:
            process_result.get_list()
            
        st.session_state.input = input_obj
