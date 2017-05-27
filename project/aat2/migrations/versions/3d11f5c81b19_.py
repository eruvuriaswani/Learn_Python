"""empty message

Revision ID: 3d11f5c81b19
Revises: 
Create Date: 2017-05-25 07:11:12.701644

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d11f5c81b19'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('migrate_version')
    op.add_column('request', sa.Column('project_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'request', 'projects', ['project_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'request', type_='foreignkey')
    op.drop_column('request', 'project_id')
    op.create_table('migrate_version',
    sa.Column('repository_id', sa.VARCHAR(length=250), nullable=False),
    sa.Column('repository_path', sa.TEXT(), nullable=True),
    sa.Column('version', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('repository_id')
    )
    # ### end Alembic commands ###