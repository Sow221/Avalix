"""Renomme customers.cif_id en customers.customer_ref (identifiant client neutre).

Revision ID: 0002_rename_customer_ref
Revises: 0001_initial
Create Date: 2026-10-11
"""

from __future__ import annotations

from collections.abc import Sequence

from alembic import op

revision: str = "0002_rename_customer_ref"
down_revision: str | None = "0001_initial"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    with op.batch_alter_table("customers") as batch:
        batch.alter_column("cif_id", new_column_name="customer_ref")


def downgrade() -> None:
    with op.batch_alter_table("customers") as batch:
        batch.alter_column("customer_ref", new_column_name="cif_id")
