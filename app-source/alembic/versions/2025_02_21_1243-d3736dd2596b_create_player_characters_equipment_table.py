"""create player characters equipment table

Revision ID: d3736dd2596b
Revises: bf33700531d1
Create Date: 2025-02-21 12:43:50.424508

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "d3736dd2596b"
down_revision: Union[str, None] = "bf33700531d1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "character_equipments",
        sa.Column("helmet", sa.Integer(), nullable=False),
        sa.Column("body_armour", sa.Integer(), nullable=False),
        sa.Column("boots", sa.Integer(), nullable=False),
        sa.Column("gloves", sa.Integer(), nullable=False),
        sa.Column("backpack", sa.Integer(), nullable=False),
        sa.Column("weapon_1", sa.Integer(), nullable=False),
        sa.Column("weapon_2", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("character_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["character_id"],
            ["player_characters.id"],
            name=op.f("fk_character_equipments_character_id_player_characters"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_character_equipments")),
        sa.UniqueConstraint(
            "character_id", name=op.f("uq_character_equipments_character_id")
        ),
    )


def downgrade() -> None:
    op.drop_table("character_equipments")
