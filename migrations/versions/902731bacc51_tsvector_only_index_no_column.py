"""tsvector only index no column

Revision ID: 902731bacc51
Revises: f91f96702648
Create Date: 2024-12-14 17:51:00.274393

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '902731bacc51'
down_revision = 'f91f96702648'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_index('ix_post_search_vector', postgresql_using='gin')
        batch_op.create_index('ix_post_search_vector', [sa.text("to_tsvector(CAST('english' AS REGCONFIG), CAST(body AS TEXT))")], unique=False, postgresql_using='gin')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_index('ix_post_search_vector', postgresql_using='gin')
        batch_op.create_index('ix_post_search_vector', [sa.text("to_tsvector('english'::regconfig, body::text)")], unique=False, postgresql_using='gin')

    # ### end Alembic commands ###
