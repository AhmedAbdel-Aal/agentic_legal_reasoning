import streamlit as st
import time
from senior import SeniorAgent
from junior import JuniorAgent
from message import Message
from utils import get_last_question, check_for_final_answer
from prompts_one import facts, conclusion
import os

# Set your secret as an environment variable


# Define the two scenarios for the conversation
def conversate_scenario_one(s_agent, j_agent, senior_system_prompt, senior_base_prompt, junior_system_prompt, junior_base_prompt):
    s_agent.add_system_message(Message('system', senior_system_prompt))
    s_agent_base_prompt = Message('user', senior_base_prompt)
    s_agent.add_system_message(Message('system', junior_system_prompt))
    j_agent_base_prompt = Message('user', junior_base_prompt)
    
    round_one = True
    while True:
        if round_one:
            answer = j_agent.reply_to(j_agent_base_prompt)
            yield f"Junior Agent -> {answer}"
            
            response = s_agent.reply_to(s_agent_base_prompt)
            question = get_last_question(response.content)
            yield f"Senior Agent -> {question}"
            
            round_one = False
        
        answer = j_agent.reply_to(Message('user', question))
        yield f"Junior Agent -> {answer}"
        
        response = s_agent.reply_to(answer)
        question = get_last_question(response.content)
        yield f"Senior Agent -> {question}"
        
        final_answer = check_for_final_answer(response.content)
        if final_answer is not None:
            yield final_answer
            break

def conversate_scenario_two(s_agent, j_agent, senior_system_prompt, senior_base_prompt, junior_system_prompt, junior_base_prompt):
    s_agent.add_system_message(Message('system', senior_system_prompt))
    s_agent_base_prompt = Message('user', senior_base_prompt)
    s_agent.add_system_message(Message('system', junior_system_prompt))
    j_agent_base_prompt = Message('user', junior_base_prompt)
    
    round_one = True
    while True:
        if round_one:
            answer = s_agent.reply_to(s_agent_base_prompt)
            yield f"Senior Agent -> {answer}"
            
            response = j_agent.reply_to(j_agent_base_prompt)
            question = get_last_question(response.content)
            yield f"Junior Agent -> {question}"
            
            round_one = False
        
        answer = s_agent.reply_to(Message('user', question))
        yield f"Senior Agent -> {answer}"
        
        response = j_agent.reply_to(answer)
        question = get_last_question(response.content)
        yield f"Junior Agent -> {question}"
        
        final_answer = check_for_final_answer(response.content)
        if final_answer is not None:
            yield final_answer
            break

# Streamlit UI setup
st.title("LLM Chat Interface")

# Input fields
facts = st.text_area("Facts", facts)
conclusion = st.text_area("Conclusion", conclusion)
junior_base_prompt = st.text_area("Junior Lawyer Base Prompt")
junior_system_prompt = st.text_area("Junior Lawyer System Prompt", "You are expert legal lawyer with European Court of Human Rights (ECHR).")
senior_base_prompt = st.text_area("Senior Lawyer Base Prompt")
senior_system_prompt = st.text_area("Senior Lawyer System Prompt", "You are expert legal lawyer with European Court of Human Rights (ECHR).")
scenario_choice = st.radio("Choose Scenario", ["scenario_one", "scenario_two"])
backend_model = st.radio("Choose Model", ["openai,gpt-4o", "groq,llama-3.1-70b-versatile"])


if "{facts}" in junior_base_prompt:
    junior_base_prompt = junior_base_prompt.replace("{facts}", facts)

if "{facts}" in senior_base_prompt:
    senior_base_prompt = senior_base_prompt.replace("{facts}", facts)

if "{conclusion}" in junior_base_prompt:
    junior_base_prompt = junior_base_prompt.replace("{conclusion}", conclusion)

if "{conclusion}" in senior_base_prompt:
    senior_base_prompt = senior_base_prompt.replace("{conclusion}", conclusion)


# CSS styling for message boxes
st.markdown(
    """
    <style>
    .message-box {
        padding: 10px;
        margin: 10px 0;
        border-radius: 5px;
        border: 1px solid #ccc;
        background-color: #e0f7fa;  /* Light blue background */
        color: #000;  /* Black text color */
        white-space: pre-wrap;  /* Allows line wrapping */
    }
    .junior-agent {
        border-left: 5px solid #4CAF50;
    }
    .senior-agent {
        border-left: 5px solid #2196F3;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Button to start conversation
if st.button("Start Conversation"):
    backend, model = backend_model.split(",")
    print(backend, model)
    s_agent = SeniorAgent(model_name=model, backend=backend)
    j_agent = JuniorAgent(model_name=model, backend=backend)

    # Choose scenario
    if scenario_choice == "scenario_one":
        conversation_generator = conversate_scenario_one(
            s_agent, j_agent, senior_system_prompt, senior_base_prompt, junior_system_prompt, junior_base_prompt
        )
    else:
        conversation_generator = conversate_scenario_two(
            s_agent, j_agent, senior_system_prompt, senior_base_prompt, junior_system_prompt, junior_base_prompt
        )

    # Display conversation messages one by one with styling
    conversation_log = []  # List to hold each conversation message

    for message in conversation_generator:
        # Check if the message is from Junior or Senior agent
        if message.startswith("Junior Agent"):
            st.markdown(f'<div class="message-box junior-agent">{message}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="message-box senior-agent">{message}</div>', unsafe_allow_html=True)
        
        time.sleep(1)  # simulate delay for real-time effect