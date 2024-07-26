import streamlit as st
import pandas as pd
import os
import requests
from utils.utils import preprocess_restaurant_name
from utils.data_structures import Input

def get_location_info(lat, lon):
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


