#!/bin/bash
set -e

alembic upgrade head

if [ -d "/app/app" ]; then
    cd /app/app
else
    exit 1
fi
exec python3 -m uvicorn main:main --host 0.0.0.0 --port 8000