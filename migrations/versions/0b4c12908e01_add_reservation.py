"""add reservation

Revision ID: 0b4c12908e01
Revises: 28f945d84529
Create Date: 2022-01-12 11:41:02.956069

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b4c12908e01'
down_revision = '28f945d84529'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reservations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('collect_date', sa.DateTime(), nullable=False),
    sa.Column('return_date', sa.DateTime(), nullable=True),
    sa.Column('status', sa.Enum('Planned', 'Ongoing', 'Completed', 'Cancelled', name='reservationstatus'), nullable=False),
    sa.Column('extended', sa.Boolean(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_reservations_collect_date'), 'reservations', ['collect_date'], unique=False)
    op.create_index(op.f('ix_reservations_return_date'), 'reservations', ['return_date'], unique=False)
    op.create_table('reservation_lines',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('equipment_id', sa.Integer(), nullable=False),
    sa.Column('reservation_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['equipment_id'], ['equipments.id'], ),
    sa.ForeignKeyConstraint(['reservation_id'], ['reservations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reservation_lines')
    op.drop_index(op.f('ix_reservations_return_date'), table_name='reservations')
    op.drop_index(op.f('ix_reservations_collect_date'), table_name='reservations')
    op.drop_table('reservations')
    # ### end Alembic commands ###
