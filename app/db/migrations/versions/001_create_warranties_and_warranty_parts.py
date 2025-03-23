"""create warranties and warranty parts tables

Revision ID: 001
Revises: 
Create Date: 2024-03-19 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from datetime import date

# revision identifiers, used by Alembic.
revision = '001'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Create warranties table
    op.create_table(
        'warranties',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('vehicle_id', sa.Integer(), nullable=False),
        sa.Column('part_id', sa.Integer(), nullable=False),
        sa.Column('location_id', sa.Integer(), nullable=False),
        sa.Column('failure_type', sa.String(), nullable=False),
        sa.Column('failure_date', sa.Date(), nullable=False),
        sa.Column('description', sa.String(), nullable=False),
        sa.Column('status', sa.String(), nullable=False),
        sa.Column('resolution_date', sa.Date(), nullable=True),
        sa.Column('resolution_description', sa.String(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['vehicle_id'], ['vehicles.id'], ),
        sa.ForeignKeyConstraint(['part_id'], ['parts.id'], ),
        sa.ForeignKeyConstraint(['location_id'], ['locations.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_warranties_id'), 'warranties', ['id'], unique=False)

    # Create warranty_parts table
    op.create_table(
        'warranty_parts',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('warranty_id', sa.Integer(), nullable=False),
        sa.Column('part_id', sa.Integer(), nullable=False),
        sa.Column('supplier_id', sa.Integer(), nullable=False),
        sa.Column('quantity', sa.Integer(), nullable=False),
        sa.Column('unit_price', sa.Float(), nullable=False),
        sa.Column('total_price', sa.Float(), nullable=False),
        sa.Column('notes', sa.String(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['warranty_id'], ['warranties.id'], ),
        sa.ForeignKeyConstraint(['part_id'], ['parts.id'], ),
        sa.ForeignKeyConstraint(['supplier_id'], ['suppliers.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_warranty_parts_id'), 'warranty_parts', ['id'], unique=False)

def downgrade():
    op.drop_index(op.f('ix_warranty_parts_id'), table_name='warranty_parts')
    op.drop_table('warranty_parts')
    op.drop_index(op.f('ix_warranties_id'), table_name='warranties')
    op.drop_table('warranties') 