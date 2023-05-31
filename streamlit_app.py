import streamlit
import requests
import pandas
import snowflake.connector

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response=requests.get('https://fruityvice.com/api/fruit/'+fruit_choice)




