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

```
# pip install -r requirements.txt
```

### Run the importer

You can run the `mongo2neo4j`importer from the shell by providing at least the password of the Neo4j DB to be exported to (if not specified the default `neo4j` DB is addressed) and the name of the MongoDB the data should be imported from.

```
# ./mongo2neo4j.py -neo4j_password=**** MyMongoDB
```

Further configuration options are listed on calling

```
# ./mongo2neo4j.py -h
```

NOTE: *if the [APOC plugin](https://neo4j.com/docs/apoc/) is installed in the Neo4j DB, the `apoc.periodic.iterate` method is used to add sublabels.*
