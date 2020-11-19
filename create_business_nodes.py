import json

from neo4j import GraphDatabase


class Neo4jDriver:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_business(self, business):
        with self.driver.session() as session:
            session.write_transaction(self._create_business_node, business)

    @staticmethod
    def _create_business_node(tx, business):
        tx.run("CREATE (:Business { "
               "business_id : $business_id,"
               "name : $name,"
               "address : $address,"
               "city : $city,"
               "state : $state,"
               "postal_code : $postal_code,"
               "latitude : $latitude,"
               "longitude : $longitude,"
               "stars : $stars"
               " })",
               business_id=business["business_id"],
               name=business["name"],
               address=business["address"],
               city=business["city"],
               state=business["state"],
               postal_code=business["postal_code"],
               latitude=business["latitude"],
               longitude=business["longitude"],
               stars=business["stars"])


if __name__ == "__main__":
    driver = Neo4jDriver("neo4j://localhost:7687", "neo4j", "neo4j_team")

    # create Business node
    with open("data/business.json", "r") as f:
        line = f.readline()
        while line:
            item = json.loads(line)
            driver.create_business(item)
            line = f.readline()

    driver.close()
