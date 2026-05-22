import streamlit as st
import requests

st.set_page_config(
    page_title="AI Policy Assistant",
    layout="wide"
)

st.title("📚 AI Policy Assistant")

query = st.text_input(
    "Ask a question from the policy documents:"
)

if st.button("Ask"):

    response = requests.post(
        "http://127.0.0.1:8000/ask",
        json={
            "query": query
        }
    )

    data = response.json()

    st.subheader("Answer")

    st.write(data["answer"])

    st.subheader("Citations")

    for citation in data["citations"]:

        st.write(
            f"{citation['source']} - Page {citation['page']}"
        )