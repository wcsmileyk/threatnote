FROM python:3.12-slim

# whois: CLI used by the python "whois" package for domain enrichment
# pango/harfbuzz/fonts: runtime libraries WeasyPrint needs to render PDF reports
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
       whois \
       libpango-1.0-0 \
       libpangoft2-1.0-0 \
       libharfbuzz-subset0 \
       fonts-dejavu-core \
  && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 5000

# The rq worker overrides this command in docker-compose.yaml
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "--access-logfile", "-", "main:app"]
