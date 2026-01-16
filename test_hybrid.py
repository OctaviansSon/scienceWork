from ml.hybrid import hybrid_detect

tests = [
    "SELECT * FROM users WHERE id=1",
    "SELECT * FROM users WHERE id=1 OR 1=1",
    "db.users.find({username: {$ne: null}})"
]

for q in tests:
    print("QUERY:", q)
    result = hybrid_detect(q)
    print("RESULT:", result)
    print("-" * 50)
