import smtplib as smtp
import streamlit as st

st.write(dict(st.secrets))

sender = smtp.SMTP("smtp.gmail.com", 587)
sender.ehlo()
sender.starttls()
sender.login(st.secrets["email"]["address"], st.secrets["email"]["apppassword"])

b = st.button("Click Me")
if b:
  sender.sendmail("python.user.143@gmail.com", "boycalledutkarsh@gmail.com", "HELLO \n\n Please check if u have recieved this")
