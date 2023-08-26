FROM python:3.11

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

# Install the food101 tensorflow dataset
RUN python app.py
