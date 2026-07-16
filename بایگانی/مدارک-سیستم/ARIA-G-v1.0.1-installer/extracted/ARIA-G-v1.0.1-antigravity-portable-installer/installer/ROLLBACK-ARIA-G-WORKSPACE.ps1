param (
    [Parameter(Mandatory=$true)]
    [string]$TargetWorkspace,
    
    [Parameter(Mandatory=$true)]
    [string]$BackupPath,
    
    [Parameter(Mandatory=$true)]
    [switch]$ConfirmRollback
)

# Restore folders
$skillsPath = Join-Path $TargetWorkspace ".agents\skills"
$roles = "r0-orchestrator", "r1-content-production", "r2-seo-serp-intelligence", "r3-internal-linking", "r4-schema-entity-graph", "r5-iranian-trust", "r6-ux-cro", "r7-quality-assurance", "r8-strategy-conflict-resolution", "r9-shopfa-verification", "r10-shopfa-integration", "r11-research-intelligence"

foreach ($r in $roles) {
    $src = Join-Path $BackupPath $r
    if (Test-Path $src) {
        $dst = Join-Path $skillsPath $r
        if (Test-Path $dst) { Remove-Item -Path $dst -Recurse -Force }
        Copy-Item -Path $src -Destination $dst -Recurse -Force
    }
}

# Create rollback record
$recordPath = Join-Path $TargetWorkspace ".agents\ROLLBACK-RECORD-v1.0.1.txt"
Set-Content -Path $recordPath -Value "Rollback executed on $(Get-Date)"

Write-Host "Rollback complete."
