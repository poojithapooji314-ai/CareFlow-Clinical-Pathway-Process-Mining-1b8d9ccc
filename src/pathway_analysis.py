
import pandas as pd

# Synthetic example only — not real patient data
events = pd.DataFrame([
    ["P001", "Registration", "2026-01-01 09:00"],
    ["P001", "Assessment",   "2026-01-01 09:20"],
    ["P001", "Treatment",    "2026-01-01 10:00"],
    ["P002", "Registration", "2026-01-01 09:10"],
    ["P002", "Assessment",   "2026-01-01 09:40"],
    ["P002", "Treatment",    "2026-01-01 10:30"],
    ["P003", "Registration", "2026-01-01 08:00"],
    ["P003", "Assessment",   "2026-01-01 08:25"],
])

events.columns = ["case_id", "activity", "timestamp"]
events["timestamp"] = pd.to_datetime(events["timestamp"])
events = events.sort_values(["case_id", "timestamp"])

# Discover each case's activity sequence
pathways = (
    events.groupby("case_id")["activity"]
    .apply(lambda activities: " -> ".join(activities))
)

print("SYNTHETIC PATHWAY ANALYSIS")
print("\nActivity pathway for each case:")
print(pathways.to_string())

# Count transitions between consecutive activities
events["next_activity"] = (
    events.groupby("case_id")["activity"].shift(-1)
)

transitions = (
    events.dropna(subset=["next_activity"])
    .groupby(["activity", "next_activity"])
    .size()
    .reset_index(name="frequency")
    .sort_values("frequency", ascending=False)
)

print("\nActivity transition frequencies:")
print(transitions.to_string(index=False))
