import json


serialized = """{ "title" : "Data Science Book",
                  "author" : "Joel Grus",
                  "publicationYear" : 2019,
                  "topics" : [ "data", "science", "data science"] }"""

# Разобрать JSON, создав Python'овский словарь
deserialized = json.loads(serialized)

assert deserialized["publicationYear"] == 2019
assert "data science" in deserialized["topics"]
