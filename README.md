# [mongo2neo4j](https://makomo.github.io/mongo2neo4j/)

[MongoDB](https://www.mongodb.com/) [Mongoose](https://mongoosejs.com/) to [Neo4j](https://neo4j.com/) Importer

![License](https://img.shields.io/github/license/MAKOMO/mongo2neo4j.svg)
[![Pylint](https://github.com/MAKOMO/mongo2neo4j/actions/workflows/pylint.yaml/badge.svg)](https://github.com/MAKOMO/mongo2neo4j/actions/workflows/pylint.yaml)
[![Ruff](https://github.com/MAKOMO/mongo2neo4j/actions/workflows/ruff.yaml/badge.svg)](https://github.com/MAKOMO/mongo2neo4j/actions/workflows/ruff.yaml)
[![Mypy](https://github.com/MAKOMO/mongo2neo4j/actions/workflows/mypy.yml/badge.svg)](https://github.com/MAKOMO/mongo2neo4j/actions/workflows/mypy.yml)
[![pytest](https://github.com/artisan-roaster-scope/artisan/actions/workflows/pytest.yaml/badge.svg?branch=master)](https://github.com/artisan-roaster-scope/artisan/actions/workflows/pytest.yaml)
![coverage](./images/coverage.svg)


## What is mongo2neo4j?

Imports object relations generated by Object Relation Mappers (ORMs) like [Mongoose](https://mongoosejs.com/) and stored in [MongoDB](https://www.mongodb.com/) into the graph database management system [Neo4j](https://neo4j.com/) for exploration with the no-code graphical querying tool [SemSpect](https://www.semspect.de/). Further relations between objects can be specified via options.

![](https://github.com/MAKOMO/mongo2neo4j/blob/main/images/motivation.jpg?raw=true)

## What for?

Imagine you just released your latest [MEAN-stack](https://en.wikipedia.org/wiki/MEAN_(solution_stack)) app and want to learn how it is used. You could write some [MongoDB](https://www.mongodb.com/) queries to find out _"how many users of the free tier are at all producing some data?", "which feature is used most by subscribers?",_ ... But maybe you never find time to write those queries or you do not know exact what to look for. A graphical large-data exploration tool like [SemSpect](https://www.semspect.de/) comes in handy, which allows you to discover patterns in your data by simple navigation.

![](https://github.com/MAKOMO/mongo2neo4j/blob/main/images/semspect.jpg?raw=true)

As [SemSpect](https://www.semspect.de/) is layered on top of the graph database system [Neo4j](https://neo4j.com/) as graph app, your [MongoDB](https://www.mongodb.com/) data needs first to be established in [Neo4j](https://neo4j.com/). This can be easily achieved using the `mongo2neo4j` tool.


## How does it work?

The `mongodb2neo4j` script creates a label (class of nodes) in [Neo4j](https://neo4j.com/) for each collection in the given [MongoDB](https://www.mongodb.com/) and adds nodes in [Neo4j](https://neo4j.com/) for all documents. Cross-references between [MongoDB](https://www.mongodb.com/) documents using unique `ObjectId` identifiers are turned into [Neo4j](https://neo4j.com/) relations, nicely rendered by [SemSpect](https://www.semspect.de/).

![](https://github.com/MAKOMO/mongo2neo4j/blob/main/images/mongodb.jpg?raw=true)


## Installation

### Install Neo4j

The free Neo4j Desktop works well (see [Neo4j](https://neo4j.com/))

### Install SemSpect Plugin

The free SemSpect Graph App for Neo4j works well (see [SemSpect](https://www.semspect.de/))

### Install `mongo2neo4j`

```sh
% pip install mongo2neo4j
```

## Run the importer

You can run the `mongo2neo4j`importer from the shell by providing at least the name of the [MongoDB](https://www.mongodb.com/) DB the data should be imported from. If not specified the default `neo4j` DB is targeted with the default `neo4j` user. It is likely that you will have to add passwords.

```sh
% mongo2neo4j \
  [--mongo_host mongodb://<mongo_user>:<mongo_password>@<mongo_host>] \
  [--neo4j_user=<neo4j_user>] [--neo4j_password=<neo4j_password>] \
  <mongo_db>
```

Further configuration options are listed on calling

```sh
% mongo2neo4j -h
```

See [Script Arguments](https://github.com/MAKOMO/mongo2neo4j/wiki/Script-Arguments) for the full list of available arguments.


NOTE: *if the [APOC plugin](https://neo4j.com/docs/apoc/) is installed in the Neo4j DB, the faster and memory-effective `apoc.periodic.iterate` method is used to generate nodes and sublabels.*
