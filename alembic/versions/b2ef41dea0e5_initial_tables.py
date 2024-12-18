"""Initial tables

Revision ID: b2ef41dea0e5
Revises: 
Create Date: 2024-09-17 11:10:41.643121

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b2ef41dea0e5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('link',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('url', sa.Unicode(), nullable=False),
                    sa.Column('hashid', sa.String(), nullable=False),
                    sa.Column('start_life', sa.TIMESTAMP(), nullable=True),
                    sa.Column('end_life', sa.TIMESTAMP(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_link_hashid'), 'link', ['hashid'], unique=True)
    op.create_index(op.f('ix_link_url'), 'link', ['url'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_link_url'), table_name='link')
    op.drop_index(op.f('ix_link_hashid'), table_name='link')
    op.drop_table('link')
    # ### end Alembic commands ###
