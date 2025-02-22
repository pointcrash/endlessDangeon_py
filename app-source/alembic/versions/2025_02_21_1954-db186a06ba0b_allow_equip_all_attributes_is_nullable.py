"""allow equip all attributes is nullable

Revision ID: db186a06ba0b
Revises: 15bb9fce4777
Create Date: 2025-02-21 19:54:50.259773

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "db186a06ba0b"
down_revision: Union[str, None] = "15bb9fce4777"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "character_equipments",
        "helmet",
        existing_type=sa.INTEGER(),
        nullable=True,
    )
    op.alter_column(
        "character_equipments",
        "body_armour",
        existing_type=sa.INTEGER(),
        nullable=True,
    )
    op.alter_column(
        "character_equipments",
        "boots",
        existing_type=sa.INTEGER(),
        nullable=True,
    )
    op.alter_column(
        "character_equipments",
        "gloves",
        existing_type=sa.INTEGER(),
        nullable=True,
    )
    op.alter_column(
        "character_equipments",
        "backpack",
        existing_type=sa.INTEGER(),
        nullable=True,
    )
    op.alter_column(
        "character_equipments",
        "weapon_1",
        existing_type=sa.INTEGER(),
        nullable=True,
    )
    op.alter_column(
        "character_equipments",
        "weapon_2",
        existing_type=sa.INTEGER(),
        nullable=True,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "character_equipments",
        "weapon_2",
        existing_type=sa.INTEGER(),
        nullable=False,
    )
    op.alter_column(
        "character_equipments",
        "weapon_1",
        existing_type=sa.INTEGER(),
        nullable=False,
    )
    op.alter_column(
        "character_equipments",
        "backpack",
        existing_type=sa.INTEGER(),
        nullable=False,
    )
    op.alter_column(
        "character_equipments",
        "gloves",
        existing_type=sa.INTEGER(),
        nullable=False,
    )
    op.alter_column(
        "character_equipments",
        "boots",
        existing_type=sa.INTEGER(),
        nullable=False,
    )
    op.alter_column(
        "character_equipments",
        "body_armour",
        existing_type=sa.INTEGER(),
        nullable=False,
    )
    op.alter_column(
        "character_equipments",
        "helmet",
        existing_type=sa.INTEGER(),
        nullable=False,
    )
    # ### end Alembic commands ###
