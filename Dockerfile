FROM python:3.9

WORKDIR /pythonProject2

COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt
RUN chmod +x /pythonProject2/entrypoint.sh


ENTRYPOINT ["/pythonProject2/entrypoint.sh"]
