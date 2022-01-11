"""Add terms_version to payments table

Revision ID: 1b9af0580e8a
Revises: 362909e71290
Create Date: 2021-01-29 21:06:56.652137

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1b9af0580e8a'
down_revision = '362909e71290'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('payments', sa.Column('terms_version', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('payments', 'terms_version')
    # ### end Alembic commands ###
