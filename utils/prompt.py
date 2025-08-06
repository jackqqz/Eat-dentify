"""This file contains the prompts used by the bot to generate responses throughout the application."""


choose_meal = "Analyze this menu image and choose one dish as my meal. If you choose the dish before, don't choose it again. Include why you suggest this meal in point form with emoji. If you cannot identify any dishes, just say that you cannot identify any dish from the menu. Please make sure your result comply with the image, don't make up information"

analyse_cuisine = "Analyze this image and determine the cuisine. Simple answer. List its ingredients, and provide cooking instructions with summary form. Your answer should using point form and emoji, you can also provide the useful video link or article if you find it. Please make sure your result complies with the image, don't make up information."

food_bot = """
You are FoodBot, a knowledgeable and helpful food and restaurant assistant. You have extensive knowledge about various cuisines, cooking techniques, dietary restrictions, and food trends. Provide accurate, engaging, and concise responses to users' food-related queries. If you're unsure about something, it's okay to say so. Aim to be informative and occasionally suggest follow-up questions to engage the user further. If the users ask about meal from a specific restaurant, provide the meal name and short description of the meal. If possible, give the best seller meal from the restaurant. Politely tell that you can't answer any non-food related questions if being asked things not related to food. Provide with short answer. Don't say that you can't identify the image if not asked something related to the image.
"""

nutrition = """
Analyse the image, provide a simple nutritional breakdown. Include:
1. Estimated calories
2. Macronutrients (protein, carbohydrates, fat)
2. Key vitamins and minerals
3. Any potential allergens
4. Overall health assessment of the meal

Present the information in a concise, easy-to-read format using markdown and include emoji.
Only if the image is more that one dish, return 'None'.
"""

chart_data_prompt = """
Return the macronutrient list from your previous answer, you should provide a list of data of macronutrients in the following format. you just need to provide the list, no need to make any explanation. Return the form of 'x, y, z', where x is the protein in x grams, y is the carbs in y grams, and z is the fat in z grams in number. i.e. 2.2, 3.3, 4.4. Approximate number is fine."""

search_prompt = '''
Please generate short and concise text search request for google that include
properties related to restaurant or food that fulfil this requirements. You should not include
the cuisine type in your response (i.e. indian, thai)
Your response should be suitable for their religion.
Include the atmospheric for the position if I mentioned who I am dealing with.
Also consider the weather if provided, if it is raining, recommend indoor venue,
if its hot, recommend air conditional place. You should not ask for additional information. Your response should and must be short, must be vague and must be maximum 4 words only nothing else describing the properties don't use comma and next line. Do not respond my prompt, provide answer only.
for example: quiet vegetarian. Use your imagination and response:
'''

review_summary = '''
provide reasons and a short explaination why this restaurant might be suitable for this situation.
Please be confident on the reviews given, do not question them, treat them as facts.
Do not ask for more information, just use what you have and the rest depends on your imagination.
Include bad reviews too that might be disturbing in this scenario.
Use food emoji in your sentence. Always relate your response to the scenario given. 
You may give example for your explaination
Write it in plane text, use food emoji. Bold important information not title.
You must provide review citation and must apply ' :green-background[place holder] ' if it is a positive review
, :red-background[place holder] ' if it a nagative review based on the requirement (not how does it sound) to your
citation (the exact context of the review not the author) in a new line.
Please trim the citation with '...' if it is too long. If you can't a relavent review, do not mention citation or claim. 
Always include positive review if there is one. Do not sound too negative towards the restaurant.
If the review is a mixture of possitive and negative, you are allowed to split it as two review parts.
You are not allowed to provide citation without this format:
'''

meal_suggestion = """
provide one meal that is suitable for the scenario strictly mentioned in the review.
Food description should be strongly focus on the taste and also include some explaination on why it is suitable. 
Include the dish name in your description
Provide review citation (the context not the author).
Output your response
in the format of food name | review citation | food description / explaination.\n
something like this: sushi | the sushi here is great! | Sushi is a strong flavor but is largely neutral, tangy, and sweet Japanese dish of prepared vinegared rice.
If you can't, return None | None | None. Don't generate table 
"""

column_prompt = '''
provide reasons and a short explaination. Please be confident on the reviews given, do not question them, treat them as facts
Do not ask for more information, just use what you have and the rest depends on your imagination.
for your explaination
Write it in plane text, use food emoji. Bold important information not title.
You must provide review citation and must apply ' :green-background[place holder] ' if it is a positive review
, :red-background[place holder] ' if it a nagative review based on the requirement (not how does it sound) to your citation 
(the exact context of the review not the author) in a new line. Do not continue the previous sentence. Please trim the citation with '...'
if it is too long. You are not allowed to provide citation without this format. If you can't a relavent review, do not mention citation.
Logical assumption based on the review that didn't explicitly mentioned in the review can be made.
If the review is a mixture of possitive and negative, you are allowed to split it as two review parts.
'''