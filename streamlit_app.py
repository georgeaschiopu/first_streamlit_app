import streamlit
import requests
import panadas


fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.header("Fruityvice Fruit Advice!")





