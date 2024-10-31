
import os
from groq import Groq
from openai import OpenAI
from dotenv import load_dotenv
from message import Message

load_dotenv()


class SeniorAgent:
    def __init__(self, backend="groq", model_name="llama3-8b-8192", cache = None):
        self.model_name = model_name
        self.cache = cache
        self.backend = backend
        self.model_name = model_name
        self.conversation_history = []
        self.role = "user"

        if backend == "groq":
            self.groq_client = Groq(api_key=os.getenv("GROQ_API_TOKEN"))
        elif backend == "openai":
            self.openai_client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    def __str__(self) -> str:
        s = f"SummaryAgent(model_name={self.model_name})"
        for key, value in self.cache.items():
            s += f"\n{key}: {value}"
        return s

    def get_completion(self, prompt, system_message="You are a helpful assistant."):

        if self.backend == "groq":
            chat_completion = self.groq_client.chat.completions.create(
                model=self.model_name,#"llama3-70b-8192",
                temperature=0,
                messages=prompt,
            )
            return chat_completion.choices[0].message.content
        elif self.backend == "openai":
            completion = self.openai_client.chat.completions.create(
                        model="gpt-4o",
                        messages=prompt,
            )
            return completion.choices[0].message.content
        else:
            raise ValueError("Please provide a valid inference: 'ollama' or 'groq'")

    def add_system_message(self, message):
        self.conversation_history.append({"role": message.role, "content": message.content})
    
    def _generate(
        self, message: Message
    ):
        
        # Add user message to history
        self.conversation_history.append({
            "role": message.role,
            "content": message.content
        })
        # Get response from API
        response = self.get_completion(self.conversation_history)
        message = Message(self.role, response)
        
        # Add assistant response to history
        self.conversation_history.append({
            "role": self.role,
            "content": response
        })

        return message


    def reply_to(self, message: Message) -> Message:
        response = self._generate(message)

        return response
