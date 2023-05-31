import streamlit
import requests
import pandas


fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.header("Fruityvice Fruit Advice!")





