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

    def create_friends(self, myId, myFriends):
        with self.driver.session() as session:
            session.write_transaction(self._create_friends_relation, myId, myFriends)

    @staticmethod
    def _create_friends_relation(tx, myId, myFriends):
        tx.run(
            "MATCH (u1:User) WHERE u1.user_id = $myId\n"
            "UNWIND $myFriends as friend\n"
            "MATCH (u2:User) WHERE u2.user_id = friend\n"
            "MERGE (u1) -[:FRIEND]- (u2)",
            myId=myId,
            myFriends=myFriends
        )


if __name__ == "__main__":
    driver = Neo4jDriver("neo4j://localhost:7687", "neo4j", "neo4j_team")

    # create Business node
    with open("data/user.json", "r") as f:
        line = f.readline()
        lineNum = 1
        try:
            while line:
                if lineNum % 1000 == 0:
                    print(lineNum)
                if lineNum < 136345:
                    line = f.readline()
                    lineNum += 1
                    continue
                else:
                    item = json.loads(line)
                    myId = item["user_id"]
                    friends = item["friends"]
                    if friends != "None":
                        myFriends = [x.strip() for x in item["friends"].split(',')]
                        driver.create_friends(myId, myFriends)
                    line = f.readline()
                    lineNum += 1
        finally:
            print(lineNum)

    driver.close()
