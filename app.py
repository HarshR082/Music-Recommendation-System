import streamlit as st
from deepface import DeepFace
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from PIL import Image
import io

# -------------------------------------------
# Spotify Credentials
# -------------------------------------------
client_id = "YOUR_SPOTIFY CLIENT_ID"
client_secret = "YOUR SPOTIFY CLIENT_SECRET"

# Authenticate Spotify
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=client_id, 
    client_secret=client_secret
))

# -------------------------------------------
# Streamlit App UI
# -------------------------------------------
st.title("🎵 MoodMusic - Spotify Recommender")
st.caption("Detect your mood from webcam and get personalized Spotify playlists!")

# -------------------------------------------
# Step 1: Webcam Input
# -------------------------------------------
uploaded_image = st.camera_input("📸 Capture your mood")

if uploaded_image is not None:
    # Display captured image
    image_bytes = uploaded_image.getvalue()
    image = Image.open(io.BytesIO(image_bytes))
    st.image(image, caption='Captured Image', use_column_width=True)

    # Save image to disk
    with open("temp.jpg", "wb") as f:
        f.write(image_bytes)

    # ---------------------------------------
    # Step 2: Mood Detection with DeepFace
    # ---------------------------------------
    with st.spinner("Analyzing mood..."):
        try:
            result = DeepFace.analyze("temp.jpg", actions=['emotion'], enforce_detection=False)
            detected_mood = result[0]['dominant_emotion']
            st.success(f"✅ Detected Mood: **{detected_mood.capitalize()}**")
        except Exception as e:
            st.error(f"Error during mood analysis: {e}")
            st.stop()

    # ---------------------------------------
    # Step 3: Map Mood to Spotify Query
    # ---------------------------------------
    mood_mapping = {
        "happy": "party upbeat",
        "sad": "acoustic sad",
        "angry": "metal",
        "neutral": "chill",
        "surprised": "feel-good hits",
        "fearful": "ambient calm",
        "disgust": "grunge"
    }
    search_query = mood_mapping.get(detected_mood.lower(), "chill")
    st.info(f"🎯 Using Spotify search term: **{search_query}**")

    # ---------------------------------------
    # Step 4: Fetch Spotify Playlists
    # ---------------------------------------
    if st.button("🎧 Get Spotify Recommendations"):
        with st.spinner("Fetching playlists from Spotify..."):
            try:
                results = sp.search(q=search_query, type='playlist', limit=5)
                playlists = results.get('playlists', {}).get('items', [])

                if not playlists:
                    st.warning("No playlists found for this mood. Try again or change mood.")
                else:
                    st.subheader("Recommended Playlists:")

                    for playlist in playlists:
                        if not playlist:
                            continue  # ✅ Skip None entries

                        st.markdown("---")

                        # ✅ 1️⃣ Safe Image with Fallback
                        image_url = "https://via.placeholder.com/300x300.png?text=No+Image"
                        if playlist.get('images') and len(playlist['images']) > 0:
                            image_url = playlist['images'][0].get('url', image_url)
                        st.image(image_url, width=300)

                        # ✅ 2️⃣ Safe Name
                        playlist_name = playlist.get('name', 'No Name Available')
                        st.subheader(playlist_name)

                        # ✅ 3️⃣ Safe Description
                        description = playlist.get('description', '')
                        if description:
                            st.write(description)

                        # ✅ 4️⃣ Safe Spotify Link
                        spotify_url = "#"
                        if playlist.get('external_urls') and playlist['external_urls'].get('spotify'):
                            spotify_url = playlist['external_urls']['spotify']
                        st.markdown(f"[🎧 **Open in Spotify**]({spotify_url})")

            except Exception as e:
                st.error(f"Error fetching playlists: {e}")
