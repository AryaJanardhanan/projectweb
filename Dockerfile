# Use an official Python image as the base
FROM python:3.11  

# Set the working directory inside the container
WORKDIR /app  

# Copy only requirements.txt first, to leverage Docker caching
COPY requirements.txt .  

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt  

# Copy the rest of the project files
COPY . .  

# Expose the port Django runs on
EXPOSE 8000  

# Default command to run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
