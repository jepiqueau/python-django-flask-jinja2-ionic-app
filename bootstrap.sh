#!/bin/sh
export FLASK_APP=./index.py
source appenv/bin/activate
flask run -h 0.0.0.0
