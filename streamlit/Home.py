import streamlit as st
import random
import time
import LogInput
import Summarizer
from io import StringIO
import asyncio

st.title("Simple chat")
st.write("This is a simple chat application to analyze logs.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


async def main():
    uploaded_file = st.file_uploader("Choose a file")
    input_lines = {""}
    input_str = ""
    if uploaded_file is not None:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        tmp_string = stringio.read()
        for line in iter(tmp_string.splitlines()):
            input_lines.add(" ".join(line.split(" ")[4:]))
        input_str = "\n".join(input_lines)
        # with open("input_str.txt", "w") as text_file:
        #     text_file.write("%s" % input_str)
        message_placeholder = st.empty()
        with st.spinner(text='In progress'):
            message_placeholder.markdown(await Summarizer.summarize_summaries(input_str))
            st.success('Done')

asyncio.run(main())

# # Accept user input
# if prompt := st.chat_input("What is up?"):
#     # Add user message to chat history
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     # Display user message in chat message container
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     # Display assistant response in chat message container
#     with st.chat_message("assistant"):
#         message_placeholder = st.empty()
#         full_response = ""
#         assistant_response = Summarizer.summarize(input_str)
#         print(assistant_response)
#         # Simulate stream of response with milliseconds delay
#         for chunk in assistant_response.split():
#             full_response += chunk + " "
#             time.sleep(0.05)
#             # Add a blinking cursor to simulate typing
#             message_placeholder.markdown(full_response + "▌")
#         message_placeholder.markdown(full_response)
#         print(st.session_state.messages)
#     # Add assistant response to chat history
#     st.session_state.messages.append(
#         {"role": "assistant", "content": full_response})
