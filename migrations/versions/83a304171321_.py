"""empty message

Revision ID: 83a304171321
Revises: 7883b6041ccc
Create Date: 2024-03-31 16:30:00.393701

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83a304171321'
down_revision = '7883b6041ccc'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("member",sa.Column("subscription",sa.Boolean()))



def downgrade():
    op.drop_column("member","subscription")

    
