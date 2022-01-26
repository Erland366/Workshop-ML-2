FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./model /model

COPY ./app /app


ADD requirements.txt . 

RUN pip install -r requirements.txt \    
    && rm -rf /root/.cache 

CMD ["uvicorn", "fastapi_iris:app", "--host", "0.0.0.0", "--port", "8085"]