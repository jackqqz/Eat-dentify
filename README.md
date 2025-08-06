# Eat-dentify

**AI-Powered Natural Language Restaurant Discovery Platform**

Eat-dentify is a fully responsive web application built using Streamlit with custom HTML and CSS integration that addresses a critical gap in food discovery technology. While traditional restaurant review applications rely on rigid category-based searches, this platform enables users to search for meals and matching restaurants using natural language queries, providing the flexible search capabilities that current market solutions lack.

The application integrates Google Places API with multiple Large Language Model APIs and implements custom filtering logic to match results with specific dietary needs and preferences. This approach fundamentally improves meal planning and decision-making processes in ways that traditional review applications cannot achieve.

## Demo

### Login & Profile

Comprehensive account management and preference customization interface.
`<img width="2940" height="1840" alt="image" src="https://github.com/user-attachments/assets/0743d50e-840c-4247-9204-9576be2eda41" />`

### Search Flows

Natural language restaurant and meal discovery demonstration.
`<img width="2940" height="1840" alt="image" src="https://github.com/user-attachments/assets/58b9b839-9fd2-493d-8bbb-0218d6f4a14b" />`
`<img width="3840" height="2160" alt="image" src="https://github.com/user-attachments/assets/e95c6b1a-a33a-4bd5-ac25-6b177790e98c" />`
`<img width="2940" height="1840" alt="image" src="https://github.com/user-attachments/assets/a828e366-7c94-4381-8555-b20cbc9d19f4" />`

### FoodBot Interactions

Multi-modal AI assistant showcasing image analysis and conversational capabilities.
`<img width="2940" height="1840" alt="image" src="https://github.com/user-attachments/assets/b72e858c-eac9-420b-9862-f54cc9e9168d" />`

### Video Explanation

Comprehensive demonstration of platform capabilities and user workflows
https://drive.google.com/file/d/17SG41PXatlIYbOj8pGmprhCzGAGc2Azd/view?usp=sharing

## Core Functionality

### Natural Language Food Discovery

The platform processes complex food-related queries expressed in natural language, transforming user intent into actionable restaurant and meal recommendations. Users can search using contextual phrases rather than being constrained to predefined categories.

### Multi-Modal Image Analysis

Users can upload food images to receive comprehensive recipe information, detailed nutritional analysis, and follow-up question capabilities. The system processes visual food data to provide actionable culinary insights.

### Review-Based Intelligence

The application analyzes restaurant reviews to generate specific meal recommendations and answer targeted questions about menu items and dining experiences, leveraging crowd-sourced information for personalized suggestions.

### Adaptive Filtering System

Custom logic processes dietary restrictions, preferences, and nutritional requirements to filter search results beyond simple keyword matching, enabling complex preference-based recommendations.

## Key Features

### User Profile Management

- Secure authentication system with guest access options
- Customizable user profiles supporting dietary restrictions and preferences
- Persistent preference storage for personalized experiences

### AI-Enhanced Restaurant Search

- Natural language query processing for restaurant discovery
- Advanced filtering by location, price range, rating, and travel time
- Real-time integration with Google Places API for current restaurant data

### Intelligent Meal Recommendations

- AI-generated meal suggestions based on restaurant reviews and user preferences
- Nutritional analysis and dietary compliance checking
- Citation-backed recommendations with transparent sourcing

### Interactive Food Assistant

- Conversational AI interface for food-related inquiries
- Image-to-recipe conversion with nutritional breakdown
- Interactive nutrition charts and visual data representation
- Follow-up question capabilities for detailed food information

### Responsive User Interface

- Cross-platform compatibility with mobile and desktop optimization
- Dynamic theming with light and dark mode support
- Progressive loading indicators for AI processing tasks

## Project Structure

```
Eat-dentify/
│
├── pages/                          # Main application entry points
│   ├── eatdentify.py              # Primary application interface with tab navigation
│   └── login.py                   # Authentication system and database initialization
│
├── tabs/                          # Modular interface components
│   ├── restaurant.py              # Restaurant search and display interface
│   ├── meal.py                    # Meal recommendation presentation
│   ├── chatbot.py                 # AI-powered conversational interface
│   ├── foodguide.py               # Article and guide display system
│   ├── sidebar.py                 # Search parameter and filter interface
│   ├── profile.py                 # User account management
│   └── signup.py                  # Registration and authentication utilities
│
├── utils/                         # Core system utilities
│   ├── data_structures.py         # Data models and object definitions
│   ├── google_map_api.py          # Google Places API integration
│   ├── restaurant_ai.py           # AI processing pipeline for restaurants
│   ├── llm_api.py                 # Large Language Model API management
│   ├── article.py                 # Web scraping and content processing
│   ├── style.py                   # CSS styling and theme management
│   ├── config.py                  # Application configuration constants
│   ├── prompt.py                  # AI prompt engineering templates
│   └── utils.py                   # General utility functions
│
├── .streamlit/                    # Streamlit configuration
│   ├── config.toml               # Application configuration settings
│   └── Eat-dentify_manual.png    # Documentation assets
│
├── requirements.txt               # Python dependency specifications
└── README.md                     # Project documentation
```

### Architecture Components

#### Application Layer

- **Main Interface**: Central hub managing navigation, theme switching, and session state
- **Authentication System**: Secure user management with SQLite database integration

#### User Interface Layer

- **Restaurant Display**: Interactive cards with mapping integration and custom analysis
- **Meal Presentation**: AI-generated recommendations with expandable details
- **Conversational Interface**: Multi-modal AI assistant supporting text and image inputs
- **Content Management**: Responsive article grid with web scraping capabilities
- **Search Interface**: Comprehensive filtering with geolocation services
- **Profile Management**: Secure user account and preference management

#### Core Logic Layer

- **Data Management**: Structured models for restaurants, user inputs, and search results
- **API Integration**: Google Maps Places API for location and restaurant data
- **AI Processing**: Multi-model pipeline for restaurant analysis and recommendations
- **Content Processing**: Web scraping and article management systems
- **Styling System**: Dynamic CSS with responsive design capabilities

## Technical Implementation

### API Integration

- Google Places API for restaurant data, photos, and location services
- OpenAI GPT-4o for natural language processing and conversational capabilities
- Google Gemini Pro for specialized food analysis and recommendation generation

### Data Processing

- Custom filtering algorithms for dietary preference matching
- Real-time image analysis for recipe and nutrition extraction
- Review sentiment analysis for restaurant recommendation scoring

### User Experience

- Progressive web application features with offline capability consideration
- Responsive design optimized for mobile and desktop platforms
- Real-time status updates for all AI processing operations

## Technologies

- **Framework**: Streamlit with custom HTML/CSS integration
- **AI & NLP**: OpenAI GPT-4o, Google Gemini Pro for specialized food analysis
- **APIs**: Google Places API for restaurant data and location services
- **Database**: SQLite for user management and preference storage
- **Data Processing**: Pandas, BeautifulSoup, Matplotlib for data analysis and visualization
- **Documentation**: Comprehensive project documentation available at Notion workspace

## License

This project is licensed under the MIT License.

---
