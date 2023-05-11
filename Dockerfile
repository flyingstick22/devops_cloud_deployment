FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y

COPY . .

RUN pip install streamlit

EXPOSE 8501

#CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

#This works for Heroku: 
CMD streamlit run --server.port $PORT app.py



