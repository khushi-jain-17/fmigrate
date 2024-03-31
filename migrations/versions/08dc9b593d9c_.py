"""empty message

Revision ID: 08dc9b593d9c
Revises: 3ba2a29b8147
Create Date: 2024-03-31 14:52:40.854182

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08dc9b593d9c'
down_revision = '3ba2a29b8147'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column("member","subscription")

def downgrade():
    op.add_column("member",sa.Column("subscription",sa.Boolean()))
