# Project Bootstrap

## Project Info
- **Project name:** AI Testing Prompts & Agents
- **Domain:** AI Systems Testing & Evaluation (LLM Customer Support)
- **Repository:** ai-testing-prompts-agents
- **Primary stakeholders:** QA Engineering, AI Engineering, Product

## Quality Goals
- **Leakage target:** < 10% hallucination rate
- **Flakiness target:** < 5% test flakiness
- **Regression time target:** < 5 min full suite
- **CFR target:** < 5% change failure rate

## In-Scope Quality Areas
- **APIs:** Groq LLM API (promptfoo + DeepEval)
- **Critical UI flows:** Prompt evaluation pipeline, Agent response pipeline
- **Data validations:** Eval input/output schemas, scoring thresholds
- **Integrations:** promptfoo ↔ custom evaluators, DeepEval ↔ LangChain agent

## Test Strategy Snapshot
- **Risk model used:** ChangeWeight × SafetyRelevance × HistoricalMultiplier
- **Prioritization mode:** Risk-based (high-risk tests run first)
- **CI execution mode:** On push to main + PRs
- **Release gate criteria:** All blocking evals pass ≥ 90%

## Required Inputs
- **Test inventory source:** `promptfooconfig.yaml` + `test_agent.py`
- **Defect history source:** Eval output logs (JSON/CSV)
- **Change metadata source:** Git commit history
- **Environment profile:** Local dev, Docker, CI (GitHub Actions)

## Deliverables
- [ ] Updated risk map (see risk_model_card.md)
- [ ] Prioritized regression subset
- [ ] Failure analysis summary
- [ ] Release quality report
