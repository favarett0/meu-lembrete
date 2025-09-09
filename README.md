# Meu Lembrete (Starter)

Este é um **starter** minimalista para você subir no **Google Cloud Run** com **Cloud Build (CI/CD)** a partir do GitHub.

## Como usar (resumo)
1. Crie o repositório **meu-lembrete** no GitHub.
2. Faça upload destes arquivos (ou `git push`).
3. No Google Cloud:
   - Habilite as APIs: Cloud Run, Cloud Build, Artifact Registry.
   - Crie um repositório no Artifact Registry (Docker): `meulembrete` na região `southamerica-east1`.
   - Crie um **Trigger** do Cloud Build conectado ao seu GitHub e a este `cloudbuild.yaml` (branch `main`).
4. Faça um push e veja o deploy automático no Cloud Run.
  
