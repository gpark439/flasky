"""empty message

Revision ID: 747d92fad858
Revises: 45b184e1c916
Create Date: 2022-05-11 10:07:34.162340

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '747d92fad858'
down_revision = '45b184e1c916'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('car', sa.Column('driver_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'car', 'driver', ['driver_id'], ['id'])
    op.drop_column('car', 'team')
    op.drop_column('car', 'driver')
    op.add_column('driver', sa.Column('name', sa.String(), nullable=True))
    op.add_column('driver', sa.Column('team', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('driver', 'team')
    op.drop_column('driver', 'name')
    op.add_column('car', sa.Column('driver', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('car', sa.Column('team', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'car', type_='foreignkey')
    op.drop_column('car', 'driver_id')
    # ### end Alembic commands ###
