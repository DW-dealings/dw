"""empty message

Revision ID: 63ba8a4dd650
Revises: 23adf967c045
Create Date: 2020-09-09 14:40:42.902973

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '63ba8a4dd650'
down_revision = '23adf967c045'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user_role', 'emp_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('user_role', 'role_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user_role', 'role_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('user_role', 'emp_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    # ### end Alembic commands ###
