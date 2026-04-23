import pandas as pd

source_file = "source.csv"
target_file = "target.csv"
output_file = "mismatch_report.csv"

primary_key = "id"  # change as needed

# Load data
src_df = pd.read_csv(source_file)
tgt_df = pd.read_csv(target_file)

# Merge on primary key (outer join to catch missing rows)
merged = src_df.merge(
    tgt_df,
    on=primary_key,
    how="outer",
    suffixes=("_src", "_tgt"),
    indicator=True
)

mismatches = []

# Identify columns (excluding primary key)
columns = [col for col in src_df.columns if col != primary_key]

for _, row in merged.iterrows():
    key = row[primary_key]

    # Row missing cases
    if row["_merge"] == "left_only":
        mismatches.append([key, "ROW_MISSING_IN_TARGET", str(row), "NOT FOUND"])
        continue
    elif row["_merge"] == "right_only":
        mismatches.append([key, "ROW_MISSING_IN_SOURCE", "NOT FOUND", str(row)])
        continue

    # Column-level comparison
    for col in columns:
        src_val = row[f"{col}_src"]
        tgt_val = row[f"{col}_tgt"]

        # Handle NaN comparison properly
        if pd.isna(src_val) and pd.isna(tgt_val):
            continue

        if src_val != tgt_val:
            mismatches.append([key, col, src_val, tgt_val])

# Convert to DataFrame
mismatch_df = pd.DataFrame(
    mismatches,
    columns=[primary_key, "column_name", "source_value", "target_value"]
)

# Save to CSV
mismatch_df.to_csv(output_file, index=False)

print("Comparison completed. Check mismatch_report.csv")