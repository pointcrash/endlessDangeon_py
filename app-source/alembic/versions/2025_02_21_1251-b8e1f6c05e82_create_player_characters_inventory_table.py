"""create player characters inventory table

Revision ID: b8e1f6c05e82
Revises: d3736dd2596b
Create Date: 2025-02-21 12:51:46.339918

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "b8e1f6c05e82"
down_revision: Union[str, None] = "d3736dd2596b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "inventorys",
        sa.Column("slots_count", sa.Integer(), nullable=False),
        sa.Column("gold", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("character_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["character_id"],
            ["player_characters.id"],
            name=op.f("fk_inventorys_character_id_player_characters"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_inventorys")),
        sa.UniqueConstraint("character_id", name=op.f("uq_inventorys_character_id")),
    )


def downgrade() -> None:
    op.drop_table("inventorys")
