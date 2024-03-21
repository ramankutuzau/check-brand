"""empty message

Revision ID: 1b09f7263881
Revises: ecef2d100474
Create Date: 2023-10-24 11:26:46.916645

"""
from alembic import op
from sqlalchemy import text

# revision identifiers, used by Alembic.
revision = '1b09f7263881'
down_revision = 'ecef2d100474'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ##
    op.execute(text("""
    CREATE TABLE "content"."login_history_2023_10"
    PARTITION OF "content"."login_history" FOR VALUES FROM ('2023-10-01') TO ('2024-02-01');
    """))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute(text("""
        DROP TABLE "content"."login_history_2023_10";
        """))

    # ### end Alembic commands ###
