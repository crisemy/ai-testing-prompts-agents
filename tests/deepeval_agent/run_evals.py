import json
import csv
from inspect import formatannotation
import os
from agent import SimpleAgent
from deepeval import evaluate
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric
from test_agent import eval_model # Import the custom Groq evaluator
from dotenv import load_dotenv

load_dotenv()

def run_evaluation_suite():
    print("Initializing dummy agent...")
    agent = SimpleAgent()
    
    # Test cases dataset
    queries = [
        "What is your refund policy?",
        "My laptop arrived broken, I want my money back!",
        "Do you offer store credit for returns?",
        "I demand a 100% refund on my purchase instantly."
    ]
    
    print("Generating responses and preparing test cases...")
    test_cases = []
    
    for query in queries:
        actual_output = agent.query(query)
        test_case = LLMTestCase(
            input=query,
            actual_output=actual_output
        )
        test_cases.append(test_case)

    print("Running DeepEval metrics...")
    metric = AnswerRelevancyMetric(threshold=0.5, model=eval_model)
    
    # Export results manually to CSV for the dashboard
    csv_file = "eval_results.csv"
    with open(csv_file, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Input", "Actual Output", "Metric Name", "Score", "Threshold", "Success", "Reason"])
        
        for tc in test_cases:
            try:
                metric.measure(tc)
                success = metric.is_successful()
            except Exception as e:
                metric.score = 0
                success = False
                metric.reason = str(e)

            writer.writerow([
                tc.input,
                tc.actual_output,
                "Answer Relevancy",
                metric.score,
                metric.threshold,
                success,
                metric.reason
            ])
                
    print(f"Evaluation complete! Saved results to {csv_file}")

if __name__ == "__main__":
    run_evaluation_suite()
