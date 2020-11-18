# neo4j-project
A project based on neo4j graph database

# Step of deploying cluster neo4j database
1. Install Docker Desktop
2. Create directory ~/neo4j/core1/data; ~/neo4j/core1/conf; ~/neo4j/core1/logs;    
~/neo4j/core2/data; ~/neo4j/core2/conf; ~/neo4j/core2/logs;    
~/neo4j/core3/data; ~/neo4j/core3/conf; ~/neo4j/core3/logs;   
3. run `sh dock_neo4j_cluster.sh` in command line

## Data Source
Uncomment lines in prune_data.py, and change the filepath of orginial data to your own filepath in the code.        
This file will produce pruned data for our project.
