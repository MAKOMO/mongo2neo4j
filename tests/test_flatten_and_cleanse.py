from bson.objectid import ObjectId
import mongo2neo4j


class TestFlattenAndCleanseSubObjects:

    mid = '_id'

    def test_simple_values(self):
        """the sub object is flattend"""
        super_dict = {
            self.mid: ObjectId('6477dcd14ff2e36571d60890'),
            'sub': {
                'a': 1,
                'b': 2
            }
        }
        res, relations, array_fields, objects = mongo2neo4j.flatten_and_cleanse('super', super_dict, [], [], [])
        assert res == { self.mid: '6477dcd14ff2e36571d60890', 'sub_a': 1, 'sub_b': 2}
        assert not relations
        assert array_fields == set()
        assert not objects

    def test_simple_values_with_id(self):
        """the sub object is generated and linked"""
        super_dict = {
            self.mid: ObjectId('6477dcd14ff2e36571d60890'),
            'k': 0,
            'sub': {
                self.mid: ObjectId('6477dcd14ff2e36571d60891'),
                'a': 1,
                'b': 2
            }
        }
        res, relations, array_fields, objects = mongo2neo4j.flatten_and_cleanse('super', super_dict, [], [], [])
        assert res == { self.mid: '6477dcd14ff2e36571d60890', 'k': 0}
        assert relations == { 'sub': {('6477dcd14ff2e36571d60890', '6477dcd14ff2e36571d60891')}}
        assert array_fields == set()
        assert objects == {'super_sub': [{self.mid: '6477dcd14ff2e36571d60891', 'a': 1, 'b': 2}]}

    def test_sequence_numbers(self):
        """the sub object is flattend"""
        super_dict = {
            self.mid: ObjectId('6477dcd14ff2e36571d60890'),
            'k': 0,
            'sub': {
                'l': [0, 1, 2],
                'm': 1
            }
        }
        res, relations, array_fields, objects = mongo2neo4j.flatten_and_cleanse('super', super_dict, [], [], [])
        assert res == {self.mid: '6477dcd14ff2e36571d60890', 'k': 0, 'sub_l': [0, 1, 2], 'sub_m': 1}
        assert not relations
        assert array_fields == set()
        assert not objects

    def test_sequence_strings(self):
        """the sub object is flattend and sub_l is marked as array field to allow for generation of sublabels"""
        super_dict = {
            self.mid: ObjectId('6477dcd14ff2e36571d60890'),
            'k': 0,
            'sub': {
                'l': ['a', 'b', 'c'],
                'm': 1
            }
        }
        res, relations, array_fields, objects = mongo2neo4j.flatten_and_cleanse('super', super_dict, [], [], [])
        assert res == {self.mid: '6477dcd14ff2e36571d60890', 'k': 0, 'sub_l': ['a', 'b', 'c'], 'sub_m': 1}
        assert not relations
        assert array_fields == {'sub_l'}
        assert not objects

    def test_sequence_ids(self):
        """the sub objects are generated and linked"""
        super_dict = {
            self.mid: ObjectId('6477dcd14ff2e36571d60890'),
            'k': 0,
            'sub': {
                'l': [ObjectId('6477dcd14ff2e36571d60892'), ObjectId('6477dcd14ff2e36571d60894')],
                'm': 1
            }
        }
        res, relations, array_fields, objects = mongo2neo4j.flatten_and_cleanse('super', super_dict, [], [], [])
        assert res == {self.mid: '6477dcd14ff2e36571d60890', 'k': 0, 'sub_m': 1}
        assert relations == {'sub_l': {('6477dcd14ff2e36571d60890', '6477dcd14ff2e36571d60892'), ('6477dcd14ff2e36571d60890', '6477dcd14ff2e36571d60894')}}
        assert array_fields == set()
        assert not objects

    def test_sequence_objects(self):
        """sub sub objects are generated with fresh ids and linked"""
        super_dict = {
            self.mid: ObjectId('6477dcd14ff2e36571d60890'),
            'k': 0,
            'sub': {
                'l': [
                    { 'x': 0 },
                    { 'x': 1 }
                ],
                'm': 1
            }
        }
        res, relations, array_fields, objects = mongo2neo4j.flatten_and_cleanse('super', super_dict, [], [], [])
        assert res == {self.mid: '6477dcd14ff2e36571d60890', 'k': 0, 'sub_m': 1}
        # relations: {'sub_l': [('6477dcd14ff2e36571d60890', '0303b7e9b84f41e9bdb09db2e187a8d8'), ('6477dcd14ff2e36571d60890', '8e8cbc0d44d349c88f1f2df20f8458aa')]}
        assert ('sub_l' in relations) is True
        links = relations['sub_l']
        assert len(links) == 2
        assert {l[0] for l in links} == {'6477dcd14ff2e36571d60890'}
        assert array_fields == set()
        # objects: {'super_sub_l': [{'x': 0, '_id': '0303b7e9b84f41e9bdb09db2e187a8d8'}, {'x': 1, '_id': '8e8cbc0d44d349c88f1f2df20f8458aa'}]}
        assert 'super_sub_l' in objects
        sub_objects = objects['super_sub_l']
        assert len(sub_objects) == 2
        assert sub_objects[0]['x'] == 0
        assert sub_objects[1]['x'] == 1
        linked_objects = [l[1] for l in links]
        assert sub_objects[0][self.mid] in linked_objects
        assert sub_objects[1][self.mid] in linked_objects

    def test_sequence_id_objects(self):
        """sub sub objects are generated using the given ids and linked"""
        super_dict = {
            self.mid: ObjectId('6477dcd14ff2e36571d60890'),
            'k': 0,
            'sub': {
                'l': [
                    { self.mid: ObjectId('6477dcd14ff2e36571d60892'), 'x': 0 },
                    { self.mid: ObjectId('6477dcd14ff2e36571d60894'), 'x': 1 }
                ],
                'm': 1
            }
        }
        res, relations, array_fields, objects = mongo2neo4j.flatten_and_cleanse('super', super_dict, [], [], [])
        assert res == {self.mid: '6477dcd14ff2e36571d60890', 'k': 0, 'sub_m': 1}
        # relations: {'sub_l': [('6477dcd14ff2e36571d60890', '6477dcd14ff2e36571d60892'), ('6477dcd14ff2e36571d60890', '6477dcd14ff2e36571d60894')]}
        links = relations['sub_l']
        assert len(links) == 2
        assert {l[0] for l in links} == {'6477dcd14ff2e36571d60890'}
        assert array_fields == set()
        # {'super_sub_l': [{'_id': '6477dcd14ff2e36571d60892', 'x': 0}, {'_id': '6477dcd14ff2e36571d60894', 'x': 1}]}
        assert 'super_sub_l' in objects
        sub_objects = objects['super_sub_l']
        assert len(sub_objects) == 2
        assert sub_objects[0]['x'] == 0
        assert sub_objects[1]['x'] == 1
        linked_objects = [l[1] for l in links]
        assert sub_objects[0][self.mid] in linked_objects
        assert sub_objects[1][self.mid] in linked_objects



