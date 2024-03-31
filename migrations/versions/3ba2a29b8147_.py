"""empty message

Revision ID: 3ba2a29b8147
Revises: dbd5dbf7e656
Create Date: 2024-03-31 14:21:21.314563

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ba2a29b8147'
down_revision = 'dbd5dbf7e656'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column("member","memb_name",new_column_name="mname")


def downgrade():
    op.alter_column("member","mname",new_column_name="name")
