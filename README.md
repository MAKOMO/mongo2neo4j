# mongo2neo4j

MongoDB Mongoose to Neo4j Importer

![License](https://img.shields.io/github/license/artisan-roaster-scope/artisan.svg)
[![pylint](https://github.com/artisan-roaster-scope/artisan/actions/workflows/pylint.yaml/badge.svg?branch=master&event=push)](https://github.com/artisan-roaster-scope/artisan/actions?query=workflow:pylint+event:push+branch:master)
[![Mypy](https://github.com/artisan-roaster-scope/artisan/actions/workflows/mypy.yml/badge.svg?branch=master)](https://github.com/artisan-roaster-scope/artisan/actions/workflows/mypy.yml)
[![Ruff](https://github.com/artisan-roaster-scope/artisan/actions/workflows/ruff.yaml/badge.svg?branch=master)](https://github.com/artisan-roaster-scope/artisan/actions/workflows/ruff.yaml)
[![pytest](https://github.com/artisan-roaster-scope/artisan/actions/workflows/pytest.yaml/badge.svg?branch=master)](https://github.com/artisan-roaster-scope/artisan/actions/workflows/pytest.yaml)

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

## Run the importer

You can run the `mongo2neo4j`importer from the shell by providing at least the name of the MongoDB the data should be imported from. If not specified the default `neo4j` DB is targeted with the default `neo4j` user. It is likely that you will have to add passwords.

```sh
% ./src/mongo2neo4j.py \
  [--mongo_host mongodb://<mongo_user>:<mongo_password>@<mongo_host>] \
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
  <dt><pre>mongo_db</pre></dt>
  <dd>MongoDB DB to be imported</dd>
</dl>


### Optional Arguments

MongoDB connection
<dl>
  <dt><pre>-mh MONGO_HOST, --mongo_host MONGO_HOST</pre></dt>
  <dd>MongoDB simple hostname or a full MongoDB URI of the form mongodb://<user>:<password>@<host>:<port>. Unix domain sockets with percent encoded socket path in the URI. Default: <tt>localhost</tt></dd>
  <dt><pre>-mp MONGO_PORT, --mongo_port MONGO_PORT</pre>. Default: <tt>27017</tt></dt>
  <dd>MongoDB port</dd>
</dl>

Neo4j connection
<dl>
  <dt><tt>-nh NEO4J_HOST, --neo4j_host NEO4J_HOST</tt></dt>
  <dd>Neo4j hostname. Default: <tt>localhost</tt></dd>
  <dt><pre>-np NEO4J_PORT, --neo4j_port NEO4J_PORT</pre></dt>
  <dd>Neo4j port. Default: <tt>7687</tt></dd>
  <dt><pre>-nu NEO4J_USER, --neo4j_user NEO4J_USER</pre></dt>
  <dd>Neo4j user. Default: <tt>neo4j</tt></dd>
  <dt><pre>-npw NEO4J_PASSWORD, --neo4j_password NEO4J_PASSWORD</pre></dt>
  <dd>Neo4j password</dd>
  <dt><pre>-nd NEO4J_DB, --neo4j_db NEO4J_DB</pre></dt>
  <dd>Neo4j DB to import into. Default: <tt>default Neo4j DB</tt></dd>
</dl>

Mapping
<dl>
  <dt><pre>-i INCLUDED_COLLECTIONS, --include INCLUDED_COLLECTIONS</pre></dt>
  <dd>Collection to be transferred. If not specified, transfer all not excluded ones</dd>
</dl>
<dl>
  <dt><pre>-x EXCLUDED_COLLECTIONS, --exclude EXCLUDED_COLLECTIONS</pre></dt>
  <dd>Collection to be excluded. Collection names can have a * at the begin or end to match multiple collections.</dd>
</dl>
<dl>
  <dt><pre>-f EXCLUDED_FIELDS, --exclude_fields EXCLUDED_FIELDS</pre></dt>
  <dd>MongoDB document fields to be ignored. Field names can have a * at the begin or end to match multiple fields.</dd>
</dl>
<dl>
  <dt><pre>-sl SUBLABELS, --sublabels SUBLABELS</pre></dt>
  <dd>List of <tt>&lt;collection&gt;.&lt;attrib&gt;</tt> of type string or list of strs to create sublabels</dd>
</dl>
<dl>
  <dt><pre>-r RELATIONS, --relations RELATIONS</pre></dt>
  <dd>List of <tt>&lt;collection&gt;.&lt;attrib&gt;[.&lt;postfix&gt;][,&lt;others&gt;]</tt> fields of type string or list of strings to create sublabels. The optional <tt>&lt;postfix&gt;</tt> is added to the generated sublabel and if <tt>&lt;others&gt;</tt> is given it is used to collect nodes without proper value.</dd>
</dl>
<dl>
  <dt><pre>-lr LIST_RELATIONS, --list_relations LIST_RELATIONS</pre></dt>
  <dd>List of <tt>&lt;collection&gt;.&lt;attrib&gt;,&lt;collection&gt;.&lt;attrib&gt;</tt> tuples to relations between nodes of list of str/number values and str/number values</dd>
</dl>


Options
<dl>
  <dt><pre>-h, --help</pre></dt>
  <dd>show a help message and exit</dd>
</dl>
<dl>
  <dt><pre>--conf_export</pre></dt>
  <dd>Dump config and exit</dd>
</dl>
<dl>
  <dt><pre>--conf CONF</pre></dt>
  <dd>Read JSON config file. Default: <tt>mongo2neo4j.conf</tt></dd>
</dl>
<dl>
  <dt><pre>-v, --verbose</pre></dt>
  <dd>Output Cypher</dd>
</dl>
<dl>
  <dt><pre>-s, --simulate</pre></dt>
  <dd>Don't connect to Neo4j</dd>
</dl>
<dl>
  <dt><pre>-c, --create</pre></dt>
  <dd>Use CREATE instead of MERGE to create objects in Neo4j</dd>
</dl>
<dl>
  <dt><pre>-k CHUNK_SIZE, --chunk_size CHUNK_SIZE</pre></dt>
  <dd>Processing objects chunk size. Default: <tt>500</tt></dd>
</dl>
