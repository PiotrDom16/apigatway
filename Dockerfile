FROM python:3.12


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 7001

ENTRYPOINT ["python3", "apigateway.py"]