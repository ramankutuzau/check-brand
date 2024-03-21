"""updated

Revision ID: 7cdf0b10e532
Revises: 3dde5ed298a1
Create Date: 2022-11-27 18:32:16.444426

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7cdf0b10e532'
down_revision = '3dde5ed298a1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('application', sa.Column('field_1', sa.String(), nullable=True), schema='content')
    op.add_column('application', sa.Column('field_2', sa.String(), nullable=True), schema='content')
    op.add_column('application', sa.Column('field_3', sa.String(), nullable=True), schema='content')
    op.add_column('application', sa.Column('field_4', sa.String(), nullable=True), schema='content')
    op.add_column('application', sa.Column('field_5', sa.String(), nullable=True), schema='content')
    op.add_column('application', sa.Column('field_6', sa.String(), nullable=True), schema='content')
    op.add_column('application', sa.Column('field_7', sa.String(), nullable=True), schema='content')
    op.add_column('application', sa.Column('field_8', sa.String(), nullable=True), schema='content')
    op.add_column('application', sa.Column('field_9', sa.String(), nullable=True), schema='content')
    op.add_column('application', sa.Column('field_10', sa.String(), nullable=True), schema='content')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('application', 'field_10', schema='content')
    op.drop_column('application', 'field_9', schema='content')
    op.drop_column('application', 'field_8', schema='content')
    op.drop_column('application', 'field_7', schema='content')
    op.drop_column('application', 'field_6', schema='content')
    op.drop_column('application', 'field_5', schema='content')
    op.drop_column('application', 'field_4', schema='content')
    op.drop_column('application', 'field_3', schema='content')
    op.drop_column('application', 'field_2', schema='content')
    op.drop_column('application', 'field_1', schema='content')
    # ### end Alembic commands ###
