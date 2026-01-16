from llm.llm_check import llm_analyze

print(llm_analyze("SELECT * FROM users WHERE id=1"))
print(llm_analyze("SELECT * FROM users WHERE id=1 OR 1=1"))
print(llm_analyze('db.users.find({username: {$ne: null}})'))
