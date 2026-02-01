Here is the consolidated, formatted **README.md** file containing all the data you provided.

---

```markdown
# 🎬 Movie Recommendation System

A **Streamlit-based Movie Recommendation System** that recommends the **top 5 similar movies** based on user selection and displays **movie posters using the TMDB API**.

---

## 🚀 Live Application
🔗 Live App: [Movie Champ](https://movie-champ-ecwm3auxjtsj58dmqxix4p.streamlit.app/)


---

## ✨ Features
* **Content-based movie recommendation**: Uses similarity scores to find relevant films.
* **Visual Suggestions**: Displays the top 5 similar movie suggestions with posters.
* **Real-time Posters**: Fetches high-quality posters directly via the TMDB API.
* **Fast UI**: Built with Streamlit for a smooth and interactive user experience.
* **Secure API Handling**: Uses environment variables for API token security.
* **Cloud Ready**: Configured for easy deployment on platforms like Streamlit Cloud or Heroku.

---

## 🛠️ Tech Stack
* **Language**: Python
* **Web Framework**: Streamlit
* **Data Analysis**: Pandas
* **Machine Learning**: Scikit-learn
* **API**: TMDB (The Movie Database)
* **Serialization**: Pickle

---

## 📁 Project Structure
```text
movie-recommender/
│
├── app.py              # Main Streamlit application script
├── movies_dict.pkl     # Processed movie data dictionary
├── similarity.pkl      # Pre-computed similarity matrix
├── requirements.txt    # List of Python dependencies
├── setup.sh            # Configuration script for deployment
├── Procfile            # Process file for Heroku/Cloud deployment
├── .gitignore          # Files to be excluded from version control
└── README.md           # Project documentation

```

---

## ⚙️ Run the Project Locally

### 1️⃣ Clone the Repository

```bash
git clone [https://github.com/USERNAME/movie-recommender.git](https://github.com/USERNAME/movie-recommender.git)
cd movie-recommender

```

### 2️⃣ Create & Activate Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate

```

**Mac / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate

```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt

```
# 🎬 Movie Champ – Movie Recommendation System

Movie Champ is a content-based movie recommendation web application built using **Python** and **Streamlit**.  
It recommends similar movies based on user selection using cosine similarity.

---

## 🚀 Live Demo
👉 https://movie-champ-dbwheczuwcpnfluamtzyxo.streamlit.app/

---

## 🛠 Tech Stack

- Python 3.10+
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Pickle
- python-dotenv

---

## 📂 Project Structure

movie-champ/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── movies_dict.pkl # (NOT pushed to GitHub)
├── similarity.pkl # (NOT pushed to GitHub)
└── .env # (Local only)


---

## ⚙️ Local Setup (Run on Your System)

### 1️⃣ Clone Repository
```bash
git clone https://github.com/IshwariShinde8772/Movie-champ.git
cd Movie-champ
2️⃣ Create Virtual Environment
python -m venv .venv
Activate it:

Windows

.venv\Scripts\activate
Mac / Linux

source .venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Environment Variables (Token Setup)
Create a .env file:

API_TOKEN=your_api_token_here
In app.py:

from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
5️⃣ Run the App
streamlit run app.py

---

## 🔐 TMDB API Token Setup (IMPORTANT)

This project uses a **TMDB Bearer Token** to fetch movie posters.

### 🔑 Get TMDB Token

1. Visit: [https://www.themoviedb.org/settings/api](https://www.themoviedb.org/settings/api)
2. Copy your **API Read Access Token (Bearer Token)**.

### 4️⃣ Set Environment Variable

You must set your token in your environment for the app to function.

**Windows (Command Prompt):**

```cmd
setx TMDB_TOKEN "your_tmdb_bearer_token"

```

*Note: Restart your terminal after running this command.*

**PowerShell:**

```powershell
$env:TMDB_TOKEN="your_tmdb_bearer_token"

```

**Mac / Linux:**

```bash
export TMDB_TOKEN="your_tmdb_bearer_token"

```

#### 🔒 Optional (Recommended): .env File

For cleaner local development, create a `.env` file in the project root:

```text
TMDB_TOKEN=your_tmdb_bearer_token

```

Then, install `python-dotenv` and add these lines to the top of your `app.py`:

```python
from dotenv import load_dotenv
import os
load_dotenv()
tmdb_token = os.getenv("TMDB_TOKEN")

```

*Ensure `.env` is added to your `.gitignore` to keep your token private.*

---

### 5️⃣ Run the Application

```bash
streamlit run app.py

```

The app will be available at: **http://localhost:8501**

```

Would you like me to help you write the `requirements.txt` file or the `app.py` logic to handle that TMDB token?

```