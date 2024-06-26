"""Initial migration

Revision ID: 154a4f640eb9
Revises: 
Create Date: 2024-04-18 20:30:52.830986

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '154a4f640eb9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('my_task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created', sa.DateTime(), nullable=True))
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('my_task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DATETIME(), nullable=True))
        batch_op.drop_column('created')

    # ### end Alembic commands ###
