"""Create patients table

Revision ID: 8bed2daacd98
Revises: 
Create Date: 2022-07-07 22:19:00.465404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8bed2daacd98'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "patients",
        sa.Column("patient_id", sa.Integer, primary_key=True),
        sa.Column("patient_last_name", sa.String),
        sa.Column("patient_first_name", sa.String),
        sa.Column("patient_middle_name", sa.String),
        sa.Column("patient_birth_date", sa.Date)
    )


def downgrade() -> None:
    op.drop_table("patients")
