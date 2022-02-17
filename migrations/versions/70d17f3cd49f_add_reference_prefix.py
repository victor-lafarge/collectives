"""add_reference_prefix

Revision ID: 70d17f3cd49f
Revises: 8bea958748e8
Create Date: 2022-02-16 16:30:12.525345

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "70d17f3cd49f"
down_revision = "8bea958748e8"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "equipment_types",
        sa.Column("reference_prefix", sa.String(length=10), nullable=False),
    )
    op.create_unique_constraint(None, "equipment_types", ["reference_prefix"])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "equipment_types", type_="unique")
    op.drop_column("equipment_types", "reference_prefix")
    # ### end Alembic commands ###
