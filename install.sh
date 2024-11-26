#!/bin/bash

# Define the Python interpreter and script path
PYTHON_PATH="$HOME/work/aqi-collector/.venv/bin/python3"
SCRIPT_PATH="$HOME/work/aqi-collector/fetch_aqi.py"

# Check if the Python path exists
if [ ! -f "$PYTHON_PATH" ]; then
    echo "Error: Python interpreter not found at $PYTHON_PATH"
    exit 1
fi

# Check if the script exists
if [ ! -f "$SCRIPT_PATH" ]; then
    echo "Error: Python script not found at $SCRIPT_PATH"
    exit 1
fi

# Cron job to run after reboot
REBOOT_CRON_JOB="@reboot sleep 5; $PYTHON_PATH $SCRIPT_PATH"

# Cron job to run every 2 minutes
TWO_MINUTES_CRON_JOB="*/2 * * * * $PYTHON_PATH $SCRIPT_PATH"

# Add the cron jobs if they aren't already present
(crontab -l 2>/dev/null | grep -Fx "$REBOOT_CRON_JOB") || (crontab -l 2>/dev/null; echo "$REBOOT_CRON_JOB") | crontab -
(crontab -l 2>/dev/null | grep -Fx "$TWO_MINUTES_CRON_JOB") || (crontab -l 2>/dev/null; echo "$TWO_MINUTES_CRON_JOB") | crontab -

echo "Cron jobs added successfully"
