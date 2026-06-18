import pandas as pd

# ==========================================
# STEP 1: Load the dataset
# ==========================================

df = pd.read_csv("Dataset for Data Analytics - Sheet1.csv")

print("\n========== ORIGINAL DATA ==========")
print(df.head())

# ==========================================
# STEP 2: Check dataset size and structure
# ==========================================

print("\n========== DATASET SHAPE ==========")
print("Rows and Columns:", df.shape)

print("\n========== DATA INFORMATION ==========")
df.info()

# ==========================================
# STEP 3: Check missing values
# ==========================================

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Handle missing values
# Remove rows with missing OrderID because ID is important
df.dropna(subset=["OrderID"], inplace=True)

# Fill missing values in text columns with "Unknown"
text_columns = df.select_dtypes(include="object").columns
df[text_columns] = df[text_columns].fillna("Unknown")

# Fill missing numerical columns with median
number_columns = df.select_dtypes(include=["int64", "float64"]).columns
df[number_columns] = df[number_columns].fillna(
    df[number_columns].median()
)

print("\nMissing values after cleaning:")
print(df.isnull().sum())


# ==========================================
# STEP 4: Remove duplicate rows
# ==========================================

print("\n========== DUPLICATES ==========")

print("Duplicate rows before removing:",
      df.duplicated().sum())

df.drop_duplicates(inplace=True)

print("Duplicate rows after removing:",
      df.duplicated().sum())


# ==========================================
# STEP 5: Check duplicate Order IDs
# ==========================================

print("\n========== ORDER ID CHECK ==========")

duplicate_ids = df["OrderID"].duplicated().sum()

print("Duplicate Order IDs before cleaning:",
      duplicate_ids)

df.drop_duplicates(subset=["OrderID"],
                   keep="first",
                   inplace=True)

print("Duplicate Order IDs after cleaning:",
      df["OrderID"].duplicated().sum())


# ==========================================
# STEP 6: Correct Date Format
# ==========================================

print("\n========== DATE FORMAT CHECK ==========")

df["Date"] = pd.to_datetime(
    df["Date"],
    errors="coerce"
)

print("Invalid dates:",
      df["Date"].isnull().sum())


# Remove rows with invalid dates
df.dropna(subset=["Date"], inplace=True)


# ==========================================
# STEP 7: Standardize text formatting
# ==========================================

text_columns = df.select_dtypes(include="object").columns

for column in text_columns:
    df[column] = (
        df[column]
        .astype(str)
        .str.strip()
        .str.title()
    )


# ==========================================
# STEP 8: Final quality check
# ==========================================

print("\n========== FINAL DATA CHECK ==========")

print("Final dataset shape:")
print(df.shape)

print("\nRemaining missing values:")
print(df.isnull().sum())

print("\nRemaining duplicate rows:")
print(df.duplicated().sum())

print("\nRemaining duplicate Order IDs:")
print(df["OrderID"].duplicated().sum())


# ==========================================
# STEP 9: Save cleaned dataset
# ==========================================

df.to_csv(
    "cleaned_dataset.csv",
    index=False
)

print(
    "\nData cleaning completed successfully!"
)

print(
    "Cleaned file saved as cleaned_dataset.csv"
)