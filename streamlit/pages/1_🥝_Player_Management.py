import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Player Management",
    page_icon=":kiwi:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# filepaths
player_filepath = "./tables/player_data.csv"

columns = ["name", "points", "games_played", "games_won", "games_drawn", "games_lost", "goals_for", "goals_against", "personal_goals"]

def load_player_data():
    if os.path.exists(player_filepath):
        df = pd.read_csv(player_filepath)
        for col in columns:
            if col not in df.columns:
                df[col] = 0 if col != "name" else ""
        return df[columns]
    else:
        return pd.DataFrame(columns=columns)

def save_player_data(df):
    df.to_csv(player_filepath, index=False)

st.title("🍍 Player Management")

# Load existing or empty DataFrame
player_df = load_player_data()

# Form to add a new player
with st.form("add_player_form"):
    st.subheader("Add New Player")
    name = st.text_input("Player Name")
    submit = st.form_submit_button("Add Player")
    
    if submit:
        if name and name not in player_df["name"].values:
            new_row = {
                "name": name,
                "points": 0,
                "games_played": 0,
                "games_won": 0,
                "games_drawn": 0,
                "games_lost": 0,
                "goals_for": 0,
                "goals_against": 0,
                "personal_goals": 0,
            }
            player_df = pd.concat([player_df, pd.DataFrame([new_row])], ignore_index=True)
            save_player_data(player_df)
            st.success(f"Player '{name}' added.")
        elif name in player_df["name"].values:
            st.warning("Player already exists.")
        else:
            st.error("Please enter a name.")

# Display the current player table
st.subheader("Current Player List")
st.dataframe(
    player_df.sort_values(by="points", ascending=False)
    ,hide_index=True
    ,use_container_width=True
)