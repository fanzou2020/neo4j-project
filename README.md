# neo4j-project
A project based on neo4j graph database

## Steps of deploying cluster neo4j database
1. Install Docker Desktop
2. Create directory ~/neo4j/core1/data; ~/neo4j/core1/conf; ~/neo4j/core1/logs;    
~/neo4j/core2/data; ~/neo4j/core2/conf; ~/neo4j/core2/logs;    
~/neo4j/core3/data; ~/neo4j/core3/conf; ~/neo4j/core3/logs;   
3. Run `sh dock_neo4j_cluster.sh` in command line at home directory `~`.
4. Configure multi-data center load balancing:    
copy `neo4j.conf` file into directory `~/neo4j/core1/conf`, `~/neo4j/core2/conf`, `~/neo4j/core3/conf`
and then restart server.
5. Run `pip install neo4j`in command line to install neo4j driver. 
6. Run `neo4j_driver.py` to test database connection.

## Data Source
1. Uncomment lines in `prune_data.py`, and change the filepath of original data to your own filepath in the code.        
This python file will produce pruned data for our project.
2. 