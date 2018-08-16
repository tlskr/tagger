from webtest import TestApp
from tagger_app import app

# NB: depends on data load to local database -- 
#   database layer really should be mocked

def test_get_tag():
    test_app = TestApp(app)
    response = test_app.get('/tags/48011705d5074addaecaaff237627564')
    assert (response.json == {
                'tag_id': '48011705d5074addaecaaff237627564',
                'tag_metadata': {
                    'size': 'S', 'type': 'jersey', 'color': 'black'
                    },
                'vendor_id': 'ac15e22e62304a8c966bf5aab9d6f368'
                })
