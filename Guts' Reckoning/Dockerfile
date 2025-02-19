FROM python:3.9-alpine

WORKDIR /app
COPY server.py .

# Expose the port that the server listens on (5001 in our code)
EXPOSE 5001

# When the container starts, run the server automatically
CMD ["python", "server.py"]

