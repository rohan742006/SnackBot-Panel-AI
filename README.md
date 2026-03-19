# SnackBot 🍔🤖

**SnackBot** is an AI-powered chatbot for snack and beverage shops.  
It allows users to browse the menu, place orders, choose pickup or delivery, and even collect payments — all via a conversational interface.

## Features
- Interactive chat interface for ordering snacks, drinks, sides, and desserts  
- Menu browsing with prices displayed  
- Suggests combos and extras  
- Handles pickup 🏃‍♂️ and delivery 🛵  
- Summarizes full order before checkout 📝  
- Collects payment via UPI  
- Friendly and conversational bot personality 😄  

## Tech Stack
- Python  
- Panel – for the chat interface  
- OpenAI / OpenRouter API – for AI responses  

## Learning Highlights
While building SnackBot, I explored **Prompt Engineering** and learned about:  
1. **Context** – providing AI the necessary background (used to define bot behavior and menu)  
2. **Role** – defining how AI should respond  
3. **Expectations** – specifying the style and type of output  

## Setup & How to Run
1. Clone the repository:

**#bash**
git clone https://github.com/rohan742006/SnackBot-Panel-AI.git
cd SnackBot-Panel-AI

Install dependencies, add your OpenAI API key, and run the app:
pip install -r requirements.txt

# In app.py, replace the placeholder with your OpenAI key:
OPENAI_API_KEY = "your_openai_api_key_here"

**# Serve the Panel app**:
panel serve app.py

**Credits**
Special thanks to instructors who inspired this learning journey:
Isa Fulford – Member of Technical Staff, OpenAI
Andrew Ng – Founder, DeepLearning.AI; Co-founder, Coursera

**License**
This project is open-source and free to use.

**Hashtags**
#AI #Chatbot #PromptEngineering #Python #OpenAI #Panel #OpenRouter #DeepLearning #MachineLearning #SnackBot #AIProjects #TechLearning #AndrewNg #IsaFulford #Innovation
