# mongo2neo4j

MongoDB Mongoose to Neo4j Importer

## Installation

### Install Neo4j

see [Neo4j](https://neo4j.com/)

### Install SemSpect

see [SemSpect](https://www.semspect.de/)

### Install Python

see [Python](https://python.org/)

### Install Python libs

```sh
% pip install -r requirements.txt
```

### Run the importer

You can run the `mongo2neo4j`importer from the shell by providing at least the name of the MongoDB the data should be imported from. If not specified the default `neo4j` DB is targeted with the default `neo4j` user. It is likely that you will have to add passwords.

```sh
% ./src/mongo2neo4j.py \  
  [--mongo_host mongodb://<mongo_user>:<mongo_password>@<mongo_host] \
  [--neo4j_user=<neo4j_user>] [--neo4j_password=<neo4j_password>] \  
  <mongo_db>
```

```sh
  
```

Further configuration options are listed on calling

```sh
% ./src/mongo2neo4j.py -h
```

NOTE: *if the [APOC plugin](https://neo4j.com/docs/apoc/) is installed in the Neo4j DB, the `apoc.periodic.iterate` method is used to add sublabels.*
