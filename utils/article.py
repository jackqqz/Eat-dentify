from bs4 import BeautifulSoup
import requests
import streamlit as st
from streamlit_theme import st_theme


def get_article_info(url):
  try:
      response = requests.get(url)
      soup = BeautifulSoup(response.content, 'html.parser')

      # Extract title
      title = soup.find('h1').text.strip() if soup.find('h1') else "No title found"

      # Extract image
      img = soup.find('meta', property='og:image')
      img_url = img['content'] if img else "https://via.placeholder.com/300x200.png?text=No+Image"

      # Extract summary (first paragraph or meta description)
      summary = soup.find('meta', property='og:description')
      if summary:
          summary = summary['content']
      else:
          summary = soup.find('p').text.strip() if soup.find('p') else "No summary available"

      return title, img_url, summary[:200] + "..."  # Truncate summary to 200 characters
  except Exception as e:
      st.error(f"Error fetching article info: {str(e)}")
      return "Error fetching article", "https://via.placeholder.com/300x200.png?text=Error", "Could not fetch article information"

def display_article_card(title, img_url, summary, article_url):
  st.markdown(f"""
  <div class="article-card">
      <img src="{img_url}" class="article-image">
      <div class="article-title">{title}</div>
      <div class="article-summary">{summary}</div>
      <a href="{article_url}" target="_blank" style="
          text-decoration: none;
          color: #4A4A4A;
          background-color: #D3D3D3;
          padding: 8px 16px;
          border: 1px solid #B3CDE0;
          border-radius: 5px;
          display: inline-block;
          width: 100%;
          text-align: center;
          font-size: 0.9em;
          transition: background-color 0.3s, color 0.3s;
      ">
          Read the full article
      </a>
  </div>
  """, unsafe_allow_html=True)