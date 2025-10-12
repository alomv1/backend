# Backend Labs

## Prerequisites

- Python 3.7+ installed
- Docker installed 
- (Optional) Docker Compose installed or use Docker CLI’s `docker compose`

---

## Local Setup Without Docker

Follow these steps to run the project locally on your machine without Docker.

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```
### 2. Create and activate a virtual environment

```bash
python3 -m venv env
source env/bin/activate  
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI app

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Running with Docker

### 1. Build the Docker Image

```bash
docker build -t <YOUR_CONTAINER_NAME> .
```

### 2. Run the Docker container

```bash
docker run -p 8000:8000 <YOUR_CONTAINER_NAME>

```

## Running with Docker Compose

### 1. Run

```bash
docker-compose up --build
```


## Deployment

This project is deployed and running on [Render.com](https://render.com).

You can access here:

**[https://backend-fu08.onrender.com/healthcheck](https://backend-fu08.onrender.com/healthcheck)**
