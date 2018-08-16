# coding: utf-8
from sqlalchemy import Column, Text
from sqlalchemy.dialects.postgresql.json import JSONB

from . base import Base

from tagger.db.session import get_session


class Tag(Base):
    __tablename__ = 'tag'

    tag_id = Column(Text, primary_key=True)
    vendor_id = Column(Text, nullable=False)
    tag_metadata = Column(JSONB(astext_type=Text()), nullable=False)

    @classmethod
    def get_session(cls):
        Session = get_session()     # TODO: clean up, ugly
        return Session()

    @classmethod
    def list_vendors(cls):
        session = cls.get_session()
        x = session.query(cls.vendor_id).distinct()
        return list(x.all())

    @classmethod
    def list_tags(cls):
        session = cls.get_session()
        x = session.query(Tag.tag_id).distinct()
        return list(x.all())

    @classmethod
    def get_tag_instance(cls, tag_id):
        ''' get Tag instance by tag_id '''
        session = cls.get_session()
        data = session.query(Tag).filter(Tag.tag_id == tag_id)
        return data[0]

    @classmethod
    def get_tag_data(cls, tag_id):
        ''' return Tag tag_metadata '''
        tag = cls.get_tag_instance(tag_id)
        return tag.all_data

    @property
    def all_data(self):
        ''' return all data in instance '''

        # TODO: there must be a better way
        retval = {}
        for col in self.__table__.columns:
            retval[col.name] = getattr(self, col.name)
        return retval

    @classmethod
    def load_tags(cls, data):
        session = cls.get_session()
    
        vendor_id = data['vendor_id']
    
        for tag in data['tags']:
            new_tag = {}
            for item in tag.get('metadata', []):
                if 'key' not in item:
                    continue
                new_tag[item['key']] = item.get('value')

            this_tag = Tag(
                    tag_id=tag['tag_id'],
                    vendor_id=vendor_id,
                    tag_metadata=new_tag,
                    )
            session.add(this_tag)       # faster to use add_all()? 
            session.commit()
