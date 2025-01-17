"""Initial migration

Revision ID: acfc966cc227
Revises: 
Create Date: 2024-10-09 11:49:30.816434

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'acfc966cc227'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pigs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pig_housee', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('pig_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pigs_id'), 'pigs', ['id'], unique=False)
    op.create_table('wolves',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('power', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_wolves_id'), 'wolves', ['id'], unique=False)
    op.create_table('houses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('sturdiness', sa.Integer(), nullable=False),
    sa.Column('pig_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pig_id'], ['pigs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_houses_id'), 'houses', ['id'], unique=False)
   
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    
    op.drop_index(op.f('ix_houses_id'), table_name='houses')
    op.drop_table('houses')
    op.drop_index(op.f('ix_wolves_id'), table_name='wolves')
    op.drop_table('wolves')
    op.drop_index(op.f('ix_pigs_id'), table_name='pigs')
    op.drop_table('pigs')
    # ### end Alembic commands ###
