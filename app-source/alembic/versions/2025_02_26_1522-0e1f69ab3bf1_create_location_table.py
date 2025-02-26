"""create location table

Revision ID: 0e1f69ab3bf1
Revises: db186a06ba0b
Create Date: 2025-02-26 15:22:31.228158

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "0e1f69ab3bf1"
down_revision: Union[str, None] = "db186a06ba0b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "locations",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("bg", sa.String(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_locations")),
        sa.UniqueConstraint("name", name=op.f("uq_locations_name")),
    )


def downgrade() -> None:
    op.drop_table("locations")
