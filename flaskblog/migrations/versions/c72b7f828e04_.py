"""empty message

Revision ID: c72b7f828e04
Revises: 512588c697df
Create Date: 2020-07-30 17:37:59.170885

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c72b7f828e04'
down_revision = '512588c697df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('type',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('type_name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('article', sa.Column('type_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'article', 'user', ['user_id'], ['id'])
    op.create_foreign_key(None, 'article', 'type', ['type_id'], ['id'])
    op.create_foreign_key(None, 'comment', 'user', ['user_id'], ['id'])
    op.create_foreign_key(None, 'comment', 'article', ['article_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.drop_constraint(None, 'article', type_='foreignkey')
    op.drop_constraint(None, 'article', type_='foreignkey')
    op.drop_column('article', 'type_id')
    op.drop_table('type')
    # ### end Alembic commands ###
