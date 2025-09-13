import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------- Step 1: Load Data ----------
# Replace with your actual file names
time_data = pd.read_csv("multiTimeline_new.csv")      # interest over time
region_data = pd.read_csv("multiTimeline_new.csv")  # interest by region
print(time_data.columns.tolist())


# ---------- Step 2: Clean & Rename Columns ----------
# Replace '<1' with 0
time_data = time_data.replace('<1', 0)
region_data = region_data.replace('<1', 0)

# Rename columns for simplicity
time_data.rename(columns={
    'ChatGPT: (Worldwide)': 'ChatGPT',
    'Gemini: (Worldwide)': 'Gemini',
    'Microsoft Copilot: (Worldwide)': 'Copilot'
}, inplace=True)

region_data.rename(columns={
    'ChatGPT: (Worldwide)': 'ChatGPT',
    'Gemini: (Worldwide)': 'Gemini',
    'Microsoft Copilot: (Worldwide)': 'Copilot'
}, inplace=True)

# Convert numeric columns
for col in ['ChatGPT', 'Gemini', 'Copilot']:
    time_data[col] = pd.to_numeric(time_data[col])
    region_data[col] = pd.to_numeric(region_data[col])

# Convert Week column to datetime
time_data['Week'] = pd.to_datetime(time_data['Week'])

# ---------- Step 3: Quick EDA ----------
print("---- Time Data Info ----")
print(time_data.info())
print("\n---- Summary Stats ----")
print(time_data.describe())

# ---------- Step 4: Trend Line Chart ----------
plt.figure(figsize=(12,6))
plt.plot(time_data['Week'], time_data['ChatGPT'], label='ChatGPT', color='blue')
plt.plot(time_data['Week'], time_data['Gemini'], label='Gemini', color='orange')
plt.plot(time_data['Week'], time_data['Copilot'], label='Copilot', color='gray')
plt.xlabel("Week")
plt.ylabel("Search Interest (0-100)")
plt.title("Search Trends: ChatGPT vs Gemini vs Copilot")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------- Step 5: Key Peaks & Insights ----------
for tool in ['ChatGPT', 'Gemini', 'Copilot']:
    peak_week = time_data.loc[time_data[tool].idxmax(), 'Week']
    peak_value = time_data[tool].max()
    print(f"{tool} peak: {peak_week.date()} with value {peak_value}")

# ---------- Step 6: Regional Analysis ----------
for tool in ['ChatGPT', 'Gemini', 'Copilot']:
    top_regions = region_data[['Region', tool]].sort_values(by=tool, ascending=False).head(10)
    print(f"\nTop 10 regions for {tool}:")
    print(top_regions)

    # Bar chart for top regions
    plt.figure(figsize=(10,5))
    sns.barplot(x=tool, y='Region', data=top_regions, palette="viridis")
    plt.title(f"Top 10 Regions for {tool}")
    plt.xlabel("Search Interest")
    plt.ylabel("Region")
    plt.tight_layout()
    plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # ---------- Step 1: Load Data with auto-skip ----------
# # Adjust skiprows if needed; starts reading from the row with headers
# time_data = pd.read_csv("multiTimeline_new.csv", skiprows=1)
# region_data = pd.read_csv("multiTimeline_new.csv", skiprows=1)

# # ---------- Step 2: Clean Column Names ----------
# # Strip spaces and rename columns for simplicity
# time_data.columns = time_data.columns.str.strip()
# region_data.columns = region_data.columns.str.strip()

# time_data.rename(columns={
#     'ChatGPT: (Worldwide)': 'ChatGPT',
#     'Gemini: (Worldwide)': 'Gemini',
#     'Microsoft Copilot: (Worldwide)': 'Copilot'
# }, inplace=True)

# region_data.rename(columns={
#     'ChatGPT: (Worldwide)': 'ChatGPT',
#     'Gemini: (Worldwide)': 'Gemini',
#     'Microsoft Copilot: (Worldwide)': 'Copilot'
# }, inplace=True)

# # ---------- Step 3: Replace <1 and convert to numeric ----------
# time_data.replace('<1', 0, inplace=True)
# region_data.replace('<1', 0, inplace=True)

# for col in ['ChatGPT', 'Gemini', 'Copilot']:
#     time_data[col] = pd.to_numeric(time_data[col], errors='coerce').fillna(0)
#     region_data[col] = pd.to_numeric(region_data[col], errors='coerce').fillna(0)

# # Convert Week to datetime
# time_data['Week'] = pd.to_datetime(time_data['Week'], errors='coerce')

# # ---------- Step 4: Quick EDA ----------
# print("---- Time Data Info ----")
# print(time_data.info())
# print("\n---- Summary Stats ----")
# print(time_data.describe())

# # ---------- Step 5: Trend Line Chart ----------
# plt.figure(figsize=(12,6))
# plt.plot(time_data['Week'], time_data['ChatGPT'], label='ChatGPT', color='blue')
# plt.plot(time_data['Week'], time_data['Gemini'], label='Gemini', color='orange')
# plt.plot(time_data['Week'], time_data['Copilot'], label='Copilot', color='gray')
# plt.xlabel("Week")
# plt.ylabel("Search Interest (0-100)")
# plt.title("Search Trends: ChatGPT vs Gemini vs Copilot")
# plt.legend()
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# # ---------- Step 6: Peak Week Analysis ----------
# for tool in ['ChatGPT', 'Gemini', 'Copilot']:
#     peak_row = time_data.loc[time_data[tool].idxmax()]
#     print(f"{tool} peak: {peak_row['Week'].date()} with value {peak_row[tool]}")

# # ---------- Step 7: Regional Top 10 Analysis ----------
# for tool in ['ChatGPT', 'Gemini', 'Copilot']:
#     if 'Region' not in region_data.columns:
#         print(f"Region column not found for {tool}")
#         continue
#     top_regions = region_data[['Region', tool]].sort_values(by=tool, ascending=False).head(10)
#     print(f"\nTop 10 regions for {tool}:")
#     print(top_regions)

#     # Bar chart for top regions
#     plt.figure(figsize=(10,5))
#     sns.barplot(x=tool, y='Region', data=top_regions, palette="viridis")
#     plt.title(f"Top 10 Regions for {tool}")
#     plt.xlabel("Search Interest")
#     plt.ylabel("Region")
#     plt.tight_layout()
#     plt.show()
