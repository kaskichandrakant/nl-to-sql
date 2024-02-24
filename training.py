from transformers import AutoTokenizer, AutoModelForCausalLM

from connector import connect
from format import format_res
from schema import schema_prompt
import streamlit as st

conn = connect()
cur = conn.cursor()
tokenizer = AutoTokenizer.from_pretrained("nsql-350M")
model = AutoModelForCausalLM.from_pretrained("nsql-350M")


def start_app():
    st.title("Ask Anything About Your Database")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        query = schema_prompt + f"-- {prompt}"
        with st.chat_message("assistant"):
            with st.spinner("Thinking"):
                input_ids = tokenizer(query, return_tensors="pt").input_ids
                generated_ids = model.generate(input_ids, max_length=500)
                response = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
                try:
                    sql_query = format_res(response)
                    st.markdown(sql_query)
                    result = cur.execute(sql_query)
                    rows = cur.fetchall()[:50]
                    st.table(rows)
                except:
                    st.markdown("I am afraid i have generated something wrong")
                    connect()

        st.session_state.messages.append({"role": "assistant", "content": format_res(response)})
