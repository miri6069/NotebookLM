
import streamlit as st
from agent import agent_executor
from langgraph.types import Command

st.title("🔍 NotebookLM Clone")
config = {"configurable": {"thread_id": "session_1"}}

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

if query := st.chat_input("מה תרצה לחקור היום?"):
    st.session_state.messages.append({"role": "user", "content": query})
    st.chat_message("user").markdown(query)
    
    response = agent_executor.invoke({"messages": [("user", query)]}, config=config)
    st.rerun()

snapshot = agent_executor.get_state(config)

if snapshot.next:
    if st.warning("הסוכן זיהה צורך לחפש באינטרנט, מחכה לאישורך"):
        if st.button("אשר והמשך"):
            agent_executor.invoke(Command(resume="continue"), config=config)
            st.rerun()
else:
    state = agent_executor.get_state(config)
    if state.values.get("messages"):
        last_msg = state.values["messages"][-1]
        if last_msg.type == "ai" and last_msg.content:
            st.chat_message("assistant").markdown(last_msg.content)
