FROM python:3.9-alpine



WORKDIR /app

COPY hrdwr1.py .



# Install socat for better stability

RUN apk add --no-cache socat



# Start a listener that executes Python script for each connection

CMD ["sh", "-c", "while true; do socat TCP-LISTEN:,reuseaddr,fork EXEC:'python3 /app/hrdwr1.py',pty,stderr; done"]

