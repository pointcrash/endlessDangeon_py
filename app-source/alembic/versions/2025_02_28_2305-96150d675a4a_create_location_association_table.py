"""create location association table

Revision ID: 96150d675a4a
Revises: af33c4e0f891
Create Date: 2025-02-28 23:05:18.116827

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "96150d675a4a"
down_revision: Union[str, None] = "af33c4e0f891"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "location_association",
        sa.Column("location_id", sa.Integer(), nullable=False),
        sa.Column("related_location_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["location_id"],
            ["locations.id"],
            name=op.f("fk_location_association_location_id_locations"),
        ),
        sa.ForeignKeyConstraint(
            ["related_location_id"],
            ["locations.id"],
            name=op.f("fk_location_association_related_location_id_locations"),
        ),
        sa.PrimaryKeyConstraint(
            "location_id",
            "related_location_id",
            name=op.f("pk_location_association"),
        ),
    )


def downgrade() -> None:
    op.drop_table("location_association")
