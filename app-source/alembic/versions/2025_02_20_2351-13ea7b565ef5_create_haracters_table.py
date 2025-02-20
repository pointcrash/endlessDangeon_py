"""create haracters table

Revision ID: 13ea7b565ef5
Revises: 2009c6ad4bf0
Create Date: 2025-02-20 23:51:27.088209

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "13ea7b565ef5"
down_revision: Union[str, None] = "2009c6ad4bf0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "characters",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("lvl", sa.Integer(), server_default="1", nullable=False),
        sa.Column("hp", sa.Integer(), server_default="1", nullable=False),
        sa.Column("mp", sa.Integer(), server_default="0", nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_characters")),
        sa.UniqueConstraint("name", name=op.f("uq_characters_name")),
    )


def downgrade() -> None:
    op.drop_table("characters")
