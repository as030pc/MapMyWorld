FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./
COPY . ./
RUN pip install --no-cache-dir -r requirements.txt
ENV PATH="/app/alembic:$PATH"
EXPOSE 8000

CMD alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port 8000
