import streamlit as st
import pandas as pd
import os
import requests
from utils.utils import preprocess_restaurant_name
from utils.data_structures import Input

def get_location_info(lat, lon):
    """
    Get city and country information from latitude and longitude coordinates.
    
    Args:
        lat (float): Latitude coordinate
        lon (float): Longitude coordinate
        
    Returns:
        tuple: (city, country) where both are strings or None if not found
        
    Uses Google Maps Geocoding API to reverse geocode coordinates into
    human-readable location information. Extracts locality (city) and
    country from the address components.
    """
    api_key = os.environ["GOOGLE_MAPS_API_KEY"]
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "latlng": f"{lat},{lon}",
        "key": api_key
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        if data["status"] == "OK" and data["results"]:
            city = ""
            country = ""
            for component in data["results"][0]["address_components"]:
                if "locality" in component["types"]:
                    city = component["long_name"]
                if "country" in component["types"]:
                    country = component["long_name"]

            return city, country
        else:
            st.error(f"Geocoding API error: {data['status']}")
            return None, None
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred while fetching location info: {str(e)}")
        return None, None

def _get_photo_url(photo_reference, max_width=400):
    """
    Generate a photo URL from Google Places photo reference.
    
    Args:
        photo_reference (str): Photo reference ID from Google Places API
        max_width (int, optional): Maximum width for the photo. Defaults to 400.
        
    Returns:
        str: Complete URL for accessing the photo from Google Places API
        
    Private helper function that constructs the proper Google Places Photo API
    URL with the required parameters including API key and photo dimensions.
    """
    api_key = os.environ["GOOGLE_MAPS_API_KEY"]
    base_url = "https://maps.googleapis.com/maps/api/place/photo"
    params = {
        "maxwidth": max_width,
        "photo_reference": photo_reference,
        "key": api_key
    }
    response = requests.get(base_url, params=params)
    return response.url

def gmaps_text_search(search_prompt: str, input: Input):
    """
    Search for restaurants using Google Places Text Search API.
    
    Args:
        search_prompt (str): Search query text for finding restaurants
        input (Input): User input object containing search criteria and filters
        
    Returns:
        list: Filtered list of restaurant data dictionaries from Google Places API
        
    Performs a text-based search for restaurants with the following filters:
    - Search radius based on travel time from Input object
    - Rating range filtering (min/max ratings)
    - Open now status (only returns currently open restaurants)
    - Validates that results have required fields (rating, opening_hours)
    """
    api_key = os.environ["GOOGLE_MAPS_API_KEY"]
    base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    filtered_results = []

    params = {
        "query": search_prompt,
        "radius": input.get_radius(),
        "key": api_key,
        "minRating": input.get_min_rating(),
        "maxRating": input.get_max_rating()
    }

    response = requests.get(base_url, params=params)
    response.raise_for_status()
    data = response.json()
    if data["status"] == "OK" and data["results"]:

        min_rating = input.get_min_rating()
        max_rating = input.get_max_rating()

        filtered_results = [
            place for place in data["results"]
            if 'rating' in place and 'opening_hours' in place and min_rating <= place['rating'] <= max_rating and place['opening_hours']['open_now']
        ]

    else:
        st.toast('search map error')

    return filtered_results

def get_review_and_photo(place_id: str):
    """
    Retrieve restaurant reviews and photo URL using Google Places Details API.
    
    Args:
        place_id (str): Google Places unique identifier for the restaurant
        
    Returns:
        tuple: (review, photo_url) where:
            - review (str): String representation of restaurant reviews
            - photo_url (str): URL of the restaurant's primary photo
            
    Uses Google Places Details API to fetch additional restaurant information
    including customer reviews and photos. Processes the first available photo
    through the photo reference system to generate accessible photo URLs.
    """
    api_key = os.environ["GOOGLE_MAPS_API_KEY"]

    # Get additional details including photos, reviews, and website
    details_url = "https://maps.googleapis.com/maps/api/place/details/json"
    details_params = {
      "place_id": place_id,
      "fields": "photos,reviews",
      "key": api_key
    }
    details_response = requests.get(details_url, params=details_params)
    details_data = details_response.json()

    photo_url = f'{_get_photo_url(details_data["result"]["photos"][0]["photo_reference"])}'
    review = f"{details_data['result']['reviews']}"
    
    return review, photo_url


