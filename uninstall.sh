#!/bin/bash

# Get the current script directory
SCRIPT_DIR=$(dirname "$(realpath "$0")")

# Define the Python interpreter and script path
PYTHON_PATH="$SCRIPT_DIR/.venv/bin/python3"
SCRIPT_PATH="$SCRIPT_DIR/fetch_aqi.py"

# Cron job commands
REBOOT_CRON_JOB="@reboot sleep 5; $PYTHON_PATH $SCRIPT_PATH"
TWO_MINUTES_CRON_JOB="*/2 * * * * $PYTHON_PATH $SCRIPT_PATH"

# Remove the cron jobs if they exist
crontab -l 2>/dev/null | grep -v -F "$REBOOT_CRON_JOB" | crontab -
crontab -l 2>/dev/null | grep -v -F "$TWO_MINUTES_CRON_JOB" | crontab -

echo "Cron jobs removed successfully!"