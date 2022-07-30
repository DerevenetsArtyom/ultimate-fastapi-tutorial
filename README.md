# The Ultimate FastAPI Tutorial

For detailed explanations and to follow along:

- Read the [blog post series](https://christophergs.com/tutorials/ultimate-fastapi-tutorial-pt-1-hello-world/)
- [Order the course](https://academy.christophergs.com/courses/fastapi-for-busy-engineers/)

## Local Setup

1. `pip install poetry` (or safer, follow the instructions: https://python-poetry.org/docs/#installation).
2. Install dependencies `cd` into the directory where the `pyproject.toml` is located then `poetry install`.
3. Run the DB migrations via poetry `poetry run python app/prestart.py` (only required once) (Unix users can use the bash script if preferred).
4. Run the FastAPI server via poetry with the bash script: `poetry run ./run.sh`.
5. Open `http://localhost:8001/`.

To stop the server, press CTRL+C.

## Run with Docker

Make sure you have Docker and [Docker Compose](https://docs.docker.com/compose/install/) installed.

1. Run `docker-compose -f docker-compose.local.yml up -d` (this will download the postgres
   image and build the image for the recipe app - takes about 5 mins).
2. Visit `http://localhost:8001/docs`.
