"""added password field

Revision ID: 135a6638a374
Revises: 21febe88833a
Create Date: 2022-11-10 18:05:43.003876

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '135a6638a374'
down_revision = '21febe88833a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=200), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###