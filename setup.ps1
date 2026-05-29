param(
    [string]$EnvFile = ".env"
)

Write-Host "=== AI Testing Framework Setup ===" -ForegroundColor Cyan

# --- Root .env ---
if (-not (Test-Path $EnvFile)) {
    Copy-Item ".env.example" -Destination $EnvFile
    Write-Host "[!] Created $EnvFile from .env.example — edit it with your GROQ_API_KEY" -ForegroundColor Yellow
} else {
    Write-Host "[OK] $EnvFile already exists" -ForegroundColor Green
}

# --- Promptfoo (npm) ---
Write-Host "`n--- Promptfoo Setup ---" -ForegroundColor Cyan
Push-Location "tests/promptfoo"
if (-not (Test-Path "node_modules")) {
    npm install
    Write-Host "[OK] npm install completed" -ForegroundColor Green
} else {
    Write-Host "[OK] node_modules already installed" -ForegroundColor Green
}
Pop-Location

# --- DeepEval Agent (pip) ---
Write-Host "`n--- DeepEval Agent Setup ---" -ForegroundColor Cyan
Push-Location "tests/deepeval_agent"
if (-not (Test-Path "venv")) {
    python -m venv venv
    Write-Host "[OK] Virtual environment created" -ForegroundColor Green
}
# Activate and install
$venvActivate = if ($IsWindows -or $env:OS -match "Windows") { "venv\Scripts\Activate.ps1" } else { "venv/bin/Activate.ps1" }
if (Test-Path $venvActivate) {
    & $venvActivate
    pip install -r requirements.txt
    Write-Host "[OK] pip install completed" -ForegroundColor Green
}
Pop-Location

Write-Host "`n=== Setup complete! ===" -ForegroundColor Cyan
Write-Host "Next steps:" -ForegroundColor White
Write-Host "  1. Add your GROQ_API_KEY to $EnvFile" -ForegroundColor Gray
Write-Host "  2. Run: npx promptfoo eval  (in tests/promptfoo)" -ForegroundColor Gray
Write-Host "  3. Run: pytest test_agent.py -v  (in tests/deepeval_agent)" -ForegroundColor Gray
