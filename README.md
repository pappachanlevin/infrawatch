# InfraWatch 🔍

A real-time website monitoring system that detects downtime and tracks response times — storing every result permanently in PostgreSQL.

## What it does

Every 60 seconds InfraWatch visits a list of URLs, checks if they are alive, measures response time, and saves every result to a database. If a site goes down you know within 60 seconds — not when a customer complains.

## Demo

```
[14:00:40] ✓  https://google.com  330ms
[14:00:40] ✓  https://github.com  189ms
[14:00:41] ✗  https://httpbin.org/status/500  466ms
---
```

## Tech stack

- **Python** — async URL health checks
- **PostgreSQL** — stores every result permanently
- **Docker** — runs the database as a container
- **SQLAlchemy** — connects Python to PostgreSQL
- **GitHub Actions** — CI/CD pipeline *(coming soon)*
- **Terraform + AWS** — cloud deployment *(coming soon)*
- **Kubernetes** — container orchestration *(coming soon)*
- **AI agent** — incident analysis in plain English *(coming soon)*

## Project structure

```
infrawatch/
├── checker.py      # main script — pings URLs and saves results
├── database.py     # database connection and table definition
├── .env            # configuration (not committed)
└── README.md
```

## How to run locally

**1. Clone the repo**
```
git clone git@github.com:pappachanlevin/infrawatch.git
cd infrawatch
```

**2. Install dependencies**
```
pip3 install httpx sqlalchemy psycopg2-binary python-dotenv
```

**3. Start the database**
```
docker run --name infrawatch-db \
  -e POSTGRES_USER=infrawatch \
  -e POSTGRES_PASSWORD=secret \
  -e POSTGRES_DB=infrawatch \
  -p 5432:5432 \
  -d postgres
```

**4. Create your .env file**
```
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=infrawatch
POSTGRES_USER=infrawatch
POSTGRES_PASSWORD=secret
MONITOR_TARGETS=https://google.com,https://github.com
```

**5. Run**
```
python3 checker.py
```

## Roadmap

- [x] Async URL monitoring every 60 seconds
- [x] PostgreSQL database with full history
- [x] Docker containerisation
- [ ] Docker Compose — one command setup
- [ ] GitHub Actions CI/CD pipeline
- [ ] Terraform infrastructure on AWS
- [ ] Kubernetes production deployment
- [ ] Prometheus + Grafana monitoring
- [ ] AI agent for incident analysis

## Author

Built by [@pappachanlevin](https://github.com/pappachanlevin)

