FROM python:3.14-alpine
WORKDIR /bot
RUN pip install --upgrade pip poetry
COPY ./pyproject.toml ./poetry.toml ./poetry.lock ./
RUN poetry install --no-interaction
COPY . .
RUN chmod +x ./prestart.sh
RUN chmod +x ./start.sh
ENTRYPOINT ["./prestart.sh"]
CMD ["./start.sh"]