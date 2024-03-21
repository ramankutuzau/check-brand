"""create inital tables

Revision ID: b165b637258c
Revises: 42917e680c69
Create Date: 2022-09-24 21:20:57.272291

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'b165b637258c'
down_revision = '42917e680c69'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('application', sa.Column('created_at', sa.DateTime(), nullable=True), schema='content')
    op.add_column('application', sa.Column('updated_at', sa.DateTime(), nullable=True), schema='content')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('application', 'updated_at', schema='content')
    op.drop_column('application', 'created_at', schema='content')
    # ### end Alembic commands ###
