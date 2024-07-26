from typing import Dict
import streamlit as st


"""
This file contains the data structures used in the application.
So we no need to remember what the property store in the json object.
"""
class Article:
  def __init__(self, url: str, title: str, description: str, img_url:str):
    self.url = url
    self.title = title
    self.description = description
    self.upvotes = 0
    self.downvotes = 0
    self.tags = []
    self.image = img_url

  def upvote(self):
    self.upvotes += 1

  def downvote(self):
    self.downvotes += 1

  def add_tag(self, tag: str):
    self.tags.append(tag)


class Input:
  """
  This represents the user input from the sidebar
  """
  def __init__(self, min_rating: int, max_rating: int, city: str, budget: str, craving: str, cuisine: str, travel_time: str, remarks: str):
    self.min_rating: int = min_rating
    self.max_rating: int = max_rating
    self.city: str = city
    self.budget: str = budget
    self.craving: str = craving
    self.cuisine: str = cuisine
    self.travel_time: str = travel_time
    self.remarks: str = remarks

  def get_city(self) -> str:
    return self.city

  def get_min_rating(self) -> int:
    return self.min_rating

  def get_max_rating(self) -> int:
    return self.max_rating
    
  def get_radius(self) -> float:
    return min(500 * float(self.travel_time), 20000)

  def get_remarks(self) -> str:
    return self.remarks

  def get_cuisine(self) -> str:
    return self.cuisine

  def get_craving(self) -> str:
    return self.craving

  def __str__(self):
    return f"fulfil this requirement {self.remarks}, I am searching for {self.cuisine} cuisine, craving for {self.craving}"

class Restaurant:
  """
  This represents one restaurant
  """

  def __init__(self, place_id: str, name: str, rating: str, address: str):
    self.place_id: str = place_id
    self.name: str = name
    self.rating: str = rating
    self.reviews: str = ""
    self.photo: str = ""
    self.restaurant_reason: str = ""
    self.meal: str = ""
    self.meal_citation: str = ""
    self.meal_description: str = ""
    self.custom_field: Dict[str, str] = {}
    self.address: str = address
    

  def get_address(self) -> str:
    return self.address

  def get_rating(self) -> str:
    return self.rating

  def get_place_id(self) -> str:
    return self.place_id

  def get_name(self) -> str:
    return self.name

  def add_reviews(self, reviews: str):
    self.reviews += reviews

  def get_review(self) -> str:
    return self.reviews

  def set_photo(self, photo: str):
    self.photo = photo

  def get_photo(self) -> str:
    return self.photo

  def add_restaurant_reason(self,reason: str):
    self.restaurant_reason += reason

  def get_restaurant_reason(self) -> str:
    return self.restaurant_reason
    
  def add_meal(self, meal: str, meal_citation: str, meal_description: str):
    self.meal += meal
    self.meal_citation += meal_citation
    self.meal_description += meal_description

  def get_meal(self) -> str:
    return self.meal

  def get_meal_citation(self) -> str:
    return self.meal_citation

  def get_meal_description(self) -> str:
    return self.meal_description

  def add_custom_field(self, key: str, value: str):
    self.custom_field[key] = value

  def get_custom_field_dict(self):
    return self.custom_field

  def get_custom_field(self, key: str) -> str:
    try:
      return self.custom_field[key]
    except:
      return ""

  

class RestaurantResult:
  """
  The represents the output restaurants
  """
  def __init__(self, filtered_result, random_index: list[int]):

    self.restaurant_result: list[Restaurant] = []
    
    for each_index in random_index:
      each_output = filtered_result[each_index]
      self.restaurant_result.append(Restaurant(
        name=f"{each_output['name']}",
        place_id=f"{each_output['place_id']}",
        rating=f"{each_output['rating']}",
        address=f"{each_output['formatted_address']}"
      ))

  def update_list(self, restaurant_result: list[Restaurant]) :
    self.restaurant_result = restaurant_result

  def get_list(self) -> list[Restaurant]:
    return self.restaurant_result

  def __len__(self):
    return len(self.restaurant_result)