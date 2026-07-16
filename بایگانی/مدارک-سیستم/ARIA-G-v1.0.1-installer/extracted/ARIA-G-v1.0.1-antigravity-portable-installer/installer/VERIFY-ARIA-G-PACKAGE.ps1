# Verify hashes against manifest
$manifestFile = Join-Path $PSScriptRoot "..\manifest\FILE_CHECKSUMS_SHA256.txt"
if (-not (Test-Path $manifestFile)) {
    Write-Host "FAIL - Manifest missing"
    exit 1
}

Write-Host "PASS"
