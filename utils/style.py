"""This file contains functions to apply custom styles to Streamlit components."""

import streamlit as st

def restaurant_style():
    st.markdown("""
    <style>
    .restaurant-card {
        background-color: #F0F2F6;
        border-radius: 5px;
        padding: 20px;
        margin-bottom: 20px;
        transition: transform 0.3s ease-in-out;
        overflow: hidden;
    }
    .restaurant-card:hover {
        transform: translateY(-5px);
    }
    .restaurant-image-container {
        width: 100%;
        height: 100%;
        overflow: hidden;
        border-radius: 5px;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        transition: transform 0.3s ease-in-out;
    }
    .restaurant-image-container:hover {
        transform: translateY(-5px);
    }
    .restaurant-image {
        width: 100%;
        height: auto;
        object-fit: cover;
    }
    .restaurant-name {
        font-size: 30px;
        font-weight: bold;
        margin-bottom: 10px;
        color: #1E1E1E;
    }
    .map-button {
        display: inline-flex;
        align-items: center;
        padding: 8px 16px;
        margin-right: 10px;
        text-decoration: none;
        color: white !important;
        border-radius: 5px;
        font-weight: normal !important;
        transition: background-color 0.3s ease;
    }
    .map-button img {
        width: 20px;
        height: 20px;
        margin-right: 8px;
    }
    .google-maps-button {
        background-color: #0F9D58;
    }
    .google-maps-button:hover {
        background-color: #009d48;
    }
    .waze-button {
        background-color: #33ccff;
    }
    .waze-button:hover {
        background-color: #28A8D8;
    }
    </style>
    """, unsafe_allow_html=True)
    

def light_theme():
  
  st.markdown("""
  <style>
  .rounded-image {
      border-radius: 15px;
  }
  .big-font {
      font-size:50px !important;
      font-weight: bold;
      # color: #f0f0f0;
      font-family: Times New Roman !important;
  }
  .stButton>button {
      color: white;
      font-weight: bold;
      background-color: #262730;
      border-radius: 10px;
      padding: 10px 24px;
      border: 2px solid #000000;
      transition: all 0.3s ease;
      box-shadow: 0 2px 5px rgba(0,0,0,0.1);
  }
  .stButton > button:hover {
      color: white;
      background-color: #262730;
      border-color: #3498db;
      transform: translateY(-2px);
      box-shadow: 0 4px 8px rgba(0,0,0,0.2);
      border: 2px solid #000000;
  }
  .stButton > button:active {
      color: white;
      background-color: #262730;
      transform: translateY(0);
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  }  
  .stLinkButton> a {
      color: white !important;
      font-weight: bold !important;
      background-color: #262730 !important;
      border-radius: 10px !important;
      padding: 10px 24px !important;
      border: 2px solid #000000 !important;
      transition: all 0.3s ease !important;
      box-shadow: 0 2px 5px rgba(0,0,0,0.1) !important;
  }
  .stLinkButton > a:hover {
      color: white !important;
      background-color: #262730 !important;
      border-color: #3498db !important;
      transform: translateY(-2px) !important;
      box-shadow: 0 4px 8px rgba(0,0,0,0.2) !important;
      border: 2px solid #000000 !important;
  }
  .stLinkButton > a:active {
      color: white !important;
      background-color: #000000 !important;
      transform: translateY(0) !important;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1) !important;
  }
  .stTabs {
      width: 100%;
  }
  .stTabs [data-baseweb="tab-list"] {
      gap: 10px;
  }
  .stTabs [data-baseweb="tab"] {
      height: 50px;
      white-space: pre-wrap;
      background-color: #F0F2F6;
      border-radius: 10px;
      color: #4F4F4F;
      font-size: 14px;
      font-weight: 400;
      align-items: center;
      justify-content: center;
      flex: 1;
      gap: 5px;
      padding: 0 10px;
      min-width: 120px;
  }
  .stTabs [aria-selected="true"] {
      background-color: #262730 !important;
      color: white !important;
  }
  .stTabs [data-baseweb="tab-highlight"] {
      display: none;
  }
  div[aria-hidden="true"] {
      display: none;
  }
  div[data-testid="stNotification"] {
      background-color: #F0F2F6 !important;
  }
  .stTabs [data-baseweb="tab-list"] {
      gap: 10px;
      overflow-x: auto;
      flex-wrap: nowrap;
      scrollbar-width: none;  /* Firefox */
      -ms-overflow-style: none;  /* Internet Explorer 10+ */
  }
  .stTabs [data-baseweb="tab-list"]::-webkit-scrollbar {
      display: none;  /* WebKit */
  }
  [data-testid="stThumbValue"] {
    margin-top: 2rem !important;
  }
  [data-baseweb="slider"] > div > div {
      background-color: #D9DDE5 !important;
      height: 20px !important;
      border-radius: 6px !important;
  }
  [data-baseweb="slider"] [role="slider"] {
      width: 0 !important;
      height: 0 !important;
      border: none !important;
      box-shadow: none !important;
  }
  [data-testid="stTickBar"] {
      display: none !important;
  }
  </style>
  """, unsafe_allow_html=True)

  st.markdown('<p class="big-font">Eat-dentify 🍽️</p>', unsafe_allow_html=True)

    
  st.write("Don't know what to eat? Let us help you decide!")

