import streamlit as st
import time
usr=''
ph=st.empty()
records={'alice':None,'bob':None}
  us=''
if st.button('Go to Sign in'): 
  with ph.container():
          st.title('Login')
          USERS = {
                  'alice': 'password123',
                  'bob': 'pass123',
                  'charlie': 'password'}
          st.write('Please log in')
          us=st.text_input('Username')
          pas=st.text_input('Password',type='password')
          if st.button('Log in'):
              if us in USERS and pas==USERS[us]:
                  ph.empty()
                  st.success('Logged in')
                  

                  
                  
              else:
                  st.error('Invalid credentials, try again.')

  
