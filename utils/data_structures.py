from typing import Dict
import streamlit as st
"""
This file contains the data structures used in the application.
"""

class Article:
    """
    Represents a food-related article with metadata and user interaction features.
    
    Stores article information including URL, title, description, and image.
    Supports user engagement through upvote/downvote system and tagging functionality.
    """
    
    def __init__(self, url: str, title: str, description: str, img_url:str):
        """
        Initialize an Article object.
        
        Args:
            url (str): The source URL of the article
            title (str): Article title
            description (str): Article description or summary
            img_url (str): URL of the article's featured image
        """
        self.url = url
        self.title = title
        self.description = description
        self.upvotes = 0
        self.downvotes = 0
        self.tags = []
        self.image = img_url

    def upvote(self):
        """Increment the upvote count for this article."""
        self.upvotes += 1

    def downvote(self):
        """Increment the downvote count for this article."""
        self.downvotes += 1

    def add_tag(self, tag: str):
        """
        Add a tag to categorize this article.
        
        Args:
            tag (str): Tag to add to the article
        """
        self.tags.append(tag)


class Input:
    """
    Represents user input from the sidebar for restaurant search criteria.
    
    Encapsulates all search parameters including ratings, location, budget,
    cuisine preferences, and personal remarks for AI-powered recommendations.
    """
    
    def __init__(self, min_rating: int, max_rating: int, city: str, budget: str, craving: str, cuisine: str, travel_time: str, remarks: str):
        """
        Initialize search input parameters.
        
        Args:
            min_rating (int): Minimum acceptable restaurant rating
            max_rating (int): Maximum restaurant rating filter
            city (str): Target city for restaurant search
            budget (str): Budget level ($, $$, $$$)
            craving (str): Specific food craving or dish
            cuisine (str): Preferred cuisine types (comma-separated)
            travel_time (str): Maximum travel time in minutes
            remarks (str): Additional search context and preferences
        """
        self.min_rating: int = min_rating
        self.max_rating: int = max_rating
        self.city: str = city
        self.budget: str = budget
        self.craving: str = craving
        self.cuisine: str = cuisine
        self.travel_time: str = travel_time
        self.remarks: str = remarks

    def get_city(self) -> str:
        """Get the target city for restaurant search."""
        return self.city

    def get_min_rating(self) -> int:
        """Get the minimum acceptable restaurant rating."""
        return self.min_rating

    def get_max_rating(self) -> int:
        """Get the maximum restaurant rating filter."""
        return self.max_rating
    
    def get_radius(self) -> float:
        """
        Calculate search radius based on travel time.
        
        Returns:
            float: Search radius in meters, capped at 20km
        """
        return min(500 * float(self.travel_time), 20000)

    def get_remarks(self) -> str:
        """Get additional search context and user preferences."""
        return self.remarks

    def get_cuisine(self) -> str:
        """Get preferred cuisine types."""
        return self.cuisine

    def get_craving(self) -> str:
        """Get specific food craving or dish preference."""
        return self.craving

    def __str__(self):
        """
        String representation of search criteria for AI processing.
        
        Returns:
            str: Formatted search requirements for AI analysis
        """
        return f"fulfil this requirement {self.remarks}, I am searching for {self.cuisine} cuisine, craving for {self.craving}"

class Restaurant:
    """
    Represents a single restaurant with comprehensive information and AI analysis.
    
    Stores restaurant data from Google Maps API along with AI-generated
    recommendations, meal suggestions, and custom analysis fields.
    """

    def __init__(self, place_id: str, name: str, rating: str, address: str):
        """
        Initialize a Restaurant object with basic information.
        
        Args:
            place_id (str): Google Places API unique identifier
            name (str): Restaurant name
            rating (str): Restaurant rating (e.g., "4.5")
            address (str): Formatted restaurant address
        """
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
        """Get the formatted restaurant address."""
        return self.address

    def get_rating(self) -> str:
        """Get the restaurant rating as a string."""
        return self.rating

    def get_place_id(self) -> str:
        """Get the Google Places API unique identifier."""
        return self.place_id

    def get_name(self) -> str:
        """Get the restaurant name."""
        return self.name

    def add_reviews(self, reviews: str):
        """
        Add customer reviews to the restaurant.
        
        Args:
            reviews (str): Customer review text to append
        """
        self.reviews += reviews

    def get_review(self) -> str:
        """Get all customer reviews for this restaurant."""
        return self.reviews

    def set_photo(self, photo: str):
        """
        Set the restaurant's photo URL.
        
        Args:
            photo (str): URL of the restaurant's photo
        """
        self.photo = photo

    def get_photo(self) -> str:
        """Get the restaurant's photo URL."""
        return self.photo

    def add_restaurant_reason(self,reason: str):
        """
        Add AI-generated reasoning for why this restaurant was recommended.
        
        Args:
            reason (str): AI analysis explaining the recommendation
        """
        self.restaurant_reason += reason

    def get_restaurant_reason(self) -> str:
        """Get the AI-generated recommendation reasoning."""
        return self.restaurant_reason
    
    def add_meal(self, meal: str, meal_citation: str, meal_description: str):
        """
        Add AI-suggested meal information for this restaurant.
        
        Args:
            meal (str): Name of the suggested meal/dish
            meal_citation (str): Citation or source for the meal suggestion
            meal_description (str): Detailed description of the meal
        """
        self.meal += meal
        self.meal_citation += meal_citation
        self.meal_description += meal_description

    def get_meal(self) -> str:
        """Get the AI-suggested meal name."""
        return self.meal

    def get_meal_citation(self) -> str:
        """Get the citation for the meal suggestion."""
        return self.meal_citation

    def get_meal_description(self) -> str:
        """Get the detailed meal description."""
        return self.meal_description

    def add_custom_field(self, key: str, value: str):
        """
        Add a custom analysis field with AI-generated content.
        
        Args:
            key (str): Field name (e.g., "Vegetarian Options")
            value (str): AI-generated analysis for this field
        """
        self.custom_field[key] = value

    def get_custom_field_dict(self):
        """
        Get all custom analysis fields.
        
        Returns:
            Dict[str, str]: Dictionary of custom field names and values
        """
        return self.custom_field

    def get_custom_field(self, key: str) -> str:
        """
        Get a specific custom field value.
        
        Args:
            key (str): Field name to retrieve
            
        Returns:
            str: Field value or empty string if not found
        """
        try:
            return self.custom_field[key]
        except:
            return ""

class RestaurantResult:
    """
    Container for restaurant search results with filtering and management capabilities.
    
    Processes Google Maps API results and creates Restaurant objects for
    selected establishments based on random sampling or filtering criteria.
    """
    
    def __init__(self, filtered_result, random_index: list[int]):
        """
        Initialize restaurant results from filtered Google Maps data.
        
        Args:
            filtered_result: Dictionary of restaurant data from Google Maps API
            random_index (list[int]): List of indices for random restaurant selection
            
        Creates Restaurant objects for each selected establishment with
        basic information from the Google Places API response.
        """
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
        """
        Update the internal restaurant list.
        
        Args:
            restaurant_result (list[Restaurant]): New list of Restaurant objects
        """
        self.restaurant_result = restaurant_result

    def get_list(self) -> list[Restaurant]:
        """
        Get the list of Restaurant objects.
        
        Returns:
            list[Restaurant]: List of all restaurants in the result set
        """
        return self.restaurant_result

    def __len__(self):
        """
        Get the number of restaurants in the result set.
        
        Returns:
            int: Number of restaurants in the collection
        """
        return len(self.restaurant_result)