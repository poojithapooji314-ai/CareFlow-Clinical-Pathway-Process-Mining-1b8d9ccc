import pandas as pd

data = {
	"case_id": ["P001", "P001", "P002", "P002"],
	"timestamp": [
		"2026-01-01 09:00",
		"2026-01-01 10:00",
		"2026-01-01 09:10",
		"2026-01-01 10:30",
	],
}

df = pd.DataFrame(data)
df["timestamp"] = pd.to_datetime(df["timestamp"])

duration = df.groupby("case_id")["timestamp"].agg(
	start="min",
	end="max",
)

duration["duration_minutes"] = (
	duration["end"] - duration["start"]
).dt.total_seconds() / 60

print("Synthetic Journey Duration Analysis")
print(duration.to_string())
