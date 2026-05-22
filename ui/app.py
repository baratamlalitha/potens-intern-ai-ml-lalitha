import streamlit as st
import requests

st.set_page_config(
    page_title="AI Policy Assistant",
    page_icon="📚",
    layout="centered"
)

st.title("📚 Multilingual AI Policy Assistant")

st.caption(
    "Semantic policy retrieval with multilingual support and contradiction analysis."
)

st.divider()

query = st.text_input(
    "Ask a question from the policy documents:"
)

if st.button("Ask"):

    with st.spinner("Generating answer..."):

        response = requests.post(
            "http://127.0.0.1:8000/ask",
            json={
                "query": query
            }
        )

        data = response.json()

        st.subheader("Answer")

        st.write(data["answer"])

        st.divider()

        st.subheader("Citations")

        shown = set()

        for citation in data["citations"]:

            key = (
                citation["source"],
                citation["page"]
            )

            if key not in shown:

                st.write(
                    f"📄 {citation['source']} - Page {citation['page']}"
                )

                shown.add(key)