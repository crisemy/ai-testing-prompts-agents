# AI Testing Prompts & Agents

Evaluation framework for LLM-powered customer support agents using **promptfoo** and **DeepEval**.

## Branches

All branches are currently synchronized at the same commit.

| Branch          | Purpose                                                |
|---------------- |--------------------------------------------------------|
| `main`          | Default branch. Clean, production-ready state.         |
| `promptfoo`     | Feature branch for promptfoo-based evaluation configs. |
| `deepeval_agent`| Feature branch for DeepEval + LangChain agent eval.    |

## Project Structure

```bash
tests/
├── promptfoo/              # Prompt-level evaluation (promptfoo)
│   ├── promptfooconfig.yaml   # Eval configuration: prompts, providers, tests
│   ├── evaluators/
│   │   ├── tech_eval.py       # Python assert: checks conciseness + "unplug"
│   │   └── polite_eval.js     # JS assert: checks empathetic/policy vocabulary
│   ├── package.json
│   └── output.json / output.txt
│
└── deepeval_agent/         # Agent-level evaluation (DeepEval)
    ├── agent.py               # LangChain agent (Groq + custom prompt template)
    ├── test_agent.py          # Pytest suite with DeepEval metrics
    ├── run_evals.py           # Bulk evaluation runner → CSV export
    ├── dashboard.py           # Streamlit dashboard for results visualization
    ├── requirements.txt
    ├── analysis.ipynb
    └── eval_results.csv
```

## How to Run

### Quick Setup (Root)

```powershell
# One-shot bootstrap (copies .env.example → .env, installs deps)
./setup.ps1
```

Or step by step:

### Promptfoo (tests/promptfoo/)

```powershell
cd tests/promptfoo
npm install
$env:GROQ_API_KEY="your_key"
npx promptfoo eval
```

Model: `groq:llama-3.3-70b-versatile` (generation + grading).

### DeepEval Agent (tests/deepeval_agent/)

```powershell
cd tests/deepeval_agent
pip install -r requirements.txt
$env:GROQ_API_KEY="your_key"
pytest test_agent.py -v      # Run test suite
python run_evals.py           # Bulk eval → eval_results.csv
streamlit run dashboard.py    # Visual dashboard
```

### Docker (Reproducible runs)

```powershell
# Run both eval suites in isolated containers
docker compose --profile eval up --build

# Launch dashboard
docker compose --profile dashboard up --build
```

### Makefile (Cross-platform task runner)

```powershell
make setup              # Bootstrap everything
make eval-promptfoo     # Run promptfoo suite
make eval-deepeval      # Run DeepEval suite
make dashboard          # Launch Streamlit dashboard
make docker-run         # Run evals via Docker
make docker-dashboard   # Dashboard via Docker
```

## Evaluation Tests

### Promptfoo Tests

| Test            | Input                                               | Assertions                                                                                         |
|---------------- |-----------------------------------------------------|----------------------------------------------------------------------------------------------------|
| Router restart  | "How do I restart my TP-Link router?"               | Must mention "unplug" + conciseness < 100 words                                                    |
| Refund demand   | "My TV arrived broken, I want my money right now."  | No refund mention, must redirect to return policy or offer must use polite/policy vocabulary       |

Two prompt variants are compared:

* **Polite assistant** — friendly, concise, strict refund redirect
* **Tech expert** — technical, direct, strict refund redirect

### DeepEval Tests

| Test                          | Input                                                                                         Metric                                                  |
|------------------------------|-----------------------------------------------------------------------------------------------|---------------------------------------------------------|
| Answer relevancy (positive)  | "What is your refund policy?"                                                                 | AnswerRelevancyMetric (threshold ≥ 0.5)                 |
| Answer relevancy (negative)  | "I hate this store, everything I buy is broken and I demand a full refund!"                  | AnswerRelevancyMetric (threshold ≥ 0.5)                 |

## Prompt Design Patterns

1. **Under 100 words** — enforced via Python evaluator (tech_eval.py)
2. **"Unplug" instruction** — both prompts explicitly template the restart steps
3. **Refund redirect** — both prompts instruct to refer to return policy, never mention refunds
4. **Grading consistency** — same model (Llama 3.3 70B) used for both generation and evaluation

## Key Dependencies

* **promptfoo** — prompt testing framework (npm)
* **deepeval** — LLM evaluation metrics (Python)
* **langchain-groq** — LangChain integration with Groq API
* **streamlit + plotly** — evaluation dashboard
* **Groq API** — inference via LPU hardware (llama-3.3-70b-versatile)
