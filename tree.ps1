function Show-Tree {

    param (
        [string]$Path = ".",
        [string[]]$Exclude = @(
            "media",
            "staticfiles",
            "__pycache__",
            ".git",
            "node_modules"
        ),
        [string]$OutputFile = "structure.txt"
    )

    $script:tree = @()

    function Get-Tree {

        param (
            [string]$CurrentPath,
            [string]$Prefix = ""
        )

        $items = Get-ChildItem $CurrentPath |
            Where-Object {
                $Exclude -notcontains $_.Name
            } |
            Sort-Object @{Expression = {$_.PSIsContainer}; Descending = $true}, Name

        for ($i = 0; $i -lt $items.Count; $i++) {

            $item = $items[$i]
            $isLast = ($i -eq $items.Count - 1)

            if ($isLast) {
                $connector = "\--"
                $newPrefix = "$Prefix    "
            }
            else {
                $connector = "+--"
                $newPrefix = "$Prefix|   "
            }

            if ($item.PSIsContainer) {
                $icon = "[DIR]"
            }
            else {
                $icon = "[FILE]"
            }

            $script:tree += "$Prefix$connector $icon $($item.Name)"

            if ($item.PSIsContainer) {
                Get-Tree -CurrentPath $item.FullName -Prefix $newPrefix
            }
        }
    }

    $script:tree += "[ROOT] $Path"

    Get-Tree -CurrentPath $Path

    $script:tree | Out-File -FilePath $OutputFile -Encoding utf8

    Write-Host "Saved to $OutputFile"
}

Show-Tree
