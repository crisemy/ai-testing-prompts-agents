.PHONY: setup eval-promptfoo eval-deepeval dashboard docker-run docker-dashboard clean

# --- Bootstrap ---
setup:
	cp -n .env.example .env || true
	cd tests/promptfoo && npm install
	cd tests/deepeval_agent && pip install -r requirements.txt

# --- Run Evaluations ---
eval-promptfoo:
	cd tests/promptfoo && npx promptfoo eval

eval-deepeval:
	cd tests/deepeval_agent && python run_evals.py

# --- Dashboard ---
dashboard:
	cd tests/deepeval_agent && streamlit run dashboard.py

# --- Docker ---
docker-run:
	docker compose --profile eval up --build

docker-dashboard:
	docker compose --profile dashboard up --build

# --- Cleanup ---
clean:
	rm -rf tests/promptfoo/node_modules
	rm -rf tests/deepeval_agent/venv
	rm -rf tests/deepeval_agent/__pycache__
	rm -rf tests/deepeval_agent/.pytest_cache
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
