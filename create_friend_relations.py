import json

from neo4j import GraphDatabase

"""
create FRIEND relationship, given one user and a set of his/her friends

MATCH (u1:User) WHERE u1.user_id = "eIeftwebaehpl"
for each friend
    MATCH (u2:User) WHERE u2.user_id = "webae"
    MERGE (u1) -[:FRIEND]- (u2)
    
"""


class Neo4jDriver:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_knows(self, my_id, friend_id):
        with self.driver.session() as session:
            session.write_transaction(self._create_knows_relation, my_id, friend_id)

    # TODO: create friend relationships
    @staticmethod
    def _create_knows_relation(tx, my_id, friends):
        tx.run()


if __name__ == "__main__":
    driver = Neo4jDriver("neo4j://localhost:7687", "neo4j", "neo4j_team")

    # create Business node
    with open("data/user.json", "r") as f:
        line = f.readline()
        while line:
            item = json.loads(line)
            myId = item["user_id"]
            myFriends = [x.strip() for x in item["friends"].split(',')]
            driver.create_knows(myId, myFriends)
            line = f.readline()

    driver.close()
