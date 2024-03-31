"""empty message

Revision ID: dbd5dbf7e656
Revises: c6534d3ca735
Create Date: 2024-03-31 14:08:38.188570

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dbd5dbf7e656'
down_revision = 'c6534d3ca735'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
    "blog",
    sa.Column("content", sa.String(), nullable=True),
)
    


def downgrade():
    op.drop_column("blog","content")
