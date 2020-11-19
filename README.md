# neo4j-project
A project based on neo4j graph database

# Step of deploying cluster neo4j database
1. Install Docker Desktop
2. Create directory ~/neo4j/core1/data; ~/neo4j/core1/conf; ~/neo4j/core1/logs;    
~/neo4j/core2/data; ~/neo4j/core2/conf; ~/neo4j/core2/logs;    
~/neo4j/core3/data; ~/neo4j/core3/conf; ~/neo4j/core3/logs;   
3. run `sh dock_neo4j_cluster.sh` in command line
4. configure multi-data center load balancing:    
copy `neo4j.conf` file into directory `~/neo4j/core1/conf`, `~/neo4j/core2/conf`, `~/neo4j/core3/conf`
and then restart server.
5. run `neo4jDriver.py` to test database connection.

## Data Source
Uncomment lines in prune_data.py, and change the filepath of orginial data to your own filepath in the code.        
This file will produce pruned data for our project.
