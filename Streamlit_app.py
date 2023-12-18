import streamlit
streamlit.title ('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast ')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ "kiwi")
streamlit.text(fruityvice_response)
streamlit.header("Fruityvice Fruit Advice!")
# write your own comment -what does the next line do? 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)


