"""empty message

Revision ID: a458894b655e
Revises: d8416e77a2fe
Create Date: 2022-06-01 16:04:58.717316

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a458894b655e'
down_revision = 'd8416e77a2fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_venue', sa.BOOLEAN(), nullable=True))
    op.drop_column('Artist', 'seeking_talent')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_talent', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('Artist', 'seeking_venue')
    # ### end Alembic commands ###
