"""create enemies table

Revision ID: af33c4e0f891
Revises: 932133ba3941
Create Date: 2025-02-26 19:56:19.624455

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "af33c4e0f891"
down_revision: Union[str, None] = "932133ba3941"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "enemies",
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("lvl", sa.Integer(), server_default="1", nullable=False),
        sa.Column("hp", sa.Integer(), server_default="1", nullable=False),
        sa.Column("mp", sa.Integer(), server_default="0", nullable=False),
        sa.Column("image", sa.String(), server_default="", nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("location_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["location_id"],
            ["locations.id"],
            name=op.f("fk_enemies_location_id_locations"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_enemies")),
        sa.UniqueConstraint("name", name=op.f("uq_enemies_name")),
    )


def downgrade() -> None:
    op.drop_table("enemies")
