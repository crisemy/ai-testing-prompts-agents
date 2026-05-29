# Risk Model Card

## Model Identity
- **Model name:** Groq Llama 3.3 (70B) / Llama 3.1 (8B Instant)
- **Model type:** Causal LLM (chat)
- **Provider:** Groq (LPU inference)
- **Version:** llama-3.3-70b-versatile (promptfoo), llama-3.1-8b-instant (agent)

## Intended Use
- Customer support assistant for an electronics/tech store
- Responds to device troubleshooting and refund/policy queries
- Must stay under 100 words, use "unplug" for restart steps, never offer refunds

## Risk Assessment

### Known Failure Modes
| Failure Mode | Severity | Likelihood | Detection |
|-------------|----------|------------|-----------|
| Refund policy violation (offers money back) | Critical | Medium | promptfoo refund tests |
| Hallucinated troubleshooting steps | High | Low | DeepEval relevancy metric |
| Excessive verbosity (>100 words) | Medium | High | Custom Python evaluator |
| Safety bypass (jailbreak) | Critical | Low | promptfoo injection tests |
| Off-policy response in non-English | High | Medium | Multi-lang tests (planned) |

### Risk Mitigations
- **Guardrail:** Hard-coded redirect to return policy
- **Evaluator:** tech_eval.py checks conciseness + "unplug"
- **Evaluator:** polite_eval.js checks refusal vocabulary
- **Metric:** AnswerRelevancyMetric threshold ≥ 0.5
- **Red-teaming:** jailbreak/injection test suite (planned Phase 1.5)

## Evaluation Protocol
- **Frequency:** On every PR and push to main
- **Environment:** CI (GitHub Actions) + optional local Docker
- **Grading model:** Same Llama 3.3 70B (self-grading via llm-rubric)
