import json

from neo4j import GraphDatabase


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
        tx.run("MATCH (a:User), (b:Business)"
               "WHERE a.user_id = $user_id AND b.business_id = $business_id"
               "CREATE (a) -[:Has_Reviewed {stars: $stars, date: $date }]-> (b)",
               user_id=review["user_id"],
               business_id=review["name"],
               stars=review["review_count"],
               date=review["average_stars"]
               )


if __name__ == "__main__":
    driver = Neo4jDriver("neo4j://localhost:7687", "neo4j", "neo4j_team")

    # create Business node
    with open("data/review.json", "r") as f:
        line = f.readline()
        while line:
            item = json.loads(line)
            driver.create_review(item)
            line = f.readline()

    driver.close()
