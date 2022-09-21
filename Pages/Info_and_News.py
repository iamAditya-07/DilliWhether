import streamlit as st
from PIL import Image

st.title("Delhi Weather And Transport")

st.header('LATEST NEWS')
st.subheader('Dated : 20Sept.2022')

image = Image.open('img4.jpg')
st.image(image, caption='On September 15, the average 24-hour AQI was 75')

st.markdown('Only three days after the city saw its first day of good air quality in 2022, Delhis air quality began to deteriorate. **At 4 pm on September 19**, the citys 24-hour average air quality index (AQI) was **182**, according to data. On September 18, it was **119**, on the previous day, **70**, and on September 16, **47**. **Anand Vihar** was the most polluted area in the capital with an AQI of 405 on September 18. The first "good" air quality day of the year was brought on by a prolonged period of light rain on September 16 in the capital.')

st.header('OTHER INFO')
image = Image.open('img1.jpg')
st.image(image, caption='Temp. change in recent years')

image = Image.open('img5.jpg')
st.image(image, caption='Transport Vehicles')

st.markdown('The present study focusses on the different exposure levels recorded by  commuters  using  six modes  of transport  in  Delhi  and  the results showed  that  travellers  in  open  modes  of  transport  **(rickshaws  and walking)**  were  exposed  to  the  highest  PM2.5 concentrations.  Inside enclosed modes of transports which used AC, including **private cars** and the **metro**, were found to have signicantly lower PM2.5 concentrations. The exposure levels  for passengers on  **buses**  and travellers in  **non-AC cars** were found to lie between fully closed and open transport modes. Nevertheless,  open  windows  and the  frequency of opening  doors  on buses resulted  in ambient pollution  (background plus  that emitted by other vehicles) entering vehicles, thus increasing the concentrations to which travellers were exposed');

image = Image.open('img3.jpg')
st.image(image, caption='Delhi transport')

image = Image.open('img2.jpg')
st.image(image, caption='Coldest Since 1951')



