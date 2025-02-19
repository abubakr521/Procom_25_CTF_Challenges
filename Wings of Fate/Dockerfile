FROM python:3.9-alpine

WORKDIR /app
COPY osint2.py .

RUN apk add --no-cache socat

EXPOSE 4567

CMD ["sh", "-c", "socat TCP-LISTEN:4567,reuseaddr,fork EXEC:'python osint2.py'"]