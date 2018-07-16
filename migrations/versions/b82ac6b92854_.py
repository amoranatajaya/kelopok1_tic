"""empty message

Revision ID: b82ac6b92854
Revises: 55228ee71ed7
Create Date: 2018-07-16 12:33:15.520515

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b82ac6b92854'
down_revision = '55228ee71ed7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mata_kuliah',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('kd_mk', sa.String(length=10), nullable=True),
    sa.Column('nama_mk', sa.String(length=50), nullable=False),
    sa.Column('sks', sa.String(length=10), nullable=False),
    sa.Column('semester', sa.String(length=10), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.Column('updated_at', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mata_kuliah')
    # ### end Alembic commands ###