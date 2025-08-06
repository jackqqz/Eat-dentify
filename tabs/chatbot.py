import streamlit as st
import PIL.Image
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np

from utils.style import chat_bot
from utils.prompt import choose_meal, analyse_cuisine, food_bot, nutrition, chart_data_prompt
from utils.utils import response_imageOpenAI
from utils.llm_api import get_OpenAI


def food_suggestion_chatbot():
    """
    Main function for the food suggestion chatbot interface.
    
    Creates a comprehensive chatbot interface that allows users to:
    - Ask food-related questions via text input
    - Upload images of food/menus for analysis
    - Take pictures using camera input
    - Get meal recommendations, recipes, and nutrition analysis
    - Access personalized suggestions based on user remarks/preferences
    
    The function handles chat history, user authentication state, and provides
    multiple interaction modes including text chat and image analysis buttons.
    """
    st.info("""
        **Foodbot answers all your food-related questions!** 
        \n 🥸 Simply ask about any food topic, and it will provide the answers you need. 
        \n 🥪 You can also upload an image to get information. 
        \n 📝 Upload your menu to get recommendations.
        \n 🍜 Ask for recipes of dishes you like. 
        \n 📊 Consult Foodbot for nutritional information and learn more about your food!
    """)
    chat_bot()

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    chat_container = st.container()

    # Display chat messages from history on app rerun
    with chat_container:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"], unsafe_allow_html=True)

    df = None
    prompt = st.chat_input("What would you like to know about food?",
                           key="user_input")

    # personalized chatbox
    remarks_prompt = ""
    if st.session_state.logged_in:
        remarks_prompt = "Also, your answer should based on the remarks: " + st.session_state.user_remarks + ". For example, if the remarks consist vegeterian, if the image or question consist meat, you should notify the user. Since you are talking to the user, remember use you but not general."

    if 'image' not in st.session_state:
        st.session_state.image = None

    # Camera input
    if st.checkbox("Click to Take Picture!"):
        img_file_buffer = st.camera_input("Take a picture")
        if img_file_buffer:
            st.session_state.image = PIL.Image.open(img_file_buffer)

    # File upload
    uploaded_file = st.file_uploader(
        "Upload your menu or dish, ask any question in the input box or click the button below 🤖",
        type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        st.session_state.image = PIL.Image.open(uploaded_file)

    # Read image
    if st.session_state.image:

        button_container = st.container()
        col1, col2, col3 = st.columns(3)

        with button_container:
            # meal hunt button
            if col1.button("Meal Hunt!", use_container_width=True):
                with st.spinner("Hunting For You..."):
                    if remarks_prompt != "":
                        msg = choose_meal + "Choose the meal based on the remarks: " + st.session_state.user_remarks
                    else:
                        msg = choose_meal
                    analysis = analyze_food_image(st.session_state.image, msg)
                    message = f"Based on the image you uploaded: \n{analysis}"
                    append_message(chat_container, "assistant", message)

            # recipe button
            if col2.button("Ask for recipe", use_container_width=True):
                with st.spinner("Analyzing Cuisine..."):
                    msg = analyse_cuisine + remarks_prompt
                    cuisine_analysis = analyze_food_image(
                        st.session_state.image, msg)
                    message = f"Cuisine Analysis: \n{cuisine_analysis}"
                    append_message(chat_container, "assistant", message)

            # nutrition button
            if col3.button("Analyze Nutrition", use_container_width=True):
                with st.spinner("Analyzing Nutrition..."):
                    nutrition_info, chart_data = analyze_nutrition(
                        st.session_state.image, remarks_prompt)
                    message = f"Nutrition Analysis: \n{nutrition_info}"
                    append_message(chat_container, "assistant", message)
                    if chart_data:
                        display_nutrition_chart(chat_container, chart_data)

            st.markdown('</div>', unsafe_allow_html=True)

    if prompt:
        append_message(chat_container, "user", prompt)

        with st.spinner("Thinking..."):
            if st.session_state.image is not None:
                input = f"Strictly based on the image, assist me with: {prompt}. don't make up information and don't ever mention the image. Don't tell that you can or cannot identify the image if not asked something related to the image." + remarks_prompt
                response = analyze_food_image(st.session_state.image, input)
            else:
                msg = prompt + remarks_prompt
                response = generate_food_bot_response(msg)

        append_message(chat_container, "assistant", response)

        # Scroll to the bottom
        st.markdown(
            '<script>window.scrollTo(0, document.body.scrollHeight);</script>',
            unsafe_allow_html=True)

    if df is not None:
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Macronutrients Distribution")
            st.bar_chart(df)

        with col2:
            st.subheader("Macronutrients Breakdown")
            st.table(df)


def generate_food_bot_response(prompt):
    """
    Generate AI-powered responses to food-related text queries.
    
    Args:
        prompt (str): User's text input/question about food
        
    Returns:
        str: AI-generated response about food topics, recipes, nutrition, etc.
        
    Uses OpenAI's GPT-4o model with chat history context to provide coherent,
    conversational responses. Includes the last 5 messages for context continuity.
    """
    client = get_OpenAI()

    # Include the chat history for context
    messages = [{"role": "system", "content": food_bot}]
    for message in st.session_state.messages[
            -5:]:  # Include last 5 messages for context
        messages.append({
            "role": message["role"],
            "content": message["content"]
        })
    messages.append({"role": "user", "content": prompt})

    completion = client.chat.completions.create(
        model="gpt-4o",  # Using a more capable model
        messages=messages,
        max_tokens=300,  # Adjust as needed
        temperature=0.7,  # Slightly more creative
    )

    return completion.choices[0].message.content


def analyze_nutrition(image, remarks_prompt):
    """
    Analyze nutritional content of food from an uploaded image.
    
    Args:
        image: PIL Image object of food/meal to analyze
        remarks_prompt (str): User's dietary preferences/restrictions
        
    Returns:
        tuple: (nutrition_info, chart_data) where:
            - nutrition_info (str): Detailed nutritional breakdown text
            - chart_data (list): Macronutrient values for chart visualization
            
    Extracts nutritional information and macronutrient data (protein, carbs, fat)
    from food images for both text analysis and chart generation.
    """
    msg = nutrition + remarks_prompt
    nutrition_info = response_imageOpenAI(msg, image)

    if nutrition_info.strip() == 'None':
        return "Unfortunately, I can't provide a nutrition breakdown for this image because it contains multiple dishes.", None

    chart_data_str = response_imageOpenAI(chart_data_prompt, image)

    chart_data = [
        float(x) for x in chart_data_str.replace('\n', '').split(', ')
    ]

    return nutrition_info, chart_data


def analyze_food_image(image, input):
    """
    Perform general food image analysis based on user input.
    
    Args:
        image: PIL Image object to analyze
        input (str): Specific analysis request (recipe, identification, etc.)
        
    Returns:
        str: Analysis results in point form with emojis for visualization
        
    Acts as a versatile food image analyzer that can handle various requests
    like recipe suggestions, food identification, meal recommendations, etc.
    Provides concise, emoji-enhanced responses.
    """
    prompt = f"You're a food suggestion bot, analyze the image. {input} .If you think the question is not asking about the image, just answer like a knowledgeable and helpful food and restaurant assistant and don't ever mention about the image. Your answer should be in point form and concise, plus emoji to help visualize."
    return response_imageOpenAI(prompt, image)


def display_nutrition_chart(chat_container, chart_data):
    """
    Display interactive nutrition charts in the chat interface.
    
    Args:
        chat_container: Streamlit container for chat messages
        chart_data (list): List of 3 macronutrient values [protein, carbs, fat]
        
    Creates and displays both pie chart and bar chart visualizations of
    macronutrient distribution. Shows exact values in a styled DataFrame.
    Handles data validation and provides user-friendly error messages.
    """
    # Ensure the data is a list of three numbers
    if not isinstance(chart_data, list) or len(chart_data) != 3:
        st.write(
            "Not enough data to display a chart or incorrect data format.")
        return

    # Labels for the macronutrients
    labels = ['Protein', 'Carbohydrates', 'Fat']

    # Custom colors for the charts
    colors = ['#8BC1F7', '#06C', '#004B95']

    with chat_container:
        with st.chat_message("assistant"):
            # Create two columns
            col1, col2 = st.columns(2)

            with col1:
                # Create a pie chart with custom colors
                fig_pie, ax_pie = plt.subplots()
                ax_pie.pie(chart_data,
                           labels=labels,
                           autopct='%1.1f%%',
                           startangle=90,
                           colors=colors)
                ax_pie.axis(
                    'equal'
                )  # Equal aspect ratio ensures that pie is drawn as a circle
                plt.title("Macronutrient Distribution (Pie Chart)")
                st.pyplot(fig_pie)

            with col2:
                # Create a DataFrame for the bar chart
                df = pd.DataFrame({'Nutrient': labels, 'Grams': chart_data})
                df = df.set_index('Nutrient')

                # Display the bar chart using st.bar_chart with a color map
                st.subheader("Macronutrient Distribution (Bar Chart)")
                st.bar_chart(df, use_container_width=True, color="#004B95")

                # Display the exact values
                st.write("Exact values:")
                st.write(df.style.background_gradient(cmap='Blues'))


def append_message(chat_container, role, content):
    """
    Add a new message to the chat interface and session state.
    
    Args:
        chat_container: Streamlit container for displaying chat messages
        role (str): Message sender role ('user' or 'assistant')
        content (str): Message content to display and store
        
    Appends messages to both the visual chat interface and session state
    for persistence across app reruns. Supports HTML content rendering.
    """
    # st.toast(content)
    with chat_container:
        st.chat_message(role).markdown(content, unsafe_allow_html=True)
        st.session_state.messages.append({
            "role": role,
            "content": f"{content}"
        })
