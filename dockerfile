FROM python:3.12-alpine

RUN apk upgrade --no-cache

# Download the latest installer
ADD https://astral.sh/uv/install.sh /uv-installer.sh

# Run the installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Ensure the installed binary is on the PATH
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

COPY . /app

RUN uv sync --locked

ENTRYPOINT ["uv", "run", "./src/main.py"]