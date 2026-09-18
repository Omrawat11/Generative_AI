import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()

st.set_page_config(page_title="Chat World", page_icon="💬")
st.title("----Welcome to the chat world----")

model = ChatGroq(model="openai/gpt-oss-20b")

# Mode selection (only before chat starts)
if "mode_selected" not in st.session_state:
    st.session_state.mode_selected = False

if not st.session_state.mode_selected:
    st.subheader("Select model types:-")
    choice = st.radio(
        "Tell your response:-",
        options=[1, 2, 3],
        format_func=lambda x: {
            1: "Press 1 for Angry mode",
            2: "Press 2 for Sad mode",
            3: "Press 3 for funny mode"
        }[x]
    )

    if st.button("Start Chat"):
        if choice == 1:
            mode = "You are an Angry AI agent. you respond in angry way"
        elif choice == 2:
            mode = "You are an Sad AI agent. you respond in sad way"
        elif choice == 3:
            mode = "You are an Funny AI agent. you respond in funny way"

        st.session_state.messages = [SystemMessage(content=mode)]
        st.session_state.mode_selected = True
        st.rerun()

else:
    st.write("------Press 0 to exit------")

    # Display chat history (skip SystemMessage)
    for msg in st.session_state.messages:
        if isinstance(msg, HumanMessage):
            with st.chat_message("user"):
                st.write(msg.content)
        elif isinstance(msg, AIMessage):
            with st.chat_message("assistant"):
                st.write(msg.content)

    prompt = st.chat_input("You:-")

    if prompt is not None:
        st.session_state.messages.append(HumanMessage(content=prompt))

        if prompt == "0":
            with st.chat_message("user"):
                st.write(prompt)
            st.write(st.session_state.messages)
            st.stop()

        with st.chat_message("user"):
            st.write(prompt)

        response = model.invoke(st.session_state.messages)
        st.session_state.messages.append(AIMessage(content=response.content))

        with st.chat_message("assistant"):
            st.write(response.content)