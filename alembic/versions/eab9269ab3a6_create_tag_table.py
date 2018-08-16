"""create tag table

Revision ID: eab9269ab3a6
Revises: 
Create Date: 2018-08-14 14:19:46.188590

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy.dialects.postgresql as pg


# revision identifiers, used by Alembic.
revision = 'eab9269ab3a6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
            'tag',
            sa.Column('tag_id', sa.Text, primary_key=True),
            sa.Column('vendor_id', sa.Text, nullable=False),
            sa.Column('tag_metadata', pg.JSONB, nullable=False),
        )


def downgrade():
    op.drop_table('tag')
