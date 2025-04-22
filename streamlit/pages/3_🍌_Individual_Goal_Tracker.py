import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Individual Goal Tracker",
    page_icon=":banana:",
    layout="wide",
    initial_sidebar_state="expanded"
)

team_filepath = "./tables/match_teams.csv"
goals_filepath = "./tables/personal_goals.csv"

st.title("Goal Tracker")

# Check if team file exists
if not os.path.exists(team_filepath):
    st.warning("No teams selected yet. Please use the Matchday Selection page.")
    st.stop()

# Load team data
team_df = pd.read_csv(team_filepath)
players = team_df["name"].tolist()

# Reset goal counts if players changed
if "goal_counts" not in st.session_state or set(st.session_state.goal_counts.keys()) != set(players):
    st.session_state.goal_counts = {player: 0 for player in players}

# Reset all goals button
if st.button("Reset All Goals"):
    for player in players:
        st.session_state.goal_counts[player] = 0
    st.success("All goals have been reset.")

st.subheader("Tap a button each time a player scores.")

# Display goal buttons
for team in team_df["team"].unique():
    st.markdown(f"### {team}")
    team_players = team_df[team_df["team"] == team]["name"].tolist()
    cols = st.columns(6)

    for i, player in enumerate(team_players):
        with cols[i % 6]:
            if st.button(f"{player}", key=f"btn_{player}"):
                st.session_state.goal_counts[player] += 1
            st.write(f"Goals: {st.session_state.goal_counts[player]}")

# Show total goals per team
team1_goals = sum(
    st.session_state.goal_counts.get(player, 0)
    for player in team_df[team_df["team"] == "Team 1"]["name"]
)
team2_goals = sum(
    st.session_state.goal_counts.get(player, 0)
    for player in team_df[team_df["team"] == "Team 2"]["name"]
)

st.markdown("### Total Goals")
col1, col2 = st.columns(2)
col1.metric("Team 1", f"{team1_goals} goals")
col2.metric("Team 2", f"{team2_goals} goals")

# Save to file
if st.button("Save Personal Goals"):
    goal_df = pd.DataFrame([
        {"name": player, "personal_goals": goals}
        for player, goals in st.session_state.goal_counts.items()
    ])
    goal_df.to_csv(goals_filepath, index=False)
    st.success("Personal goals saved.")
