import os
import json
import re

def load_json(path):
    with open(path, 'r') as f:
        data = json.load(f)
    return data

def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

def load_txt(path):
    with open(path, 'r') as f:
        data = f.read()
    return data


def get_last_question(text):
    # Regex pattern to match questions, considering multiline questions
    pattern = r'(Question:\s*.*?)(?=\n[A-Z]|\Z)'

    # Find all matches with the multiline flag enabled
    matches = re.findall(pattern, text, re.DOTALL)
    
    # Get the last match
    last_question = matches[-1] if matches else None

    return last_question


def check_for_stop(text):
    # Regex pattern to match questions, considering multiline questions
    pattern = r'(Stop:\s*.*?)(?=\n[A-Z]|\Z)'

    # Find all matches with the multiline flag enabled
    matches = re.findall(pattern, text, re.DOTALL)
    
    # Get the last match
    stop = matches[-1] if matches else None

    return stop

def check_for_final_answer(text):
    # Regex pattern to match questions, considering multiline questions
    pattern = r'(Final Answer:\s*.*?)(?=\n[A-Z]|\Z)'

    # Find all matches with the multiline flag enabled
    matches = re.findall(pattern, text, re.DOTALL)
    
    # Get the last match
    stop = matches[-1] if matches else None

    return stop

def save_txt_file(file_name, content):
    with open(file_name, 'w') as f:
        f.write(content)