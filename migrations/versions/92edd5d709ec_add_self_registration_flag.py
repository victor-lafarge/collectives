"""Add flag for self registration and processor url for payments

Revision ID: 92edd5d709ec
Revises: 7df65b8fc5b0
Create Date: 2021-05-05 22:42:56.280598

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '92edd5d709ec'
down_revision = '7df65b8fc5b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("registrations") as batch_op:
        batch_op.add_column( sa.Column('is_self', sa.Boolean(), nullable=False, server_default="1"))
    op.add_column('payments', sa.Column('processor_url', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('registrations', 'is_self')
    op.drop_column('payments', 'processor_url')
    # ### end Alembic commands ###
