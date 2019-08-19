#!/bin/bash

NAME="Trivago"
USER=ishanbhatt
GROUP=domain
NUM_WORKERS=10

export PYTHONUNBUFFERED=TRUE

echo "Starting $NAME"

# Start your gunicorn
exec gunicorn runserver:app -b 0.0.0.0:5300 \
  --name $NAME \
  --workers $NUM_WORKERS \
  --enable-stdio-inheritance \
  --log-file logs/gunicorn.log \
  --capture-output \
  --log-level debug