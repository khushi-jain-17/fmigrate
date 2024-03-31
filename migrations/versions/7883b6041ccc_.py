"""empty message

Revision ID: 7883b6041ccc
Revises: 0c5448035bf9
Create Date: 2024-03-31 15:20:03.252486

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7883b6041ccc'
down_revision = '0c5448035bf9'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('total', sa.Integer(), nullable=True),
    sa.Column('oname', sa.String(length=70), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    


def downgrade():
    op.drop_table('order')
