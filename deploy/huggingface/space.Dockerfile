# Hugging Face Space (Docker) — 3 lignes.
# L'image est construite et poussee automatiquement sur GHCR par GitHub Actions
# (voir .github/workflows/deploy.yml). Rendre le package GHCR public, puis
# creer un Space "Docker" avec CE fichier comme Dockerfile.
FROM ghcr.io/sow221/credlens/api:latest

ENV PORT=7860
EXPOSE 7860
