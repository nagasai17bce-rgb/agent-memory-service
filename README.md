# Agent Memory Service

A runnable memory primitive for AI agents. It stores scoped memories with importance metadata and returns the most recent recall window.

## Run
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
uvicorn app.main:app --reload
```

POST `{"value":"customer prefers email"}` to `/v1/run`.

## Production extensions
Back the interface with a durable store, add tenant isolation, semantic retrieval, retention policies, encryption, deletion APIs, and memory provenance.
