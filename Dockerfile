# Use official Python image
FROM python:3.13-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first (faster builds)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Run the script
CMD ["python3", "checker.py"]