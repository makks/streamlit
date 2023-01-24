import streamlit
import pandas

streamlit.title('My Parents new healthy dinner')
streamlit.header('Breakfast menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, spinach & rocket Smoothie')
streamlit.text('🐔 Hard-boiled free-range Egg')
streamlit.text('🥑🍞 Advocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
