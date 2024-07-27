import streamlit as st
import math
import urllib.parse

from utils.google_map_api import get_review_and_photo, gmaps_text_search, _get_photo_url, get_location_info
from utils.restaurant_ai import get_review_summary, add_column
from utils.data_structures import Input
# from tabs.sidebar import get_results
from utils.data_structures import Input, Restaurant, RestaurantResult
from utils.style import restaurant_style


def display_restaurant():
    st.session_state.sidebar_state = "expanded"
    results = st.session_state.results.get_list()
    # st.toast(f"Displaying {len(results)} results!")

    if len(results) > 0:
        restaurant_style()

        st.markdown("## AI-Suggested Restaurants")

        for index, restaurant in enumerate(results):
            name = restaurant.get_name()
            place_id = restaurant.get_place_id()
            with st.expander(name, expanded=False):
                # Google Maps link
                maps_url = f"https://www.google.com/maps/place/?q=place_id:{place_id}"
                
                # Waze Maps link
                encoded_name = urllib.parse.quote(name)
                waze_url = f'https://waze.com/ul?q={name.replace(" ", "%20")}'
                
                col1, col2 = st.columns([1, 2])

                with col1:
                    photo_url = restaurant.get_photo()
                    if photo_url:
                        st.markdown(f"""
                            <div class="restaurant-image-container">
                                <img src="{photo_url}" class="restaurant-image" />
                            </div>
                        """,
                                    unsafe_allow_html=True)
                        st.write('---')
                        st.markdown('**Rating:**')
                        st.write(('⭐' * math.floor(float(restaurant.get_rating()))) + f' ({restaurant.get_rating()})')
                        st.write('---')
                        st.write('**Address**')
                        st.write(restaurant.get_address())

                with col2:
                    preprocessed_reason = '\n' + format_citation(restaurant.get_restaurant_reason())
                    # maps_url = f"https://www.google.com/maps/place/?q=place_id:{restaurant.get_place_id()}"
                    waze_url = f"https://waze.com/ul?q={urllib.parse.quote(name)}"
                    preprocessed_reason = '\n' + restaurant.get_restaurant_reason()
                    
                    st.markdown(f"""
                    <div class='restaurant-card'>
                        <div class='restaurant-name'>{name}</div>
                        {preprocessed_reason} <br><br>
                        <a href="{maps_url}" target="_blank" class="map-button google-maps-button">
                            <img src="https://www.google.com/s2/favicons?domain=maps.google.com&sz=32" alt="Google Maps">
                            View on Google Maps
                        </a>
                        <a href="{waze_url}" target="_blank" class="map-button waze-button">
                            <img src="https://www.google.com/s2/favicons?domain=waze.com&sz=32" alt="Waze">
                            Navigate with Waze
                        </a>
                    </div>
                    """, unsafe_allow_html=True)

                    for each_column_name in restaurant.get_custom_field_dict().keys():
                        each_column_response = '\n' + format_citation(restaurant.get_custom_field(each_column_name))

                        st.markdown(f"""
                        <div class='restaurant-card'>
                            <div class='restaurant-name'>{each_column_name}</div>
                            {each_column_response} <br><br>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        
                        

        st.subheader("Need to know more about the restaurants?")
        st.caption("By adding a column, you can include the answer of your query towards each restaurant in the result page")
        add_col1, add_col2 = st.columns([1, 2])
        with add_col1:
            column_name = st.text_input("Name the column:")
        with add_col2:
            column_prompt = st.text_input("Instruction:")
        if st.button("Add Column"):
            try:
                with st.status("Adding Column...", expanded=True) as status:
                    for each_restaurant in st.session_state.results.get_list():
                        add_column(st.session_state.input, each_restaurant, column_prompt, column_name)

            except Exception as e:
                st.error("Server busy, please try again later 🙁 \n(please wait approximately one minute before trying again)")
                # st.write(e)

            st.rerun()
            

    else:
        st.info("No restaurants found. Try adjusting your search criteria.")

def format_citation(citation):
    return citation.replace(':red-background[', '<br>:red-background[').replace(':green-background[', '<br>:green-background[').replace(']', ']<br>')
