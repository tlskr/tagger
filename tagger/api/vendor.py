import json

from bottle import request, response
from bottle import post, get, put, delete

from tagger.db.models.tag import Tag
from tagger.db.session import get_session


@get('/vendors')
def listing_handler():
    ''' Handles listing of vendors'''

    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'

    vendors = Tag.list_vendors()

    return json.dumps({'vendors': vendors})
