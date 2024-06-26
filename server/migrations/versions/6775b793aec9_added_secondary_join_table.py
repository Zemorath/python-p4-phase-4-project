"""added secondary join table

Revision ID: 6775b793aec9
Revises: 3e896ff93f47
Create Date: 2024-04-09 20:42:24.423619

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6775b793aec9'
down_revision = '3e896ff93f47'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_assigned_employees',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], name=op.f('fk_user_assigned_employees_employee_id_employees')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_user_assigned_employees_user_id_users')),
    sa.PrimaryKeyConstraint('user_id', 'employee_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_assigned_employees')
    # ### end Alembic commands ###
