"""
if    category not exist, create it, add relationship between category and business node
else  select category, add relationship between category and business node

Cypher language:
MATCH (b) WHERE b.business_id = "nIEhsGbw0vJuYl05bzzj6Q"
for each category of b
    MERGE (cat: Category { category_name: "Restaurant" })
    CREATE (b) -[:HAS_CATEGORY] -> (cat)

"""