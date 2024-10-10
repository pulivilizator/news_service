#!/bin/bash
set -e

if [ -d "/app/app" ]; then
    cd /app/app
else
    exit 1
fi

taskiq scheduler services.scheduler:scheduler &

taskiq worker services.scheduler:broker &

wait