import os
import pytest
from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric
from agent import SimpleAgent
from dotenv import load_dotenv

# Ensure environment variables are loaded
load_dotenv()

from deepeval.models.base_model import DeepEvalBaseLLM
from langchain_groq import ChatGroq

class GroqEvaluator(DeepEvalBaseLLM):
    def __init__(self):
        self.model = ChatGroq(model_name="llama-3.3-70b-versatile")

    def load_model(self):
        return self.model

    def generate(self, prompt: str) -> str:
        return self.model.invoke(prompt).content

    async def a_generate(self, prompt: str) -> str:
        res = await self.model.ainvoke(prompt)
        return res.content

    def get_model_name(self):
        return "Groq LLaMA-3.1 (8B Instant)"

eval_model = GroqEvaluator()
agent = SimpleAgent()

def test_agent_answer_relevancy():
    input_query = "What is your refund policy?"
    
    # Generate actual response using our Langchain agent
    actual_output = agent.query(input_query)
    
    # Define DeepEval metric(s) to evaluate the response
    # We use our custom Groq evaluator model to avoid OpenAI usage
    answer_relevancy_metric = AnswerRelevancyMetric(threshold=0.5, model=eval_model)

    test_case = LLMTestCase(
        input=input_query,
        actual_output=actual_output
    )

    # Asserts if the metric passes against the LLM output
    assert_test(test_case, [answer_relevancy_metric])

def test_agent_negative_sentiment():
    input_query = "I hate this store, everything I buy is broken and I demand a full refund!"
    
    actual_output = agent.query(input_query)
    
    answer_relevancy_metric = AnswerRelevancyMetric(threshold=0.5, model=eval_model)

    test_case = LLMTestCase(
        input=input_query,
        actual_output=actual_output
    )

    assert_test(test_case, [answer_relevancy_metric])
