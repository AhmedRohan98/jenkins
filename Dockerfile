# Use the official Python 3.10 image as the base
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files into the container
COPY . .

# Expose the port the app will run on (e.g., 3000)
EXPOSE 3000

# Specify the command to run your Flask application
CMD ["python", "api.py"]
