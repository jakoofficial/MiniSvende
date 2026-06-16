# FROM python:3.11-slim

# WORKDIR /backend

# COPY /Database/requirements.txt .

# RUN pip install -r ./requirements.txt

# COPY ./Database ./backend

# ENV PYTHONPATH="/backend"

# EXPOSE 8000

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM python:3.11-slim
WORKDIR /backend
COPY /Database/requirements.txt .
RUN pip install -r ./requirements.txt
COPY ./Database ./Backend
# ENV PYTHONPATH="/Database"
EXPOSE 8000
CMD ["uvicorn", "Backend.main:app", "--host", "0.0.0.0", "--port", "8000"]