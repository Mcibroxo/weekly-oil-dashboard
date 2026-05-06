# Windows PowerShell script to automate pushing the local repository to GitHub
Clear-Host
Write-Host "==========================================================" -ForegroundColor Yellow
Write-Host " 🛢️  AUTOMATIC GITHUB PUSH: WEEKLY PETROLEUM STATUS REPORT" -ForegroundColor Yellow
Write-Host "==========================================================" -ForegroundColor Yellow
Write-Host ""

# 1. Ask for the GitHub Repo URL
$repoUrl = Read-Host "👉 Paste your new GitHub Repository URL (e.g., https://github.com/username/repo-name.git)"
$repoUrl = $repoUrl.Trim()

if ([string]::IsNullOrEmpty($repoUrl)) {
    Write-Host "❌ Error: Repository URL cannot be empty." -ForegroundColor Red
    Exit
}

# 2. Check if git is initialized
if (-not (Test-Path ".git")) {
    Write-Host "🔧 Initializing git repository..." -ForegroundColor Cyan
    git init -b main
    git config user.name "Oil Analytics Dashboard"
    git config user.email "oil-analytics@example.com"
}

# 3. Commit files
Write-Host "📦 Preparing files for upload..." -ForegroundColor Cyan
git add .
git commit -m "Initial commit: Premium Oil Status Dashboard and Automated Data Pipeline" 2>$null

# 4. Link the remote and push
Write-Host "🔗 Linking remote..." -ForegroundColor Cyan
git remote remove origin 2>$null
git remote add origin $repoUrl

Write-Host "🚀 Pushing to GitHub..." -ForegroundColor Cyan
git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "🎉 SUCCESS! Your premium dashboard is now live on your GitHub!" -ForegroundColor Green
    Write-Host "Go to your browser to view your files and the gorgeous README.md!" -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "❌ Push failed. Please verify that:" -ForegroundColor Red
    Write-Host "   1. You created the repository on github.com" -ForegroundColor Red
    Write-Host "   2. You have write/push access to this repository" -ForegroundColor Red
    Write-Host "   3. Your git credentials are authenticated in this terminal" -ForegroundColor Red
}

Write-Host ""
Read-Host "Press Enter to close this window..."
