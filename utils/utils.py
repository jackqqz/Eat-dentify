import streamlit as st
import random
from utils.config import food_facts
import os
import re
import io
import base64
from openai import OpenAI

from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
import google.generativeai as genai

def get_OpenAI():
  api_key = os.environ["OPENAI_SECRET_KEY"]
  return ChatOpenAI(api_key = api_key, model="gpt-4o", temperature=1.0, max_tokens=100)

# def get_gemini():
#   api_key = os.environ["GEMINI_SECRET_KEY"]
#   genai.configure(api_key=api_key)
#   return genai.GenerativeModel('gemini-1.5-flash')

def response_imageOpenAI(prompt, image):
  api_key = os.environ["OPENAI_SECRET_KEY"]
  client = OpenAI(api_key=api_key)

  # Convert the image to base64
  buffered = io.BytesIO()
  image.save(buffered, format="PNG")
  image_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')

  try:
      response = client.chat.completions.create(
          model="gpt-4o",
          messages=[
              {
                  "role": "user",
                  "content": [
                      {"type": "text", "text": prompt},
                      {
                          "type": "image_url",
                          "image_url": {
                              "url": f"data:image/png;base64,{image_base64}"
                          }
                      }
                  ]
              }
          ],
          max_tokens=500
      )
      return response.choices[0].message.content if response.choices[0].message.content else "I'm sorry, I couldn't analyze the image. Please try again."
    
  except Exception as e:
    return "I'm sorry, I couldn't analyze the image. Please try again."

def initialize_langchain():
  client = get_OpenAI()
  memory = ConversationBufferMemory(size=4)
  buffer_chain = ConversationChain(llm=get_OpenAI(), memory=memory, verbose = True)
  return {
      "client": client,
      "memory": memory,
      "buffer_chain": buffer_chain
  }

def get_random_food_fact():
  return random.choice(food_facts)

def preprocess_restaurant_name(name):
    return re.sub(r'^\d+\.\s*', '', name).strip()


