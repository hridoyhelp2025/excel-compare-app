# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
COPY excel_compare_agent.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080
EXPOSE 8080

# Run Streamlit
CMD ["streamlit", "run", "excel_compare_agent.py", "--server.port=8080", "--server.address=0.0.0.0"]
