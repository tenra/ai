"""add email to user

Revision ID: 7bde559d8379
Revises:
Create Date: 2021-07-22 18:01:51.694139

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7bde559d8379'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('user', sa.Column('email', sa.String(128), unique=True, nullable=False)),
    op.add_column('user', sa.Column('password', sa.String(256), nullable=False)),
    op.add_column('user', sa.Column('delete_flag', sa.Boolean, default=0)),
    op.add_column('user', sa.Column('created_at', sa.DateTime)),
    op.add_column('user', sa.Column('updated_at', sa.DateTime))


def downgrade():
    op.drop_column('user', 'email'),
    op.drop_column('user', 'password'),
    op.drop_column('user', 'delete_flag'),
    op.drop_column('user', 'created_at'),
    op.drop_column('user', 'updated_at')
