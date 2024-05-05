#!/bin/sh

python -m venv .venv &&\
  ./.venv/bin/pip install --upgrade pip &&\
  ./.venv/bin/pip install -r requirements.txt &&\
  ./.venv/bin/python -m playwright install
  
ollama serve & 
ollama pull gemma:2b
ollama pull nomic-embed-text
pkill ollama
