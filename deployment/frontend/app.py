import streamlit as st
import requests as req

backend_server_location = "http://127.0.0.1:8000"

n = st.text_input("Name")
e = st.text_input("email")
p = st.text_input("password", type="password")
register_btn = st.button("register")

if register_btn:
    payload={
        "name":n,
        "email":e,
        "password":p
    }

    res = req.post(f"{backend_server_location}/register",json = payload)

    if res.status_code == 200:
        st.write(res.json())