# Dockerfile
# Base image
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy application files
COPY . .
COPY .env .env
COPY requirements.txt .



# Install required packages
RUN apt-get update && apt-get install -y \
    build-essential \
    && apt-get clean\
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

RUN pip install -r requirements.txt




# Expose Gradio app default port
EXPOSE 7860

# Set environment variable for the Google API Key securely
ENV OPENAI_API_KEY="skprojAxAiLtm412g2ZPP8tz3m8mL6K622S0hdWcn6FAzV7kLvRgBzuroUUBvCKykCP9hbwc_aYg8yoKT3BlbkFJnorVhWNqNdqgdld9vqekKUHx1Skyhe42kYvexeOJ7WjvzTRtcOwq8obXfq-s7ufuJn6Ak1TEgA"

# Command to run the application
CMD ["python", "app.py","--host=0.0.0.0","--port=7860","sh"]
