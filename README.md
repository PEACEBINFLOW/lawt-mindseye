# LAW-T (MindsEye-guided)
Time-labeled, self-evolving micro-framework for event cognition. Core loop:
**Event → Time Label → Laws → Decision → Memory**


## Quick start (Codespaces)
1. Open in GitHub Codespaces
2. Terminal → `make dev`
3. Run API → `make api`
4. Test → `make test`


### Ingest
```bash
curl -X POST http://localhost:8080/ingest \
-H 'Content-Type: application/json' \
-d '{"source":"web","type":"click","payload":{"path":"/"}}'
---


## 🏁 How to use this in a brand-new GitHub repo
1. Create an empty repo on GitHub (public or private)
2. Open **Codespaces → New with this repo**
3. Copy these files into the repo structure
4. Run `make dev` then `make api`
5. Commit & push; CI will run tests automatically


---


## 🔜 Next steps
- Add Timescale/Redis backends (`src/lawt/storage/…`)
- Make Laws data-driven (YAML/JSON DSL)
- Add Feedback Loop endpoint and persistence
- Add React UI in `/ui` for live event feed & decisions
