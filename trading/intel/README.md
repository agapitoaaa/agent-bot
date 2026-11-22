# Evidence cards

One JSON object per line in `trading/intel/cards-YYYY-MM.jsonl`. Schema and rules: `docs/trader-intel-design.md`.
Cards are append-only. Never edit or delete one; supersede it with a new card that references the old `id`.
