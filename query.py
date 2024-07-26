"""
This file is responsible for generating prompt for google map to use for the restaurant search.
"""

def get_gemini():
    api_key = os.eviron["GEMINI_SECRET_KEY"]
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel('gemini-1.5-flash')
    return model



def generate_prompt(location, budget, rating_range, craving, cuisine, travel_time, remarks):
    prompt = f"""
    I am looking for a restaurant in {location} with a budget of {budget} and a rating of {rating_range}.
    I am craving {craving} and I am looking for {cuisine} cuisine.
    I am willing to travel for {travel_time} and I want to {remarks}.
    
    """
    try:
        response = model.generate_content(text)
        return response.text
    except:
        return ''