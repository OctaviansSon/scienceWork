import psycopg2
from datetime import datetime
from ml.hybrid import hybrid_detect

#db conf
DB_CONFIG = {
    "dbname": "test_security",      # dbname
    "user": "postgres",             # user
    "password": "Diyor_080",      #ur user pass
    "host": "localhost",
    "port": 5432
}

# query guard
def execute_safe_sql(query: str):
    # 1 check by model hubrid
    analysis = hybrid_detect(query)

    # 2. Logs for data
    log = {
        "query": query,
        "decision": analysis["decision"],
        "source": analysis["source"],
        "confidence": analysis["confidence"],
        "timestamp": datetime.now().isoformat()
    }

    # 3. vulnerable scan
    if analysis["decision"] == "VULNERABLE":
        return {
            "status": "BLOCKED",
            "log": log
        }

    # 4. else execute
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute(query)

    try:
        result = cur.fetchall()
    except psycopg2.ProgrammingError:
        result = "OK"

    conn.commit()
    cur.close()
    conn.close()

    return {
        "status": "EXECUTED",
        "result": result,
        "log": log
    }
