import json

from neo4j import GraphDatabase


class Neo4jDriver:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_user(self, user):
        with self.driver.session() as session:
            session.write_transaction(self._create_user_node, user)

    @staticmethod
    def _create_user_node(tx, user):
        tx.run("CREATE (:User {"
               "user_id : $user_id, "
               "name : $name, "
               "review_count : $review_count, "
               "average_stars: $average_stars"
               " })",
               user_id=user["user_id"],
               name=user["name"],
               review_count=user["review_count"],
               average_stars=user["average_stars"]
               )


if __name__ == "__main__":
    driver = Neo4jDriver("neo4j://localhost:7687", "neo4j", "neo4j_team")

    # create Business node
    with open("data/user.json", "r") as f:
        line = f.readline()
        while line:
            item = json.loads(line)
            driver.create_user(item)
            line = f.readline()

    driver.close()
