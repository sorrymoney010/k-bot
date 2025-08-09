import streamlit as st

st.set_page_config(page_title="Karmic Bot Farm", layout="wide")

st.title("Karmic Bot Farm 🧿")
st.markdown("### Spiritual Automation Dashboard")
st.write("Control your karmic automation bots and spiritual overlays from here.")

# Sidebar controls
st.sidebar.header("Bot Controls")
bot_1 = st.sidebar.checkbox("Activate Bot 1")
bot_2 = st.sidebar.checkbox("Activate Bot 2")
bot_3 = st.sidebar.checkbox("Activate Bot 3")

# Spiritual overlay controls
st.sidebar.header("Spiritual Overlays")
mantra = st.sidebar.text_input("Daily Mantra")
sigil = st.sidebar.file_uploader("Upload Sigil", type=["png", "jpg", "jpeg"])

# Main content
if bot_1 or bot_2 or bot_3:
    st.success("One or more bots are active.")
else:
    st.warning("No bots active.")

if mantra:
    st.info(f"Today's Mantra: {mantra}")

if sigil:
    st.image(sigil, caption="Uploaded Sigil", use_column_width=True)

# Activity log
st.subheader("Activity Log")
st.write("No recent activity yet.")
