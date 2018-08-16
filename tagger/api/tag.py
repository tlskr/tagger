import json

from bottle import HTTPError, request, response
from bottle import post, get, put, delete, error
import jsonschema

from tagger.db.models.tag import Tag


@error(413)
def error413(error):
    response.status = 413
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    return json.dumps({
        'error': 'request too large',
        'message': 'please break up data into smaller request',
        })

@get('/tags')
def tag_listing_handler():
    ''' Handles tag listing '''

    # TODO: move boilerplate response stuff to function / decorator
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'

    tags = Tag.list_tags()      # TODO: compress these
    return json.dumps({'tags': tags})

@get('/tags/<tag_id>')
def get_tag_data(tag_id):
    ''' get tag by tag_id '''

    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'

    data = Tag.get_tag_data(tag_id)
    return json.dumps(data)

@post('/tags')
def load_tags():

    try:
        data = request.json

    except:
        raise ValueError

    if data is None:
        raise ValueError

    with open('docs/assignment/schema.json', 'r') as schemafile:
        schema = json.load(schemafile)

        try:
            jsonschema.validate(data, schema)
        except jsonschema.ValidationError as e:
            response.status = 400
            response.headers['Content-Type'] = 'application/json'
            response.headers['Cache-Control'] = 'no-cache'
            return json.dumps({
                'error': 'schema validation error',
                'message': str(e),
                })
                              
    Tag.load_tags(data)

    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'

    return json.dumps({'status': 'ok'})

