"""multi-language full text search

Revision ID: 5b480f137aa5
Revises: 8524c6ab4cfd
Create Date: 2024-12-14 20:58:09.473787

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5b480f137aa5'
down_revision = '8524c6ab4cfd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_index('ix_post_search_vector', postgresql_using='gin')
        batch_op.create_index('ix_post_search_vector', [sa.text("to_tsvector(CAST('simple' AS REGCONFIG), CAST(body AS TEXT))")], unique=False, postgresql_using='gin')
        batch_op.create_index('ix_post_search_vector_en', [sa.text("to_tsvector(CAST('english' AS REGCONFIG), CAST(body AS TEXT))")], unique=False, postgresql_using='gin')
        batch_op.create_index('ix_post_search_vector_es', [sa.text("to_tsvector(CAST('spanish' AS REGCONFIG), CAST(body AS TEXT))")], unique=False, postgresql_using='gin')
        batch_op.drop_column('search_vector')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('search_vector', postgresql.TSVECTOR(), autoincrement=False, nullable=True))
        batch_op.drop_index('ix_post_search_vector_es', postgresql_using='gin')
        batch_op.drop_index('ix_post_search_vector_en', postgresql_using='gin')
        batch_op.drop_index('ix_post_search_vector', postgresql_using='gin')
        batch_op.create_index('ix_post_search_vector', ['search_vector'], unique=False, postgresql_using='gin')

    # ### end Alembic commands ###
