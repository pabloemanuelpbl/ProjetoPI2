FROM python:3

WORKDIR /ProjetoPI2

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src .

CMD [ "gunicorn", "application:app", "--bind", "0.0.0.0"]

EXPOSE 8000