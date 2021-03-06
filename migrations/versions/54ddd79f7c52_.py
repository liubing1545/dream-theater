"""empty message

Revision ID: 54ddd79f7c52
Revises: None
Create Date: 2016-07-05 15:42:31.853796

"""

# revision identifiers, used by Alembic.
revision = '54ddd79f7c52'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('default', sa.Boolean(), nullable=True),
    sa.Column('permissions', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_roles_default'), 'roles', ['default'], unique=False)
    op.create_table('shows',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('thumbnail_url', sa.Text(), nullable=True),
    sa.Column('show_time', sa.DateTime(), nullable=True),
    sa.Column('location', sa.Text(), nullable=True),
    sa.Column('ticket', sa.Text(), nullable=True),
    sa.Column('detail', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_shows_show_time'), 'shows', ['show_time'], unique=False)
    op.create_index(op.f('ix_shows_timestamp'), 'shows', ['timestamp'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('confirmed', sa.Boolean(), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('location', sa.String(length=64), nullable=True),
    sa.Column('about_me', sa.Text(), nullable=True),
    sa.Column('member_since', sa.DateTime(), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.Column('avatar_url', sa.Text(), nullable=True),
    sa.Column('avatar_hash', sa.String(length=32), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('body_html', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('disabled', sa.Boolean(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('show_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['show_id'], ['shows.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comments_timestamp'), 'comments', ['timestamp'], unique=False)
    op.create_table('seats',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('row', sa.Integer(), nullable=True),
    sa.Column('column', sa.Integer(), nullable=True),
    sa.Column('show_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['show_id'], ['shows.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usersAndShows',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('show_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['show_id'], ['shows.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usersAndShows')
    op.drop_table('seats')
    op.drop_index(op.f('ix_comments_timestamp'), table_name='comments')
    op.drop_table('comments')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_shows_timestamp'), table_name='shows')
    op.drop_index(op.f('ix_shows_show_time'), table_name='shows')
    op.drop_table('shows')
    op.drop_index(op.f('ix_roles_default'), table_name='roles')
    op.drop_table('roles')
    ### end Alembic commands ###
