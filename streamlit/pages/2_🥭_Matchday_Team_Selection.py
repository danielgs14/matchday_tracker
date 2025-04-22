import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Matchday Team Selection",
    page_icon=":mango:",
    layout="wide",
    initial_sidebar_state="expanded"
)
# filepaths
player_filepath = "./tables/player_data.csv"
team_filepath = "./tables/match_teams.csv"

st.title("Matchday Team Selection")

# Load player names
if not os.path.exists(player_filepath):
    st.warning("No players available. Add players on the Player Management page.")
    st.stop()

player_df = pd.read_csv(player_filepath)
player_names = player_df["name"].tolist()

# Select players for each team
team1 = st.multiselect("Team 1", player_names, max_selections=6)
team2 = st.multiselect(
    "Team 2",
    [p for p in player_names if p not in team1],  # Exclude already selected
    max_selections=6
)

if len(team1) != 6 or len(team2) != 6:
    st.info("Please select 6 players for each team.")
else:
    if st.button("Save Matchday Teams"):
        match_df = pd.DataFrame({
            "name": team1 + team2,
            "team": ["Team 1"] * 6 + ["Team 2"] * 6
        })
        match_df.to_csv(team_filepath, index=False)
        st.success("Teams saved for the matchday.")
