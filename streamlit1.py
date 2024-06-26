import streamlit as st
st.title("Which the highest  job opportunities on Jadarat?")
st.write('I was interested to know what job opportunities are offered on **Jadarat** and which experiences have the highest chances in the market.')
st.write('**Jadarat** is the Unified Employment Platform (UEP). It is a national platform empowering the workforce of Saudi Arabia. Jobseekers can use the UEP to explore and apply for both public and private sector jobs in the Saudi labor market.')

st.write('There are 56.6% of positions on the website that are offered to **fresh graduates** based on the total number of available jobs on the website. **Since the majority of the jobs are for fresh graduate, I chose to analyze the market based on them.**')
file_path = 'chart1 -streamlit1.png'
st.image(file_path, caption='', use_column_width=True)

st.write('')

st.write('The chart below shows the expected salary for fresh graduates, most companies offer them 4,000.')
st.write('    - The range of salary between 3,000 to 12,000.')
file_path = 'chart2 -streamlit1.png'
st.image(file_path, caption='', use_column_width=True)

st.write('') 

st.write('A **private company** is more likely to hire a fresh graduates, compared with a semigovernmental one.')
file_path = 'chart3 -streamlit1.png'
st.image(file_path, caption='', use_column_width=True)

st.write('') 

st.write('Also the **small company** hire a fresh graduates.')
file_path = 'chart4 -streamlit1.png'
st.image(file_path, caption='', use_column_width=True)

st.write('') 
st.write('') 
st.write('') 

st.write('In my analysis, I examined the key factors that help you understand the job market for recent graduates. These factors include **expected salary, company type and size.**')
st.write('**Good Luck!**')
