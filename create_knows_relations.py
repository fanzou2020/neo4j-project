import json

from neo4j import GraphDatabase


class Neo4jDriver:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_knows(self, my_id, friend_id):
        with self.driver.session() as session:
            session.write_transaction(self._create_knows_relation, my_id, friend_id)

    @staticmethod
    def _create_knows_relation(tx, my_id, friend_id):
        tx.run("MATCH(a:User), (b:User)"
               "WHERE a.user_id=$my_id AND b.user_id=$friend_id"
               "CREATE (a) -[:Knows]-> (b)",
               my_id=my_id,
               friend_id=friend_id
               )


if __name__ == "__main__":
    driver = Neo4jDriver("neo4j://localhost:7687", "neo4j", "neo4j_team")

    # create Business node
    with open("data/user.json", "r") as f:
        line = f.readline()
        while line:
            item = json.loads(line)
            myId = item["user_id"]
            myFriends = [x.strip() for x in item["friends"].split(',')]
            for myFriend in myFriends:
                driver.create_knows(myId, myFriend)
            line = f.readline()

    driver.close()
