"""empty message

Revision ID: 3371a445800e
Revises: cdfac269c617
Create Date: 2018-10-06 16:24:09.795116

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3371a445800e'
down_revision = 'cdfac269c617'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_location', table_name='user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_user_location', 'user', ['location'], unique=1)
    # ### end Alembic commands ###
