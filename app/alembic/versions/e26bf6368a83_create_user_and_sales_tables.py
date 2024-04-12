"""create user and sales tables

Revision ID: e26bf6368a83
Revises: 
Create Date: 2024-04-11 22:04:20.895943

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e26bf6368a83'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('user',
        sa.Column('user_id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('username', sa.String(), unique=True),
        sa.Column('password', sa.String()),
        sa.Column('name', sa.String()),
        sa.Column('lastname', sa.String()),
        sa.Column('address', sa.String()),
        sa.Column('phone_number', sa.String()),
        sa.Column('email', sa.String(), unique=True),
        sa.Column('create_user', sa.DateTime(), default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('state', sa.Boolean(), default=False)
    )

    op.create_table('sales',
        sa.Column('sale_id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('user.user_id', ondelete='CASCADE')),
        sa.Column('sale', sa.Integer()),
        sa.Column('sales_products', sa.Integer())
    )


def downgrade() -> None:
    op.drop_table('sales')
    op.drop_table('user')
