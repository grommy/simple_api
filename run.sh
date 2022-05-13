#!/bin/bash
#pip install -r requirements.txt
gunicorn -b 0.0.0.0:5000 application:app --access-logfile -