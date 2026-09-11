import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title("IPL Data Visualization")

# Load dataset
df = pd.read_csv("IPL_Matches_Data_2008_2026.csv")

# Calculate total runs
df["total_runs"] = df["team1_runs"] + df["team2_runs"]

# -------------------------------------------------
# Matches by Season - Bar Chart
# -------------------------------------------------

st.header("Matches by Season")

matches_by_season = (
    df.groupby("season")
    .size()
    .reset_index(name="matches")
)

fig_bar = px.bar(
    matches_by_season,
    x="season",
    y="matches",
    title="Number of Matches by Season"
)

st.plotly_chart(fig_bar, use_container_width=True)

# -------------------------------------------------
# Total Runs by Season - Line Chart
# -------------------------------------------------

st.header("Total Runs by Season")

runs_by_season = (
    df.groupby("season")["total_runs"]
    .sum()
    .reset_index()
)

fig_line = px.line(
    runs_by_season,
    x="season",
    y="total_runs",
    markers=True,
    title="Total Runs by Season"
)

st.plotly_chart(fig_line, use_container_width=True)

# -------------------------------------------------
# Top 10 Winning Teams - Bar Chart
# -------------------------------------------------

st.header("Top 10 Winning Teams")

wins_by_team = (
    df["winner"]
    .value_counts()
    .reset_index()
)

wins_by_team.columns = ["Team", "Wins"]

top_10_teams = wins_by_team.head(10)

fig_team = px.bar(
    top_10_teams,
    x="Team",
    y="Wins",
    title="Top 10 Teams by Number of Wins"
)

st.plotly_chart(fig_team, use_container_width=True)

# -------------------------------------------------
# Toss Decision - Pie Chart
# -------------------------------------------------

st.header("Toss Decision Distribution")

toss_decision = df["toss_decision"].value_counts().reset_index()

toss_decision.columns = ["Decision", "Count"]

fig_pie = px.pie(
    toss_decision,
    names="Decision",
    values="Count",
    title="Toss Decision Distribution"
)

st.plotly_chart(fig_pie, use_container_width=True)

# -------------------------------------------------
# Total Match Runs - Histogram
# -------------------------------------------------

st.header("Distribution of Total Match Runs")

fig_hist = px.histogram(
    df,
    x="total_runs",
    nbins=30,
    title="Distribution of Total Match Runs"
)

st.plotly_chart(fig_hist, use_container_width=True)

# -------------------------------------------------
# Team 1 Runs vs Team 2 Runs - Scatter Plot
# -------------------------------------------------

st.header("Team 1 Runs vs Team 2 Runs")

fig_scatter = px.scatter(
    df,
    x="team1_runs",
    y="team2_runs",
    title="Team 1 Runs vs Team 2 Runs",
    hover_data=["team1", "team2", "season"]
)

st.plotly_chart(fig_scatter, use_container_width=True)

# -------------------------------------------------
# Matplotlib Histogram
# -------------------------------------------------

st.header("Total Runs Histogram using Matplotlib")

fig, ax = plt.subplots()

ax.hist(df["total_runs"].dropna(), bins=30)

ax.set_title("Distribution of Total Match Runs")
ax.set_xlabel("Total Runs")
ax.set_ylabel("Number of Matches")

st.pyplot(fig)
