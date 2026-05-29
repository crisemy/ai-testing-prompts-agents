# LLM Prompt & Agent Testing Framework

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.38%2B-FF4B4B)](https://streamlit.io/)
[![Groq](https://img.shields.io/badge/Groq-Llama%203.3-orange)](https://groq.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**AI Testing Framework**, is a comprehensive Quality Assurance (QA) pipeline designed to evaluate and regression-test Large Language Models (LLMs), prompts, and autonomous AI agents.

This project serves as a Proof-of-Concept for **AI Systems Testing & Evaluation**, ensuring that generative AI applications are reliable, accurate, and aligned with business guardrails before reaching production.

## Key Features

This repository is divided into dedicated testing modules:

### 1. Prompt Regression Testing (`tests/promptfoo/`)

Utilizes **Promptfoo** to mathematically evaluate if LLM responses regress when system prompts change.

* **Prompt Matrices:** Evaluates multiple prompts against a dataset of user queries simultaneously.
* **Custom Evaluators:** Implements `Javascript` and `Python` custom heuristic scripts to enforce business rules (e.g., tone of voice, brevity).
* **Guardrail Assertions:** Hard evaluation of boundaries to prevent the AI from offering unauthorized solutions (like immediate refunds).

### 2. Autonomous Agent Evaluation (`tests/deepeval_agent/`)

Utilizes **DeepEval** and **PyTest** to evaluate dynamic agent logic.

* **LangChain Integration:** A fully functional mock technical support agent implemented in LangChain.
* **Cost-Free Custom Metrics:** Wrapped DeepEval's base metrics in a custom **Llama 3** (Groq) evaluator so evaluations do not depend on costly OpenAI API keys.
* **RAG / Answer Relevancy Validation:** Mathematically asserts if the agent actually answers the user's intent.

### 3. Local Dashboard Analytics

Say goodbye to expensive Enterprise cloud subscriptions! The framework incorporates a fully offline data pipeline.

* Test suites programmatically dump their output to `eval_results.csv`.
* Includes a **Jupyter Notebook** (`analysis.ipynb`) for deep-dive exploratory data analysis.
* A sleek, interactive **Streamlit Dashboard** (`dashboard.py`) using **Plotly** to visualize pass/fail rates, latency, and detailed failure reasons visually.

## Getting Started

### Prerequisites

* Node.js (`npm` or `npx`)
* Python 3.12+
* A Groq API Key (or OpenAI key explicitly configured).

### Quick Setup (Root)

```bash
# One-shot bootstrap (copies .env.example → .env, installs deps)
./setup.ps1
```

### Running Promptfoo

```bash
cd tests/promptfoo
npm install
npx promptfoo eval
```

Runs all 22 test scenarios across both prompt variants (polite + tech expert). Results output to `output.json` / `output.txt`.

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

### Running Specific Test Scenarios

Filter by test name or category using promptfoo's `--filter` flag:

```bash
cd tests/promptfoo

# Run only refund guardrail tests
npx promptfoo eval --filter "refund"

# Run only device troubleshooting tests
npx promptfoo eval --filter "router|TV|charge|printer|Bluetooth|firmware"

# Run only jailbreak / injection tests
npx promptfoo eval --filter "jailbreak|extraction|role-play"

# Run only multi-language tests
npx promptfoo eval --filter "Spanish|French|German|Portuguese"

# Run only escalation tests
npx promptfoo eval --filter "threats|takeover|lawyer"

# Run a single test by description
npx promptfoo eval --filter "Smart TV"
```

### Promptfoo Test Overview

| Category | Count | Evaluators Used |
|---|---|---|
| Refund guardrails | 6 | `llm-rubric` + `polite_eval.js` |
| Device troubleshooting | 6 | `llm-rubric` + `tech_eval.py` |
| Escalation / hand-off | 3 | `llm-rubric` + `polite_eval.js` + `escalation_eval.py` |
| Multi-language | 4 | `llm-rubric` + `multilang_eval.py` (+ `polite_eval.js` for refund scenarios) |
| Jailbreak / injection | 3 | `llm-rubric` + `jailbreak_eval.py` + `jailbreak_eval.js` |
| **Total** | **22** | 2 prompts × 22 tests = 44 eval runs |

### Docker (Reproducible runs)

```bash
# Run both eval suites in isolated containers
docker compose --profile eval up --build

# Launch dashboard
docker compose --profile dashboard up --build
```

### Makefile (Cross-platform task runner)

```bash
make setup              # Bootstrap everything
make eval-promptfoo     # Run promptfoo suite
make eval-deepeval      # Run DeepEval suite
make dashboard          # Launch Streamlit dashboard
make docker-run         # Run evals via Docker
make docker-dashboard   # Dashboard via Docker
```

## Evaluation Results (Phase 1)

Current pass rate on Groq Llama 3.3-70B: **50.0%** (22/44 test runs)

| Category | Pass Rate | Notes |
|---|---|---|
| Refund guardrails | 91.7% | Strong — lost-in-transit needs nuanced handling |
| Device troubleshooting | 50.0% | Model over-applies "unplug" to battery devices |
| Escalation / hand-off | 66.7% | Fixed — threats and account takeover now escalate |
| Multi-language | 0% | Language mixing persists (model-level limitation) |
| Jailbreak / injection | 16.7% | System prompt leaking, DAN compliance (model-level) |

### Known Model-Level Limitations

1. **System prompt extraction** — reveals system prompt on "ignore instructions" attempts
2. **DAN-style jailbreak** — tech expert prompt complies with DAN persona
3. **Language mixing** — inserts English phrases ("Unplug the power source") into non-English responses
4. **Blind "unplug" advice** — applies power-cycling steps to battery-powered devices (phones, headphones)
5. **Lost-in-transit** — defaults to "refer to return policy" without investigation steps

These require stronger prompts, fine-tuning, or a model swap to resolve.

### Regression Testing (per _core methodology)

| Mode | When | Scope |
|---|---|---|
| **Fast** | Low-risk docs/meta changes | Refund guardrails only (12 runs) |
| **Standard** | PRs, feature branches | Full 22-test suite (44 runs) |
| **Critical** | Release candidates, main merge | Full eval + DeepEval suite |

Run the appropriate mode with `--filter-first-n <N>` or the full `npx promptfoo eval`.

## Business Value

This pipeline acts as the ultimate **continuous integration checkpoint** for AI teams. By tracking empirical metric scores across updates, companies can confidently iterate upon their LLMs without the fear of silent performance degradation or unexpected hallucinations.

## Author

Cristian N.

* QA Engineer with 20+ years of experience in software testing and automation.
* MSc Candidate in Data Science & Artificial Intelligence.

Research interests include:

* Experimental QA engineering
* QA Architecture
* Reliability testing
* AI-assisted quality assurance
* Data-driven software stability analysis
