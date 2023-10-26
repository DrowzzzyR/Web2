"""create tables collection and book_collection

Revision ID: 7baa03583ee2
Revises: 85d8b1868198
Create Date: 2023-10-26 11:07:20.803383

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7baa03583ee2'
down_revision = '85d8b1868198'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('collections',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('desc', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_collections_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_collections')),
    sa.UniqueConstraint('name', name=op.f('uq_collections_name'))
    )
    op.create_table('book_collection',
    sa.Column('book.id', sa.Integer(), nullable=True),
    sa.Column('collection.id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['book.id'], ['books.id'], name=op.f('fk_book_collection_book.id_books')),
    sa.ForeignKeyConstraint(['collection.id'], ['collections.id'], name=op.f('fk_book_collection_collection.id_collections'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book_collection')
    op.drop_table('collections')
    # ### end Alembic commands ###