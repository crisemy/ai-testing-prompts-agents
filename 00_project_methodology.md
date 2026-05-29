# Project Methodology

CORE entry point. Use this guide to determine which artifacts, rules, workflows, and contracts to apply based on your project type and phase.

---

## 1. What type of project do I have?

Identify your project type. This determines priority skills, templates, and contracts.

### QA Automation

- Functional, API, and E2E test automation
- CI/CD integration, execution reporting
- **Key skills:** test_data_management, performance_testing, qa_observability
- **Templates:** project_bootstrap, release_quality_report
- **Rules:** _core/03_personal_tooling/rules/qa_rules.md, execution_rules.md, tooling_rules.md

### QA Architecture

- Framework design, tooling selection, quality strategy
- Coverage models, risk-based testing frameworks
- **Key skills:** test_prioritization, change_impact_analysis, quality_economics
- **Templates:** risk_model_card, experiment_card

### DS & AI

- Classification, ranking, and prediction models for QA
- Feature engineering, ML pipelines, model evaluation
- **Key skills:** applied_ml, data_engineering, data_collection, failure_analysis
- **Templates:** risk_model_card, experiment_card

### AI Engineering

- LLM-based systems, agents, AI tooling
- Safety, latency, accuracy, and security evaluation
- **Key skills:** ai_system_design, observability_engineering, data_engineering
- **Templates:** project_bootstrap, risk_model_card, release_quality_report

---

## 2. Phase 0 — Inception

Goal: define scope, initial risks, and quality strategy.

### Steps

1. Create a `project_bootstrap.md` — define objectives, stakeholders, target metrics
2. Create a `risk_model_card.md` — identify initial project risks
3. Review `_core/03_personal_tooling/rules/ai_rules.md`, `_core/03_personal_tooling/rules/qa_rules.md`, `_core/01_fundamentals/data_contracts.md` (data_rules), `_core/03_personal_tooling/rules/execution_rules.md`, `_core/03_personal_tooling/rules/tooling_rules.md`, `_core/03_personal_tooling/rules/anti_patterns.md` — align principles from day one

### Skills to apply

- `_core/03_personal_tooling/skills/quality_economics.md` — optimize testing investment vs risk
- `_core/03_personal_tooling/skills/experimentation.md` — define hypotheses and experimental design

### Expected outputs

- Completed project bootstrap (`project_bootstrap.md`)
- Risk model card with identified risks (`risk_model_card.md`)
- Mindset aligned with CORE rules

---

## 3. Phase 1 — Strategy & Contracts

Goal: define data contracts and evaluation architecture.

### Steps

1. Review `_core/01_fundamentals/data_contracts.md` — determine which contracts apply to your project
   - `test_prioritization_contract` — if test prioritization is needed
   - `change_impact_contract` — if change impact analysis is needed
   - `failure_analysis_contract` — if failure classification is needed
2. Review `_core/01_fundamentals/kpi_governance.md` — define project KPIs (use examples as reference)
3. Review `_core/01_fundamentals/risk_prioritization_contracts.md` — classify changes and define thresholds

### Skills to apply

- `_core/03_personal_tooling/skills/test_prioritization.md` — design prioritization scheme
- `_core/03_personal_tooling/skills/change_impact_analysis.md` — map dependencies
- `_core/03_personal_tooling/skills/data_engineering.md` — implement data pipelines

### Expected outputs

- Data contracts defined and versioned
- KPIs selected with thresholds
- Risk prioritization scheme

---

## 4. Phase 2 — Execution Setup

Goal: configure test execution and continuous integration.

### Steps

1. Select workflow based on project type:
   - `_core/03_personal_tooling/workflows/ci_pipeline_workflow.md` — for continuous integration
   - `_core/03_personal_tooling/workflows/regression_workflow.md` — for regression strategies
   - `_core/03_personal_tooling/workflows/risk_based_testing.md` — for risk-based execution
2. Configure report templates:
   - `_core/03_personal_tooling/templates/release_quality_report.md` — for release reporting
   - `_core/03_personal_tooling/templates/experiment_card.md` — for controlled experiments

### Skills to apply

- `_core/03_personal_tooling/skills/performance_testing.md` — if performance requirements exist
- `_core/03_personal_tooling/skills/qa_observability.md` — if dashboards and monitoring are needed
- `_core/03_personal_tooling/skills/test_data_management.md` — if test data management is needed

### Expected outputs

- Workflow configured and integrated in CI
- Templates adapted to the project
- Test data managed

---

## 5. Phase 3 — Monitoring & Operations

Goal: monitor, operate, and respond to incidents in production.

### Steps

1. Review `_core/02_operations/human_override_protocol.md` — if automated decisions need human supervision
2. Review `_core/02_operations/rollback_procedure.md` — if deployments need rollback capability
3. Review `_core/02_operations/red_team_suite.md` — configure security testing for your system type (AI/LLM or Web APIs)

### Skills to apply

- `_core/03_personal_tooling/skills/observability_engineering.md` — monitoring and alerting
- `_core/03_personal_tooling/skills/failure_analysis.md` — production failure classification

### Expected outputs

- Override protocol defined (if applicable)
- Rollback procedure documented
- Security suite configured (if applicable)

---

## 6. CORE Resource Map

| Situation | What to use |
| ----------- | ------------- |
| Starting a new project | `templates/project_bootstrap.md`, `_core/03_personal_tooling/rules/qa_rules.md`, `_core/03_personal_tooling/rules/execution_rules.md`, `_core/03_personal_tooling/rules/tooling_rules.md` |
| Defining KPIs | `_core/01_fundamentals/kpi_governance.md` |
| Defining data contracts | `_core/01_fundamentals/data_contracts.md` |
| Prioritizing tests by risk | `_core/01_fundamentals/risk_prioritization_contracts.md`, `_core/03_personal_tooling/workflows/risk_based_testing.md` |
| Analyzing change impact | `_core/03_personal_tooling/skills/change_impact_analysis.md` |
| Classifying test failures | `_core/03_personal_tooling/skills/failure_analysis.md` |
| Setting up CI pipeline | `_core/03_personal_tooling/workflows/ci_pipeline_workflow.md` |
| Designing regression strategy | `_core/03_personal_tooling/workflows/regression_workflow.md` |
| Reporting release quality | `_core/03_personal_tooling/templates/release_quality_report.md` |
| Documenting an experiment | `_core/03_personal_tooling/templates/experiment_card.md` |
| Modeling system risks | `_core/03_personal_tooling/templates/risk_model_card.md` |
| Designing human override | `_core/02_operations/human_override_protocol.md` |
| Preparing rollback | `_core/02_operations/rollback_procedure.md` |
| Security testing (any domain) | `_core/02_operations/red_team_suite.md` |
| Defining AI rules | `_core/03_personal_tooling/rules/ai_rules.md`, `_core/01_fundamentals/data_contracts.md` (data_rules), `_core/03_personal_tooling/rules/tooling_rules.md` |
| Defining team skills | `_core/03_personal_tooling/skills/` (choose by need) |
