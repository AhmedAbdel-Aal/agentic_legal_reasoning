from senior import SeniorAgent
from junior import JuniorAgent
from utils import get_last_question, check_for_final_answer
from message import Message


def conversate_scenario_two(s_agent, j_agent, senior_system_prompt, senior_base_prompt, junior_system_prompt, junior_base_prompt):

    s_agent.add_system_message(Message('system', senior_system_prompt))
    s_agent_base_prompt = Message('user', senior_base_prompt)

    s_agent.add_system_message(Message('system', junior_system_prompt))
    j_agent_base_prompt = Message('user', junior_base_prompt)


    round_one = True
    conversation = []
    while True:
        if round_one:
            answer = s_agent.reply_to(s_agent_base_prompt)
            conversation.append(f"Senior Agent -> {answer}")
            print(f"Senior Agent -> {answer}") 

            response = j_agent.reply_to(j_agent_base_prompt)
            question = get_last_question(response.content)
            conversation.append(f"Junior Agent -> {question}")
            print(f"Junior Agent -> {question}")
            round_one = False

        answer = s_agent.reply_to(Message('user', question))
        response = j_agent.reply_to(answer)
        question = get_last_question(response.content)
        final_answer = check_for_final_answer(response.content)
        
        print(f"Senior Agent -> {answer}")  
        conversation.append(f"Senior Agent -> {answer}")
        print('-'*30)  
        print(f"Jenior Agent -> {question}")
        conversation.append(f"Junior Agent -> {question}")

        if final_answer is not None:
            print(response)
            break
    return conversation