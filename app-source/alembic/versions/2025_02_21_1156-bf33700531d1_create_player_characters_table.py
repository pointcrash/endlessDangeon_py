"""create player characters table

Revision ID: bf33700531d1
Revises: 2009c6ad4bf0
Create Date: 2025-02-21 11:56:02.977026

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "bf33700531d1"
down_revision: Union[str, None] = "2009c6ad4bf0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "player_characters",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("lvl", sa.Integer(), server_default="1", nullable=False),
        sa.Column("hp", sa.Integer(), server_default="1", nullable=False),
        sa.Column("mp", sa.Integer(), server_default="0", nullable=False),
        sa.Column("image", sa.String(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
            name=op.f("fk_player_characters_user_id_users"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_player_characters")),
        sa.UniqueConstraint("name", name=op.f("uq_player_characters_name")),
        sa.UniqueConstraint("user_id", name=op.f("uq_player_characters_user_id")),
    )


def downgrade() -> None:
    op.drop_table("player_characters")
