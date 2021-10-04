"""Add statistics

Revision ID: fd21f2ac4136
Revises: 564b1ed538b2
Create Date: 2020-08-29 11:46:45.865919

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "fd21f2ac4136"
down_revision = "564b1ed538b2"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "request",
        sa.Column("index", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("response_time", sa.Float(), nullable=True),
        sa.Column("date", sa.DateTime(), nullable=True),
        sa.Column("method", sa.Text(), nullable=True),
        sa.Column("size", sa.Integer(), nullable=True),
        sa.Column("status_code", sa.Integer(), nullable=True),
        sa.Column("path", sa.String(length=128), nullable=True),
        sa.Column("user_agent", sa.Text(), nullable=True),
        sa.Column("remote_address", sa.Text(), nullable=True),
        sa.Column("exception", sa.Text(), nullable=True),
        sa.Column("referrer", sa.Text(), nullable=True),
        sa.Column("browser", sa.Text(), nullable=True),
        sa.Column("platform", sa.Text(), nullable=True),
        sa.Column("mimetype", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("index"),
    )
    op.create_index(op.f("ix_request_date"), "request", ["date"], unique=False)
    op.create_index(op.f("ix_request_path"), "request", ["path"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_request_path"), table_name="request")
    op.drop_index(op.f("ix_request_date"), table_name="request")
    op.drop_table("request")
    # ### end Alembic commands ###
