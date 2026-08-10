FROM python:3.12-slim

# Install Chromium, ChromeDriver and required packages
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    ca-certificates \
    curl \
    unzip \
    fonts-liberation \
    libnss3 \
    libxss1 \
    libasound2 \
    libgbm1 \
    libxshmfence1 \
    xvfb \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Create a virtual environment inside the image
RUN python -m venv /opt/venv

# Use virtual environment
ENV PATH="/opt/venv/bin:$PATH"

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Flask port
EXPOSE 5000

# Start Flask application
CMD ["python", "app.py"]