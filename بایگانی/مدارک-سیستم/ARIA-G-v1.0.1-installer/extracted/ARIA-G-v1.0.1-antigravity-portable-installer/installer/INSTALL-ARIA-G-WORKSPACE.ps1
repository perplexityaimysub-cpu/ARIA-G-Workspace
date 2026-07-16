param (
    [Parameter(Mandatory=$true)]
    [string]$TargetWorkspace,
    
    [Parameter(Mandatory=$true)]
    [switch]$ConfirmInstall
)

# Enforce target path checks
if (-not (Test-Path $TargetWorkspace)) {
    Write-Error "Target Workspace does not exist: $TargetWorkspace"
    exit 1
}

# Create backup directory
$backupDir = Join-Path $TargetWorkspace ".agents\skills-backups\ARIA-G-pre-v1.0.1-$(Get-Date -Format 'yyyyMMdd-HHmmss')"
New-Item -ItemType Directory -Force -Path $backupDir | Out-Null

$skillsPath = Join-Path $TargetWorkspace ".agents\skills"
if (Test-Path $skillsPath) {
    # Backup matching folders
    $roles = "r0-orchestrator", "r1-content-production", "r2-seo-serp-intelligence", "r3-internal-linking", "r4-schema-entity-graph", "r5-iranian-trust", "r6-ux-cro", "r7-quality-assurance", "r8-strategy-conflict-resolution", "r9-shopfa-verification", "r10-shopfa-integration", "r11-research-intelligence"
    foreach ($r in $roles) {
        $fullPath = Join-Path $skillsPath $r
        if (Test-Path $fullPath) {
            Copy-Item -Path $fullPath -Destination $backupDir -Recurse -Force
        }
    }
}

# Copy payload skills
$sourceSkills = Join-Path $PSScriptRoot "..\payload\skills"
Copy-Item -Path "$sourceSkills\*" -Destination $skillsPath -Recurse -Force

# Create Installation Record
$recordPath = Join-Path $TargetWorkspace ".agents\ARIA-G-v1.0.1-INSTALLATION-RECORD.md"
$recordContent = "# Installation Record`r`n* **Package:** ARIA-G v1.0.1`r`n* **Date:** $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')`r`n"
Set-Content -Path $recordPath -Value $recordContent

Write-Host "ARIA-G v1.0.1 installed successfully under $skillsPath"
