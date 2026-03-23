# LLM Prompt & Agent Testing Framework 🧪🤖

Welcome to the **AI Testing Framework**, a comprehensive Quality Assurance (QA) pipeline designed to evaluate and regression-test Large Language Models (LLMs), prompts, and autonomous AI agents.

This project serves as a Proof-of-Concept for **AI Systems Testing & Evaluation**, ensuring that generative AI applications are reliable, accurate, and aligned with business guardrails before reaching production.

## 🚀 Key Features

This repository is divided into dedicated testing modules:

### 1. Prompt Regression Testing (`tests/promptfoo/`)
Utilizes **Promptfoo** to mathematically evaluate if LLM responses regress when system prompts change.
*   **Prompt Matrices:** Evaluates multiple prompts against a dataset of user queries simultaneously.
*   **Custom Evaluators:** Implements `Javascript` and `Python` custom heuristic scripts to enforce business rules (e.g., tone of voice, brevity).
*   **Guardrail Assertions:** Hard evaluation of boundaries to prevent the AI from offering unauthorized solutions (like immediate refunds).

### 2. Autonomous Agent Evaluation (`tests/deepeval_agent/`)
Utilizes **DeepEval** and **PyTest** to evaluate dynamic agent logic.
*   **LangChain Integration:** A fully functional mock technical support agent implemented in LangChain.
*   **Cost-Free Custom Metrics:** Wrapped DeepEval's base metrics in a custom **Llama 3** (Groq) evaluator so evaluations do not depend on costly OpenAI API keys.
*   **RAG / Answer Relevancy Validation:** Mathematically asserts if the agent actually answers the user's intent.

### 3. Local Dashboard Analytics
Say goodbye to expensive Enterprise cloud subscriptions! The framework incorporates a fully offline data pipeline.
*   Test suites programmatically dump their output to `eval_results.csv`.
*   Includes a **Jupyter Notebook** (`analysis.ipynb`) for deep-dive exploratory data analysis.
*   A sleek, interactive **Streamlit Dashboard** (`dashboard.py`) using **Plotly** to visualize pass/fail rates, latency, and detailed failure reasons visually.

## ⚙️ Getting Started

### Prerequisites
*   Node.js (`npm` or `npx`)
*   Python 3.12+
*   A Groq API Key (or OpenAI key explicitly configured).

### Running Promptfoo
```bash
cd tests/promptfoo
npm install
npx promptfoo eval
```

### Running the App Dashboard & Agent Evaluator
```bash
cd tests/deepeval_agent
python -m venv venv
source venv/Scripts/activate # Windows Git Bash
pip install -r requirements.txt

# Run the tests to generate analytics data
python run_evals.py

# Launch the Dashboard
streamlit run dashboard.py
```

## 📜 Business Value
This pipeline acts as the ultimate **continuous integration checkpoint** for AI teams. By tracking empirical metric scores across updates, companies can confidently iterate upon their LLMs without the fear of silent performance degradation or unexpected hallucinations.
