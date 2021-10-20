import pandas as pd

import streamlit as st

import plotly.express as px


st.title('House Rocket Co.')

st.markdown('Welcome to House Rocker Data Analysis')

st.header('Load Data')

#Read Data
@st.cache(allow_output_mutation=True)
def get_data(path):
    data = pd.read_csv(path)
    data['date'] = pd.to_datetime(data['date'])

    return data
#Load Data
data = get_data('repos/kc_house_data.csv')

#Plot Map
st.title('House Rocket Map')
is_check = st.checkbox('Display Map')

#Filters
price_min = int(data['price'].min())
price_max = int(data['price'].max())
price_mean = int(data['price'].mean())

price_slider = st.slider('Price Range',
                         price_min,
                         price_max,
                         price_mean)

if is_check:
    #select road
    houses = data[data['price'] < price_slider][['id', 'lat', 'long', 'price']]

    st.dataframe(houses)

    #draw_map
    fig1 = px.scatter_mapbox(houses,
                             lat='lat',
                             lon='long',
                             size='price',
                             color_continuous_scale=px.colors.sequential.Inferno,
                             size_max=10,
                             zoom=10)

    fig1.update_layout(mapbox_style='open-street-map')
    fig1.update_layout(height=600, margin={'r': 0, 't': 0, 'l': 0, 'b': 0})
    st.plotly_chart(fig1)

