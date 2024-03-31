"""empty message

Revision ID: 864fe3e55e24
Revises: 1c768619ce1a
Create Date: 2024-03-31 19:47:52.906882

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '864fe3e55e24'
down_revision = '1c768619ce1a'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table("order") as batch_op:
        batch_op.create_foreign_key(
            "fk_order_blog_id",
            "blog",
            ["blog_id"],
            ["bid"],
        )

def downgrade():
    with op.batch_alter_table("order") as batch_op:
        batch_op.drop_constraint("fk_order_blog_id", type_="foreignkey")

