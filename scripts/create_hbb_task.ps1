$action = New-ScheduledTaskAction -Execute 'python.exe' -Argument 'C:\Users\prana\hbb-site\scripts\preflight.py' -WorkingDirectory 'C:\Users\prana\hbb-site'
$trigger = New-ScheduledTaskTrigger -Daily -At 00:00
Register-ScheduledTask -TaskName 'hbb-preflight' -Action $action -Trigger $trigger -Description 'Run Her Balanced Body preflight checks daily' -Force
if ($?) { Write-Host 'Task created successfully' } else { Write-Output 'Failed to create task' }
