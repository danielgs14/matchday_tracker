import streamlit as st

st.set_page_config(
    page_title="Weekly Matchday Tracker",
    page_icon=":coconut:",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.header("Weekly Matchday Tracker")

st.subheader("About this app")
st.markdown("I play six-a-side football matches with friends every week and we wanted to keep track of our stats. Here, you'll first enter all players in your group, then select two teams of six players each. During the match, you can keep a record for goals scored by each player by pressing a button. After the match, you can enter the final score. The app will automatically update the stats for each player based on their performance in the match.")


st.subheader("How to Use")
st.markdown("1. In 🥝 **Player Management**, you start by creating the list of players. Add all your players names in here. You'll only need to do this whenever a new players is added to the group, not every week when you play.") 
st.markdown("2. Then you'll visit  🥭 **Matchday Team Selection**, which you'll use every match day when teams are all set and ready to play.")
st.markdown("3. Based on the teams you entered in 🥭 **Matchday Team Selection**, a list of players in 🍌 **Individual Goal Tracker** will load. During the game, you can press each name to add a goal.")
st.markdown("4. You'll then go to 🍋 **Matchday Results** to submit the final score")
st.markdown("5. Each week, 🍉 **Stats** will be updated with the information you entered and you'll be able to see who's leading the table.")