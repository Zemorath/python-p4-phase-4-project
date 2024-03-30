"""added available services table

Revision ID: b474137da725
Revises: db408067b77e
Create Date: 2024-03-29 21:59:32.437525

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b474137da725'
down_revision = 'db408067b77e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('available_services',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('subscriptions', schema=None) as batch_op:
        batch_op.alter_column('status',
               existing_type=sa.BOOLEAN(),
               type_=sa.String(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('subscriptions', schema=None) as batch_op:
        batch_op.alter_column('status',
               existing_type=sa.String(),
               type_=sa.BOOLEAN(),
               existing_nullable=True)

    op.drop_table('available_services')
    # ### end Alembic commands ###