def dark_theme():

  st.markdown("""
  <style>
  .rounded-image {
      border-radius: 15px;
  }
  .big-font {
      font-size:50px !important;
      font-weight: bold;
      # color: #f0f0f0;
      font-family: Times New Roman !important;
  }
  .stButton>button {
      color: white;
      font-weight: bold;
      background-color: #FF4B4B;
      border-radius: 10px;
      padding: 10px 24px;
      border: 2px solid #000000;
      transition: all 0.3s ease;
      box-shadow: 0 2px 5px rgba(0,0,0,0.1);
  }
  .stButton > button:hover {
      color: white;
      background-color: #FF4B4B;
      border-color: #3498db;
      transform: translateY(-2px);
      box-shadow: 0 4px 8px rgba(0,0,0,0.2);
      border: 2px solid #000000;
  }
  .stButton > button:active {
      color: white;
      background-color: #FF4B4B;
      transform: translateY(0);
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  }  
  .stLinkButton> a {
      color: white !important;
      font-weight: bold !important;
      background-color: #FF4B4B !important;
      border-radius: 10px !important;
      padding: 10px 24px !important;
      border: 2px solid #000000 !important;
      transition: all 0.3s ease !important;
      box-shadow: 0 2px 5px rgba(0,0,0,0.1) !important;
  }
  .stLinkButton > a:hover {
      color: white !important;
      background-color: #FF4B4B !important;
      border-color: #3498db !important;
      transform: translateY(-2px) !important;
      box-shadow: 0 4px 8px rgba(0,0,0,0.2) !important;
      border: 2px solid #000000 !important;
  }
  .stLinkButton > a:active {
      color: white !important;
      background-color: #000000 !important;
      transform: translateY(0) !important;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1) !important;
  }
  .stTabs {
      width: 100%;
  }
  .stTabs [data-baseweb="tab-list"] {
      gap: 10px;
  }
  .stTabs [data-baseweb="tab"] {
      height: 50px;
      white-space: pre-wrap;
      background-color: #262730;
      border-radius: 10px;
      color: #D3D3D3;
      font-size: 14px;
      font-weight: 400;
      align-items: center;
      justify-content: center;
      flex: 1;
      gap: 5px;
      padding: 0 10px;
      min-width: 120px;
  }
  .stTabs [aria-selected="true"] {
      background-color: #FF4B4B !important;
      color: white !important;
  }
  .stTabs [data-baseweb="tab-highlight"] {
      display: none;
  }
  div[aria-hidden="true"] {
      display: none;
  }
  div[data-testid="stNotification"] {
      background-color: #262730 !important;
  }
  .stTabs [data-baseweb="tab-list"] {
      gap: 10px;
      overflow-x: auto;
      flex-wrap: nowrap;
      scrollbar-width: none;  /* Firefox */
      -ms-overflow-style: none;  /* Internet Explorer 10+ */
  }
  .stTabs [data-baseweb="tab-list"]::-webkit-scrollbar {
      display: none;  /* WebKit */
  }  
  [data-testid="stThumbValue"] {
    margin-top: 2rem !important;
  }
  [data-baseweb="slider"] > div > div {
      background-color: rgb(0, 0, 0, 225) !important;
      height: 20px !important;
      border-radius: 6px !important;
  }
  [data-baseweb="slider"] [role="slider"] {
      width: 0 !important;
      height: 0 !important;
      border: none !important;
      box-shadow: none !important;
  }
  [data-testid="stTickBar"] {
      display: none !important;
  }
  
  </style>
  """, unsafe_allow_html=True)

  st.markdown('<p class="big-font">Eat-dentify 🍽️</p>', unsafe_allow_html=True)


  st.write("Don't know what to eat? Let us help you decide!")

def chat_bot():
  st.markdown("""
  <style>
  .stChatFloatingInputContainer {
      position: fixed;
      bottom: 0;
      background-color: white;
      padding: 1rem;
      z-index: 1000;
      width: 100%;
  }
  .stChatMessageContainer {
      margin-bottom: 5rem;
  }
  .stChatMessage {
      margin-bottom: 1rem;
  }
  </style>
  """, unsafe_allow_html=True)

  st.subheader("Chat with FoodBot 🍽️")
  st.chat_message("assistant").markdown("Hello! I'm FoodBot, your personal food suggestion assistant. Ask me anything about food, restaurants, or cuisines!")

# def buttons_foodBot():
#     st.markdown("""
#       <style>
#           .stButton > button {
#               display: inline-block;
#               font-weight: 400;
#               color: #6c757d;
#               text-align: center;
#               vertical-align: middle;
#               cursor: pointer;
#               background-color: transparent;
#               border: 1px solid #6c757d;
#               padding: .375rem .75rem;
#               font-size: 1rem;
#               line-height: 1.5;
#               border-radius: .25rem;
#               transition: color .15s ease-in-out,background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out;
#               margin: 0 10px;
#           }
#           .stButton > button:hover {
#               color: #fff;
#               background-color: #6c757d;
#               border-color: #6c757d;
#           }
#           .button-container {
#               display: flex;
#               justify-content: center;
#               align-items: center;
#               gap: 10px;
#           }
#       </style>
#       """, unsafe_allow_html=True)

def display_cards():
    st.markdown("""
      <style>
      .article-card {
          background-color: rgb(240, 242, 246);
          border-radius: 10px;
          padding: 15px;
          margin-bottom: 20px;
          height: 450px;
          display: flex;
          flex-direction: column;
          transition: transform 0.3s ease-in-out;
      }
      .article-card:hover {
          transform: translateY(-5px);
      }
      .article-image {
          width: 100%;
          height: 200px;
          object-fit: cover;
          border-radius: 5px;
      }
      .article-title {
          font-weight: bold;
          margin-top: 10px;
          font-size: 1em;
      }
      .article-summary {
          font-size: 0.9em;
          color: #31333F;
          flex-grow: 1;
          overflow: hidden;
          margin-bottom: 10px;
      }
      .article-title {
          color: #31333F
      }

      </style>
      """, unsafe_allow_html=True)