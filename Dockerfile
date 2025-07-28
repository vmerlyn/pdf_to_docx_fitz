# --- Stage 1: Builder (Optional: if you want slimmer final image) -- #
FROM python:3.11-slim AS base

# Install system-level dependencies
RUN apt-get update && apt-get install -y \
    libmagic-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies (from Rye-managed pyproject.toml)
# Rye uses pyproject.toml but Docker needs requirements.txt or similar
RUN pip install --upgrade pip && \
    pip install fastapi uvicorn pymupdf python-docx python-multipart routes

# Expose FastAPI port
EXPOSE 8000

# Default command
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
