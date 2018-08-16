import json

from tagger.db.models.tag import Tag

from tagger.db.session import get_session



def insert_tags(datafile):

    Session = get_session()
    session = Session()

    with open(datafile, 'r') as dfile:
        data = json.load(dfile)
        vendor_id = data['vendor_id']

        for tag in data['tags']:
            # more pythonic?
            nt = dict([(item['key'], item.get('value')) for item in tag.get('metadata', []) if 'key' in item])

            new_tag = {}
            for item in tag.get('metadata', []):
                if 'key' not in item:       # nb: some example items are malformed
                    continue
                new_tag[item['key']] = item.get('value')

            this_tag = Tag(
                    tag_id=tag['tag_id'],
                    vendor_id=vendor_id,
                    tag_metadata=new_tag,
                    )
            session.add(this_tag)       # faster to use add_all()? 
            session.commit()
