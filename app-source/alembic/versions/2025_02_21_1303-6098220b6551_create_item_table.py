"""create item table

Revision ID: 6098220b6551
Revises: b8e1f6c05e82
Create Date: 2025-02-21 13:03:03.484285

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "6098220b6551"
down_revision: Union[str, None] = "b8e1f6c05e82"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "items",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.Text(), server_default="", nullable=False),
        sa.Column("type", sa.String(), nullable=False),
        sa.Column("cost", sa.Integer(), server_default="1", nullable=False),
        sa.Column("image", sa.String(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_items")),
    )


def downgrade() -> None:
    op.drop_table("items")