class TestFlattenAndCleanseSubSequences:

    mid = '_id'

    def test_simple_values(self):
        """the sub object is flattend"""
        super_dict = {
            self.mid: ObjectId('6477dcd14ff2e36571d60890'),
            'l': [0, 1, 2]
        }
        res, relations, array_fields, objects = mongo2neo4j.flatten_and_cleanse('super', super_dict, [], [], [])
        assert res == { self.mid: '6477dcd14ff2e36571d60890', 'l': [0, 1, 2]}
        assert not relations
        assert array_fields == set()
        assert not objects

    def test_ids(self):
        """the sub object is flattend"""
        super_dict = {
            self.mid: ObjectId('6477dcd14ff2e36571d60890'),
            'l': [ObjectId('6477dcd14ff2e36571d60892'), ObjectId('6477dcd14ff2e36571d60894')]
        }
        res, relations, array_fields, objects = mongo2neo4j.flatten_and_cleanse('super', super_dict, [], [], [])
        assert res == { self.mid: '6477dcd14ff2e36571d60890' }
        assert relations == {'l': {('6477dcd14ff2e36571d60890', '6477dcd14ff2e36571d60892'), ('6477dcd14ff2e36571d60890', '6477dcd14ff2e36571d60894')}}
        assert array_fields == set()
        assert not objects

    def test_objects(self):
        """the sub object is flattend"""
        super_dict = {
            self.mid: ObjectId('6477dcd14ff2e36571d60890'),
            'l': [ {'x': 0 }, {'x': 1}]
        }
        res, relations, array_fields, objects = mongo2neo4j.flatten_and_cleanse('super', super_dict, [], [], [])
        assert res == { self.mid: '6477dcd14ff2e36571d60890' }
        # relations: {'l': [('6477dcd14ff2e36571d60890', '0bbed9a55ca1409088521b7927b615e9'), ('6477dcd14ff2e36571d60890', '3eebc1d7b1c14485a85e53ef05734749')]}
        assert ('l' in relations) is True
        links = relations['l']
        assert len(links) == 2
        assert {l[0] for l in links} == {'6477dcd14ff2e36571d60890'}
        assert array_fields == set()
        # objects: {'super_l': [{self.mid: '0bbed9a55ca1409088521b7927b615e9', 'x': 0}, {self.mid: '3eebc1d7b1c14485a85e53ef05734749', 'x': 1}]}
        assert 'super_l' in objects
        sub_objects = objects['super_l']
        assert len(sub_objects) == 2
        assert sub_objects[0]['x'] == 0
        assert sub_objects[1]['x'] == 1
        linked_objects = [l[1] for l in links]
        assert sub_objects[0][self.mid] in linked_objects
        assert sub_objects[1][self.mid] in linked_objects

    def test_objects_with_ids(self):
        """the sub object is flattend"""
        super_dict = {
            self.mid: ObjectId('6477dcd14ff2e36571d60890'),
            'l': [ {self.mid: ObjectId('6477dcd14ff2e36571d60892'), 'x': 0 }, {self.mid: ObjectId('6477dcd14ff2e36571d60894'), 'x': 1}]
        }
        res, relations, array_fields, objects = mongo2neo4j.flatten_and_cleanse('super', super_dict, [], [], [])
        assert res == { self.mid: '6477dcd14ff2e36571d60890' }
        # relations: {'l': [('6477dcd14ff2e36571d60890', '6477dcd14ff2e36571d60892'), ('6477dcd14ff2e36571d60890', '6477dcd14ff2e36571d60894')]}
        assert ('l' in relations) is True
        links = relations['l']
        assert len(links) == 2
        assert {l[0] for l in links} == {'6477dcd14ff2e36571d60890'}
        assert array_fields == set()
        # objects: {'super_l': [{'_id': '6477dcd14ff2e36571d60892', 'x': 0}, {'_id': '6477dcd14ff2e36571d60894', 'x': 1}]}
        assert objects == {'super_l': [{'_id': '6477dcd14ff2e36571d60892', 'x': 0}, {'_id': '6477dcd14ff2e36571d60894', 'x': 1}]}
