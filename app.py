import streamlit as st
from chatbot import get_response

st.set_page_config(
    page_title="Rule-Based AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.sidebar.title("🤖 RuleBot")
st.sidebar.success("🟢 Online")
st.sidebar.write("AI Internship Project")
st.sidebar.markdown("---")
st.sidebar.write("Type **help** to see all commands.")

if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.messages = []

st.title("🤖 Rule-Based AI Chatbot")
st.caption("DecodeLabs AI Internship Project")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Type your message...")

if prompt:

    st.session_state.messages.append(
        {"role":"user","content":prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    response = get_response(prompt)

    st.session_state.messages.append(
        {"role":"assistant","content":response}
    )

    with st.chat_message("assistant"):
        st.markdown(response)