#!/bin/bash
####https://stackoverflow.com/questions/19331497/set-environment-variables-from-file-of-key-value-pairs
# create egg file in python environment
# python setup.py install

# # to start services.
# sed -i 's/\r//g' .env.development
# export $(grep -v '^#' .env.development | xargs)
# cd src
python -m uvicorn blog.main:app --host 127.0.0.1 --port 8787 --reload