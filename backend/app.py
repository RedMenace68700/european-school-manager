from fastapi import FastAPI
import os
import psycopg2

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from FastAPI"}

@app.get("/db-test")
def db_test():
    db_url = os.getenv("DATABASE_URL")
    try:
        conn = psycopg2.connect(db_url)
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()
        cur.close()
        conn.close()
        return {"db_version": version}
    except Exception as e:
        return {"error": str(e)}
