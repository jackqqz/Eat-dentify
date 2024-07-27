import streamlit as st
import os
import google.generativeai as genai
import math

from utils.utils import preprocess_restaurant_name
from utils.data_structures import Input, Restaurant, RestaurantResult
from utils.prompt import search_prompt, review_summary, meal_suggestion, column_prompt
from utils.llm_api import get_Gemini
from utils.google_map_api import gmaps_text_search, get_review_and_photo

def add_column(input: Input, restaurant: Restaurant, prompt: str, column_name: str) -> Restaurant:
    model = get_Gemini()

    response = model.generate_content(f"knowing that {input.get_remarks()}, the review {restaurant.get_review()}, tell me about: {prompt}" + column_prompt)
    restaurant.add_custom_field(column_name, response.text)
    return restaurant


def process_restaurant(input: Input) -> RestaurantResult:
    """
    Be caution with this function, it triggers one text search five place details, five photo and one geocode.
    It may cost a lot based on google maps api https://developers.google.com/maps/documentation/places/web-service/usage-and-billing
    """
    with st.status("Searching for restaurant...", expanded=True) as status:

        try:
        

            # Understand user needs and generate prompt for text search
            text_search_prompt = get_search_prompt(input)
            st.write(f"Searching Prompt: \n\n**{text_search_prompt}**")
        
            # Perform text search
            filtered_result = gmaps_text_search(text_search_prompt, input)
            st.write('---')
            st.write(f"Got **{len(filtered_result)}** results")
        
            # Tidy up output and generate random (max five) restaurant
            selected_result: RestaurantResult = restaurant_parser(filtered_result)
            st.write(f"---")
            st.write(f"Selected **{len(selected_result)}** most relevant results")
            
            # Gather review and photo
            updated_list = []
            for each_restaurant in selected_result.get_list():
                each_id = each_restaurant.get_place_id()
                review, photo_url = get_review_and_photo(each_id)
                each_restaurant.add_reviews(review)
                each_restaurant.set_photo(photo_url)
                
                updated_list.append(each_restaurant)

            st.write(f"---")
            st.write(f"Gathered reviews and photos")
        
        
            # Update restaurant list
            selected_result.update_list(updated_list)
            progress_counter = 0

            st.write(f"---")
            progress_text = "Generating restaurant output..."
            res_bar = st.progress(0.0, text=progress_text)
            total_restaurants_no = len(selected_result.get_list())
            
            # generate summary
            updated_list = []
            for index, each_restaurant in enumerate(selected_result.get_list()):
                reason = get_review_summary(each_restaurant, input)
                each_restaurant.add_restaurant_reason(reason)
                updated_list.append(each_restaurant)
                progress = min((index + 1) / total_restaurants_no, 1.0)
                res_bar.progress(progress, text=progress_text)
        
            # Update restaurant list
            selected_result.update_list(updated_list)

            st.write(f"---")
            progress_text = "Generating meal output..."
            meal_bar = st.progress(0.0, text=progress_text)
            total_restaurants_no = len(selected_result.get_list())

            
            # Generate meal suggestion
            updated_list = []

            for index, each_restaurant in enumerate(selected_result.get_list()):
                meal, meal_citation, meal_description = get_meal_suggestion(each_restaurant, input)
                each_restaurant.add_meal(meal, meal_citation, meal_description)
                updated_list.append(each_restaurant)
                progress = min((index + 1) / total_restaurants_no, 1.0)
                meal_bar.progress(progress, text=progress_text)
        
            # Update restaurant list
            selected_result.update_list(updated_list)
    
            status.update(label="Search Complete!", state="complete", expanded=False)
        
            return selected_result
            
        except Exception as e:
            st.error("Server busy, please try again later 🙁 \n(please wait approximately one minute before trying again)")
            # st.write(e)
            return None


def get_search_prompt(input: Input) -> str:

    model = get_Gemini()
    
    response = model.generate_content(f"{search_prompt} \n\n{input.get_remarks()}")
    text_search_prompt = f"$$ {response.text[:-2]} {input.get_cuisine()} {input.get_craving()} {input.get_city()}"
    return text_search_prompt
    
def generate_random_index(filtered_results) -> list[int]:
    model = get_Gemini()
    no_to_generate = 0

    if len(filtered_results) >= 5:
      no_to_generate = 5
    else:
      no_to_generate = len(filtered_results) - 1

    text = f'''
            Please generate random non-duplicating {no_to_generate} index seperating with comma ', ' strictly in
            the range 0 to {len(filtered_results) - 1}. Do not exceed the range.
            Please do not code, provide only {no_to_generate} whole numbers. Do not respond my prompt, reply with numbers only
            '''

    response = model.generate_content(text)
    random_index = list(map(int,response.text[:-2].split(', ')))
    
    return random_index


def restaurant_parser(filtered_results) -> RestaurantResult:
    
    restaurant_result = RestaurantResult(
        filtered_results,
        random_index=generate_random_index(filtered_results)
    )

    return restaurant_result
    

def get_review_summary(restaurant: Restaurant, input: Input) -> str:
  model = get_Gemini()
  review = restaurant.get_review()
  name = restaurant.get_name()

  text = f'''
          Strictly and only refer to this: \n\n {review} \n\n
          for this restaurant: {name} \n\n
          ''' + review_summary + f''' \n\n
          {str(input)}
          '''

  response = model.generate_content(text)
  return response.text

def get_meal_suggestion(restaurant: Restaurant, input: Input):
    model = get_Gemini()
    review = restaurant.get_review()
    name = restaurant.get_name()
    
    text = f'''
          Strictly and only refer to this: \n\n {review} \n\n
          for this restaurant: {name} \n\n
          {meal_suggestion} \n\n
          {str(input)}
          '''
    
    response = model.generate_content(text)
    response = response.text.split('| ')
    meal = response[0]
    meal_citation = response[1]
    meal_description = response[2]

    return meal, meal_citation, meal_description

