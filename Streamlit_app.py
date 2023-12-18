import streamlit
streamlit.title ('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast ')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

streamlit.header("Fruityvice Fruit Advice!")
import requests
#New Section to Display FruityVice API Response streamlit.header('Fruityvice Fruit Advice!') import requests

fruityvice_repsonse = requests.get("https://fruityvice.com/api/fruit/kiwi") fruityvice_normalized = json_normalize(fruityvice_repsonse.json()) streamlit.dataframe(fruityvice_normalized)

---End of Code


