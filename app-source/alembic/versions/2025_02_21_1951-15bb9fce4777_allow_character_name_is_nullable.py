"""allow character name is nullable

Revision ID: 15bb9fce4777
Revises: ddcd363636e7
Create Date: 2025-02-21 19:51:52.469547

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "15bb9fce4777"
down_revision: Union[str, None] = "ddcd363636e7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column("npcs", "name", existing_type=sa.VARCHAR(), nullable=True)
    op.alter_column(
        "player_characters", "name", existing_type=sa.VARCHAR(), nullable=True
    )


def downgrade() -> None:
    op.alter_column(
        "player_characters", "name", existing_type=sa.VARCHAR(), nullable=False
    )
    op.alter_column("npcs", "name", existing_type=sa.VARCHAR(), nullable=False)
