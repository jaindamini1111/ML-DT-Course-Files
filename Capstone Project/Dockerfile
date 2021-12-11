FROM python:3.7-slim

RUN pip install pipenv
WORKDIR /app
COPY . .
# RUN pip install -r requirements.txt
RUN pipenv install --system --deploy

EXPOSE 6969

CMD ["python", "predictdocker.py"]