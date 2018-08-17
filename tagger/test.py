from webtest import TestApp

from mock import patch

from tagger_app import app
from tagger.db.models.tag import Tag


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


mock_data = {
    'tag_id': '48011705d5074addaecaaff237627564',
    'tag_metadata': {
        'size': 'S', 'type': 'jersey', 'color': 'black'
        },
    'vendor_id': 'ac15e22e62304a8c966bf5aab9d6f368'
    }


def test_get_tag_mocked():

    test_app = TestApp(app)
    with patch('tagger.api.tag.Tag.get_tag_data', new=lambda tag_id: mock_data):
        response = test_app.get('/tags/48011705d5074addaecaaff237627564')
        assert (response.json == {
                'tag_id': '48011705d5074addaecaaff237627564',
                'tag_metadata': {
                    'size': 'S', 'type': 'jersey', 'color': 'black'
                    },
                'vendor_id': 'ac15e22e62304a8c966bf5aab9d6f368'
                })
