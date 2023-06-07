"""users table

Revision ID: 8f9e36a12319
Revises: 
Create Date: 2023-06-06 14:06:04.298274

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f9e36a12319'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'users',
        sa.Column('id', sa.BIGINT(), autoincrement=False, nullable=False),
        sa.Column('balance', sa.BIGINT(), nullable=False, default=0),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
