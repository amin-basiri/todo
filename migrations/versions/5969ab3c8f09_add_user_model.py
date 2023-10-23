"""Add User Model

Revision ID: 5969ab3c8f09
Revises: 
Create Date: 2023-10-23 14:29:16.155353

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5969ab3c8f09'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auth_User',
    sa.Column('full_name', sa.String(length=100), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated', sa.TIMESTAMP(), nullable=True),
    sa.Column('deleted', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('auth_User')
    # ### end Alembic commands ###