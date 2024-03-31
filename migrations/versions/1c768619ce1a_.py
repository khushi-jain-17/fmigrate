"""empty message

Revision ID: 1c768619ce1a
Revises: ba71d3e3a68d
Create Date: 2024-03-31 17:31:25.362601

"""
from alembic import op
import sqlalchemy as sa
from alembic.operations.batch import batch_alter_table


# revision identifiers, used by Alembic.
revision = '1c768619ce1a'
down_revision = 'ba71d3e3a68d'
branch_labels = None
depends_on = None


def upgrade():
    with batch_alter_table("order") as batch_op:
      batch_op.create_foreign_key(
        "fk_order",
        "order",
        ["blog_id"],
        ["bid"],
    )
    


def downgrade():
    pass
