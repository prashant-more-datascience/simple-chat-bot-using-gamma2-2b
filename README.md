# simple-chat-bot-using-gamma2-2b

Chat Bot Using Gamma2 Model
This project demonstrates a simple chatbot application built using the Gamma2:2B language model, powered by the langchain library and integrated with Streamlit for a user-friendly interface. The chatbot acts as an intelligent assistant, providing the best possible answers to user queries.

Features
Language Model: Utilizes the Gamma2:2B model via the langchain_community.llms.Ollama package.
Dynamic Prompting: Implements a customizable prompt template using ChatPromptTemplate from langchain_core.prompts.
Streamlit Interface: Offers a clean and interactive user interface for real-time interaction with the chatbot.
Output Parsing: Ensures structured and clean responses using langchain_core.output_parsers.StrOutputParser.
Project Highlights
Customizable Assistant Behavior: The chatbot is designed to adapt based on the prompt instructions provided to it.
Real-Time Interaction: Users can input their questions and receive answers instantly through the Streamlit UI.
Environment Configuration: Uses dotenv for secure and flexible management of API keys and environment variables.


Prerequisites
Python 3.8+

Required Libraries:
langchain
langchain_community
langchain_core
streamlit
python-dotenv

Environment Variables: Ensure the following variables are set in a .env file:
LANGCHAIN_API_KEY
LANGCHAIN_PROJECTNAME
