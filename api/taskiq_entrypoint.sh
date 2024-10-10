#!/bin/bash
set -e

if [ -d "/app/app" ]; then
    cd /app/app
else
    exit 1
fi

# Запускаем планировщик в фоне
taskiq scheduler services.scheduler:scheduler &

# Запускаем воркер в фоне
taskiq worker services.scheduler:broker &

# Ждем завершения обоих процессов
wait