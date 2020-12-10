import json

from neo4j import GraphDatabase

"""
create REVIEW relationship, given a reviewline

MATCH (u:User) WHERE u.user_id = "eIeftwebaehpl"
MATCH (b:Business) WHERE b.business_id = "abcdfrEfdf"
MERGE (u) -[:REVIEW { review_id: $review_id, stars: $stars, date: $date }]-> (b) 

"""


class Neo4jDriver:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_review(self, review):
        with self.driver.session() as session:
            session.write_transaction(self._create_review_relation, review)

    @staticmethod
    def _create_review_relation(tx, review):
        tx.run("MATCH (u:User) WHERE u.user_id = $user_id\n"
               "MATCH (b:Business) WHERE b.business_id = $business_id\n"
               "MERGE (u) -[:REVIEW { review_id: $review_id, stars: $stars, date: $date }]-> (b)",
               review_id=review["review_id"],
               user_id=review["user_id"],
               business_id=review["business_id"],
               stars=review["stars"],
               date=review["date"]
               )


if __name__ == "__main__":
    driver = Neo4jDriver("neo4j://localhost:7687", "neo4j", "neo4j_team")

    with open("data/review_test.json", "r") as f:
        line = f.readline()
        lineNum = 1
        try:
            while line:
                if lineNum % 10000 == 0:
                    print(lineNum)
                # if lineNum < 1111:
                #     line = f.readline()
                #     lineNum += 1
                #     continue
                else:
                    item = json.loads(line)
                    driver.create_review(item)
                    line = f.readline()
                    lineNum += 1

        finally:
            print(lineNum)

    driver.close()
