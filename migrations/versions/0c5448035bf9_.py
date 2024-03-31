"""empty message

Revision ID: 0c5448035bf9
Revises: 08dc9b593d9c
Create Date: 2024-03-31 15:12:25.694389

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c5448035bf9'
down_revision = '08dc9b593d9c'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_table('order')


def downgrade():
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('total', sa.Integer(), nullable=True),
    sa.Column('oname', sa.String(length=70), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    
