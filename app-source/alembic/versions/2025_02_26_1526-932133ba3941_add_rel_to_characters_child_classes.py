"""add rel to characters child classes

Revision ID: 932133ba3941
Revises: 0e1f69ab3bf1
Create Date: 2025-02-26 15:26:31.054385

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "932133ba3941"
down_revision: Union[str, None] = "0e1f69ab3bf1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("npcs", sa.Column("location_id", sa.Integer(), nullable=True))
    op.create_foreign_key(
        op.f("fk_npcs_location_id_locations"),
        "npcs",
        "locations",
        ["location_id"],
        ["id"],
    )
    op.add_column(
        "player_characters",
        sa.Column("location_id", sa.Integer(), nullable=True),
    )
    op.create_foreign_key(
        op.f("fk_player_characters_location_id_locations"),
        "player_characters",
        "locations",
        ["location_id"],
        ["id"],
    )


def downgrade() -> None:
    op.drop_constraint(
        op.f("fk_player_characters_location_id_locations"),
        "player_characters",
        type_="foreignkey",
    )
    op.drop_column("player_characters", "location_id")
    op.drop_constraint(
        op.f("fk_npcs_location_id_locations"), "npcs", type_="foreignkey"
    )
    op.drop_column("npcs", "location_id")
