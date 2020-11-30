import json

from neo4j import GraphDatabase

"""
if    category not exist, create it, add relationship between category and business node
else  select category, add relationship between category and business node

Cypher language:
MATCH (b :Business) WHERE b.business_id = "nIEhsGbw0vJuYl05bzzj6Q"
UNWIND $categories AS category
MERGE (cat: Category { category_name: category })
MERGE (b) -[:HAS_CATEGORY] -> (cat)

"""


class Neo4jDriver:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_categories(self, businessId, categories):
        with self.driver.session() as session:
            session.write_transaction(self._create_categories_relation, businessId, categories)

    @staticmethod
    def _create_categories_relation(tx, businessId, categories):
        tx.run(
            "MATCH (b:Business) WHERE b.business_id = $businessId\n"
            "UNWIND $categories AS category\n"
            "MERGE (cat:Category { category_name: category })\n"
            "MERGE (b) -[:HAS_CATEGORY]-> (cat)",
            categories=categories,
            businessId=businessId
        )


if __name__ == "__main__":
    driver = Neo4jDriver("neo4j://localhost:7687", "neo4j", "neo4j_team")

    with open("data/business.json", "r") as f:
        line = f.readline()
        lineNum = 1

        try:
            while line:
                if lineNum % 100 == 0:
                    print(lineNum)
                if lineNum < 4490:
                    line = f.readline()
                    lineNum += 1
                    continue
                else:
                    item = json.loads(line)
                    businessId = item["business_id"]
                    cats = item["categories"]
                    if cats is not None:
                        categories = [x.strip() for x in item["categories"].split(',')]
                        driver.create_categories(businessId, categories)
                    line = f.readline()
                    lineNum += 1
        finally:
            print(lineNum)

    driver.close()
