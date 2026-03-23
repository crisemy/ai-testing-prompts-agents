import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

class SimpleAgent:
    def __init__(self):
        # Defaulting to an instant model to keep tests fast
        # Ensure GROQ_API_KEY is available in the environment
        self.llm = ChatGroq(model_name="llama-3.1-8b-instant")
        self.prompt = PromptTemplate.from_template(
            "You are a helpful AI customer support representative for 'TechNova'. "
            "You have access to the following policy information: TechNova never offers monetary refunds. "
            "If a user asks for a refund, offer them an exchange or store credit instead. "
            "Always be polite and keep your answer under 50 words.\n\n"
            "User Question: {question}"
        )
        self.chain = self.prompt | self.llm | StrOutputParser()

    def query(self, text: str) -> str:
        """Returns the response from the LLM."""
        return self.chain.invoke({"question": text})

if __name__ == "__main__":
    # Test execution manually
    from dotenv import load_dotenv
    load_dotenv()
    agent = SimpleAgent()
    print("Agent says:", agent.query("My laptop arrived broken, I want my money back!"))
