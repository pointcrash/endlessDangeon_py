"""create npc table

Revision ID: ddcd363636e7
Revises: 6098220b6551
Create Date: 2025-02-21 13:09:40.858168

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "ddcd363636e7"
down_revision: Union[str, None] = "6098220b6551"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "npcs",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("lvl", sa.Integer(), server_default="1", nullable=False),
        sa.Column("hp", sa.Integer(), server_default="1", nullable=False),
        sa.Column("mp", sa.Integer(), server_default="0", nullable=False),
        sa.Column("image", sa.String(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_npcs")),
        sa.UniqueConstraint("name", name=op.f("uq_npcs_name")),
    )


def downgrade() -> None:
    op.drop_table("npcs")
