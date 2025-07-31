FROM python:3.11-slim

RUN apt update && apt install -y python3-venv make ocaml opam m4

RUN python3 -m venv /opt/venv

RUN /opt/venv/bin/pip install flask

ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app

COPY . .

RUN make

EXPOSE 5000

CMD ["python3", "marina_api.py"]