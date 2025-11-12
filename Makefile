.PHONY: dev test run api


dev:
pip install -r requirements.txt
pip install -e .


test:
pytest


api:
uvicorn api.app:app --host 0.0.0.0 --port 8080 --reload
