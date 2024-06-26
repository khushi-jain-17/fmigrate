"""empty message

Revision ID: ba71d3e3a68d
Revises: 83a304171321
Create Date: 2024-03-31 16:38:42.085787

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba71d3e3a68d'
down_revision = '83a304171321'
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