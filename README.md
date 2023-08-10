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

Further configuration options are listed on calling

```sh
% ./src/mongo2neo4j.py -h
```

NOTE: *if the [APOC plugin](https://neo4j.com/docs/apoc/) is installed in the Neo4j DB, the faster and memory-effective `apoc.periodic.iterate` method is used to generate nodes and sublabels.


### Required Argument

<dl>
  <dt>`mongo_db`</dt>
  <dd>MongoDB DB to be imported</dd>
</dl>


### Optional Arguments

MongoDB connection
<dl>
  <dt>`-mh MONGO_HOST, --mongo_host MONGO_HOST`</dt>
  <dd>MongoDB simple hostname or a full MongoDB URI of the form mongodb://<user>:<password>@<host>:<port>. Unix domain sockets with percent encoded socket path in the URI. Default: `localhost`</dd>
  <dt>`-mp MONGO_PORT, --mongo_port MONGO_PORT`. Default: `27017`</dt>
  <dd>MongoDB port</dd>
</dl>

Neo4j connection
<dl>
  <dt>`-nh NEO4J_HOST, --neo4j_host NEO4J_HOST`</dt>
  <dd>Neo4j hostname. Default: `localhost`</dd>
  <dt>`-np NEO4J_PORT, --neo4j_port NEO4J_PORT`</dt>
  <dd>Neo4j port. Default: `7687`</dd>
  <dt>`-nu NEO4J_USER, --neo4j_user NEO4J_USER`</dt>
  <dd>Neo4j user. Default: `neo4j`</dd>
  <dt>`-npw NEO4J_PASSWORD, --neo4j_password NEO4J_PASSWORD`</dt>
  <dd>Neo4j password</dd>
  <dt>`-nd NEO4J_DB, --neo4j_db NEO4J_DB`</dt>
  <dd>Neo4j DB to import into. Default: <default Neo4j DB></dd>
</dl>

Mapping
<dl>
  <dt>`-i INCLUDED_COLLECTIONS, --include INCLUDED_COLLECTIONS`</dt>
  <dd>Collection to be transferred. If not specified, transfer all not excluded ones</dd>
</dl>
<dl>
  <dt>`-x EXCLUDED_COLLECTIONS, --exclude EXCLUDED_COLLECTIONS`</dt>
  <dd>Collection to be excluded</dd>
</dl>
<dl>
  <dt>`-f EXCLUDED_FIELDS, --exclude_fields EXCLUDED_FIELDS`</dt>
  <dd>MongoDB document fields to be ignored</dd>
</dl>
<dl>
  <dt>`-sl SUBLABELS, --sublabels SUBLABELS`</dt>
  <dd>List of <Collection>.<attrib> of type string or list of strs to create sublabels</dd>
</dl>
<dl>
  <dt>`-r RELATIONS, --relations RELATIONS`</dt>
  <dd>List of <Collection>.<attrib>,<Collection>.<attrib> tuples to relations between nodes of equal str/number values</dd>
</dl>
<dl>
  <dt>`-lr LIST_RELATIONS, --list_relations LIST_RELATIONS`</dt>
  <dd>List of <Collection>.<attrib>,<Collection>.<attrib> tuples to relations between nodes of list of str/number values and str/number values</dd>
</dl>


Options
<dl>
  <dt>`-h, --help`</dt>
  <dd>show a help message and exit</dd>
</dl>
<dl>
  <dt>`--conf_export`</dt>
  <dd>Dump config and exit</dd>
</dl>
<dl>
  <dt>`--conf CONF`</dt>
  <dd>Read JSON config file. Default: `mongo2neo4j.conf`</dd>
</dl>
<dl>
  <dt>`-v, --verbose`</dt>
  <dd>Output Cypher</dd>
</dl>
<dl>
  <dt>`-s, --simulate`</dt>
  <dd>Don't connect to Neo4j</dd>
</dl>
<dl>
  <dt>`-c, --create`</dt>
  <dd>Use CREATE instead of MERGE to create objects in Neo4j</dd>
</dl>
<dl>
  <dt>`-k CHUNK_SIZE, --chunk_size CHUNK_SIZE`</dt>
  <dd>Processing objects chunk size. Default: `500`</dd>
</dl>
