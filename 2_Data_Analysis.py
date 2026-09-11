import streamlit as st
import pandas as pd

st.title("IPL Data Analysis")

# Load dataset
df = pd.read_csv("IPL_Matches_Data_2008_2026.csv")

# -------------------------------------------------
# Dataset Preview
# -------------------------------------------------

st.header("Dataset Preview")

st.dataframe(df, use_container_width=True)

# -------------------------------------------------
# Dataset Information
# -------------------------------------------------

st.header("Dataset Information")

col1, col2 = st.columns(2)

with col1:
    st.write("Number of Rows:", df.shape[0])

with col2:
    st.write("Number of Columns:", df.shape[1])

st.subheader("Missing Values")

st.dataframe(
    df.isnull().sum().reset_index().rename(
        columns={"index": "Column", 0: "Missing Values"}
    ),
    use_container_width=True
)

# -------------------------------------------------
# KPI Cards
# -------------------------------------------------

st.header("Key Performance Indicators")

total_matches = len(df)
total_seasons = df["season"].nunique()
total_venues = df["venue"].nunique()
total_cities = df["city"].nunique()

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.metric("Total Matches", total_matches)

with kpi2:
    st.metric("Total Seasons", total_seasons)

with kpi3:
    st.metric("Total Venues", total_venues)

with kpi4:
    st.metric("Total Cities", total_cities)

# -------------------------------------------------
# Calculations
# -------------------------------------------------

st.header("Match Calculations")

df["total_runs"] = df["team1_runs"] + df["team2_runs"]

df["total_wickets"] = (
    df["team1_wickets"] + df["team2_wickets"]
)

average_match_runs = df["total_runs"].mean()

highest_combined_score = df["total_runs"].max()

total_wickets = df["total_wickets"].sum()

calc1, calc2, calc3, calc4 = st.columns(4)

with calc1:
    st.metric(
        "Average Match Runs",
        round(average_match_runs, 2)
    )

with calc2:
    st.metric(
        "Highest Combined Score",
        highest_combined_score
    )

with calc3:
    st.metric(
        "Total Wickets",
        total_wickets
    )

with calc4:
    st.metric(
        "Total Match Runs",
        df["total_runs"].sum()
    )

# -------------------------------------------------
# Filters
# -------------------------------------------------

st.header("Interactive Filters")

seasons = sorted(df["season"].dropna().unique())

selected_season = st.selectbox(
    "Select Season",
    ["All Seasons"] + list(seasons)
)

teams = sorted(
    set(df["team1"].dropna().unique())
    | set(df["team2"].dropna().unique())
)

selected_team = st.selectbox(
    "Select Team",
    ["All Teams"] + teams
)

filtered_df = df.copy()

if selected_season != "All Seasons":
    filtered_df = filtered_df[
        filtered_df["season"] == selected_season
    ]

if selected_team != "All Teams":
    filtered_df = filtered_df[
        (filtered_df["team1"] == selected_team)
        | (filtered_df["team2"] == selected_team)
    ]

st.subheader("Filtered Data")

st.dataframe(
    filtered_df,
    use_container_width=True
)

st.write(
    "Number of filtered matches:",
    len(filtered_df)
)

# -------------------------------------------------
# Matches by Season
# -------------------------------------------------

st.header("Matches by Season")

matches_by_season = (
    df.groupby("season")
    .size()
    .reset_index(name="matches")
)

st.dataframe(
    matches_by_season,
    use_container_width=True
)

# -------------------------------------------------
# Wins by Team
# -------------------------------------------------

st.header("Wins by Team")

wins_by_team = (
    df["winner"]
    .value_counts()
    .reset_index()
)

wins_by_team.columns = ["Team", "Wins"]

st.dataframe(
    wins_by_team.head(10),
    use_container_width=True
)