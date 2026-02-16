#official python image
FROM python:3.12-slim

# Prevent .pyc file
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# set working directory to app
WORKDIR /app

# copy requirements.txt file
COPY requirements.txt .

# installing the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy all the project files to the working directory
COPY . .

RUN python manage.py collectstatic --noinput

# command to run the program
CMD [ "gunicorn", "tms_backend.wsgi:application", "--bind", "0.0.0.0:8000" ]

