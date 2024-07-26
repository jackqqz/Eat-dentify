"""
Get and manage your llm client here.
If you find yourself getting these model in other file, please move it here.
So we can manage it in one place.
"""

import os
from openai import OpenAI

import google.generativeai as genai

def get_OpenAI():
  api_key = os.environ["OPENAI_SECRET_KEY"]
  model = OpenAI(api_key=api_key)
  return model

def get_Gemini():
  api_key = os.environ["GEMINI_SECRET_KEY"]
  genai.configure(api_key=api_key)
  model = genai.GenerativeModel('gemini-1.5-flash')
  return model

