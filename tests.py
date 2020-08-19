import unittest, json
from nest import nest
from copy import deepcopy
from app import app


class TestNesting(unittest.TestCase):

    def setUp(self) -> None:
        with open('fixtures/input.json') as input_data:
            self.input_dicts = json.load(input_data)
        with open('fixtures/output.json') as output_data:
            self.output_dict = json.load(output_data)
        self.app = app.test_client()

    def test_correct_nest(self):
        self.assertEqual(nest(self.input_dicts, ['currency', 'country', 'city']), self.output_dict)

    def test_wrong_nest(self):
        self.assertNotEqual(nest(self.input_dicts, ['currency', 'country']), self.output_dict)

    def test_does_not_mutate_input_data(self):
        copy_input_dicts = deepcopy(self.input_dicts)
        nest(self.input_dicts, ['currency', 'country', 'city'])
        self.assertEqual(copy_input_dicts, self.input_dicts)

    def test_api_requires_authentication(self):
        response = self.app.post('/api/nest',
                                 json=self.input_dicts, content_type='application/json',
                                 query_string=dict(currency='', country='', city=''),
                                 follow_redirects=True
                                 )
        self.assertEqual(response.status_code, 401)

    def test_correct_response(self):
        response = self.app.post('/api/nest',
                                 json=self.input_dicts, content_type='application/json',
                                 query_string=dict(currency='', country='', city=''),
                                 follow_redirects=True, headers={'authorization': 'Basic dGVzdHVzZXI6YmFkcGFzc3dvcmQ='}
                                 )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.output_dict, response.get_json())


if __name__ == '__main__':
    unittest.main()
