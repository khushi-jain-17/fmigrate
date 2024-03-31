"""empty message

Revision ID: c6534d3ca735
Revises: df197834a5ef
Create Date: 2024-03-31 13:55:46.108514

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6534d3ca735'
down_revision = 'df197834a5ef'
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table('orderss','order')


def downgrade():
    op.rename_table('order','orders')
    
