FROM python:2.7

RUN mkdir -p /app
WORKDIR /app

RUN pip install --no-cache-dir Django==1.7

COPY . /app

RUN apt-get update && apt-get install -y \
		sqlite3 \
		gcc \
	--no-install-recommends && rm -rf /var/lib/apt/lists/*

EXPOSE 80
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
