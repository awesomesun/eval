"""new fields in user model

Revision ID: 917b66846c70
Revises: e3a36d3cb412
Create Date: 2018-06-13 20:24:47.690830

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '917b66846c70'
down_revision = 'e3a36d3cb412'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
