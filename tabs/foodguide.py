import streamlit as st
from utils.article import get_article_info, display_article_card
from utils.config import articles
from utils.style import display_cards

def display_foodguide():
  st.header("Latest Food Articles")
  display_cards()
  num_columns = min(3, len(articles))  

  # Display articles in rows
  for i in range(0, len(articles), num_columns):
      cols = st.columns(num_columns)
      for j in range(num_columns):
          if i + j < len(articles):
              title, img_url, summary = get_article_info(articles[i + j])
              with cols[j]:
                  display_article_card(title, img_url, summary, articles[i + j])