"""empty message

Revision ID: e012859db35e
Revises: ba0798d14d79
Create Date: 2023-11-25 17:19:47.974494

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e012859db35e'
down_revision = 'ba0798d14d79'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('profiles', schema='content') as batch_op:
        batch_op.add_column(sa.Column('email_otp', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('email_otp_exp', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('profiles', schema='content') as batch_op:
        batch_op.drop_column('email_otp_exp')
        batch_op.drop_column('email_otp')
    # ### end Alembic commands ###
