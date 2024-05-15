import streamlit as st
st.title("Which Job Opportunities?")
st.write('I was interested to know what job opportunities are offered on "Jadarat" and which experiences have the highest chances in the market.')
st.write('**Jadarat** is the Unified Employment Platform (UEP). It is a national platform empowering the workforce of Saudi Arabia. Jobseekers can use the UEP to explore and apply for both public and private sector jobs in the Saudi labor market.')

st.write('There are 56.6% of positions on the website that are offered to **fresh graduates** based on the total number of available jobs on the website. **Since the majority of the jobs are for fresh graduate, I chose to analyze the market based on them.**')
file_path = 'chart1 -streamlit1.png'
st.image(file_path, caption='Possition opp', use_column_width=True)
