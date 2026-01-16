from fastapi import FastAPI
from pydantic import BaseModel
from api.sql_guard import execute_safe_sql
from api.nosql_guard import execute_safe_nosql
app = FastAPI()

class SQLRequest(BaseModel):
    query: str

@app.post("/sql/execute")
def secure_sql(request: SQLRequest):
    return execute_safe_sql(request.query)


class NoSQLRequest(BaseModel):
    query: str

@app.post("/nosql/execute")
def secure_nosql(request: NoSQLRequest):
    return execute_safe_nosql(request.query)
