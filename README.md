# 🎵 MoodMusic - Spotify Recommender Based on Real-Time Mood Detection

MoodMusic is an interactive web application built with Streamlit that detects your current emotional state via webcam and recommends Spotify playlists that match your mood — using facial emotion recognition powered by DeepFace and Spotify’s Web API.

> 🧠 Detect your emotions → 🎶 Get matching music → ▶️ Listen instantly via embedded Spotify player

---

## 🚀 Live Demo

_You can deploy this on [Streamlit Cloud](https://streamlit.io/cloud) or any server of your choice._

---

## 🎯 Key Features

- 📷 **Real-Time Mood Detection** using your webcam
- 🧠 **DeepFace AI** for emotion classification (happy, sad, angry, etc.)
- 🎧 **Spotify Integration** to fetch personalized playlists
- 🖼️ **Interactive UI** with embedded Spotify Web Player
- 🔒 Local-only execution – no face data is stored or sent anywhere

---

## 📸 Demo Preview

| Webcam Input             | Mood Detection & Playlist Suggestions   |
|--------------------------|-----------------------------------------|
| ![Webcam Capture](https://via.placeholder.com/300x300.png?text=Camera+Input) | ![Spotify Recommendations](https://via.placeholder.com/600x400.png?text=Spotify+Player+Preview) |

---

## 🧑‍💻 Tech Stack

| Tool / Library | Purpose                         |
|----------------|---------------------------------|
| [Streamlit](https://streamlit.io)   | UI and frontend web app       |
| [DeepFace](https://github.com/serengil/deepface) | Facial emotion recognition    |
| [Spotipy](https://spotipy.readthedocs.io/) | Python client for Spotify Web API |
| [Pillow](https://pillow.readthedocs.io/en/stable/) | Image handling in Python      |

---

## 📦 Installation

### ✅ Clone the repository

```bash
git clone https://github.com/HarshR082/moodmusic-spotify-recommender.git
cd moodmusic-spotify-recommender
