# Agentic Legal Reasoning with LLMs


## Scenarios

The application supports two distinct scenarios, each with different interaction patterns between the junior and senior lawyer agents.

### Scenario 1: Senior Lawyer Inquires for Case Details

- **Senior Lawyer** does not have access to the case text.
- **Junior Lawyer** has access to the case text.
- The senior lawyer initiates the dialogue by asking questions about the case text.
- **Senior Lawyer** asks one question at a time.
- **Junior Lawyer** provides answers based solely on the case text, one question at a time.

To modify prompts for Scenario 1, edit `prompts_one.py`.

### Scenario 2: Junior Lawyer Inquires About the Law

- **Senior Lawyer** does not have access to the case text.
- **Junior Lawyer** has access to the case text.
- **Junior Lawyer** initiates the dialogue by asking questions about relevant laws.
- **Senior Lawyer** responds to each question by sharing knowledge about the law.
- The interaction follows a one-question-at-a-time pattern, initiated by the junior lawyer.

To modify prompts for Scenario 2, edit `prompts_two.py`.

## Models Used

This app supports the following models:
- `gpt-4o`
- `llama-3.1-70B`

## How to Use the Application

### Deployed App

The application is available at: [Agentic Legal Reasoning App](https://agenticlegalreasoning.streamlit.app/).

In the app interface:
- No additional setup or secrets are required.
- Facts and conclusions load dynamically based on your scenario choice.
- To include facts and conclusions in a prompt (e.g., for the junior lawyer), use `{facts}` in the respective prompt template.

### Using the Colab Notebook

Alternatively, Colab notebook: [Colab Notebook Link](https://colab.research.google.com/drive/1hQvGph_i5zjcd8ehM3eTchxid24sVLd1?usp=sharing).

**Note**: You will need to add secrets in the specified cell within the Colab notebook.