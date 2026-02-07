#!/bin/sh
set -e
if [ $DEBUG -eq 0 ]; then
    echo Starting in normal mode
    python3 ./main.py
fi
if [ $DEBUG -eq 1 ]; then
    echo Starting in debug mode
    echo Debugpy is listening on 3223
    python -m debugpy --listen 0.0.0.0:3223 ./main.py
fi

exec "$@"