
# 📈 Alpha Terminal

Alpha Terminal is a modern financial analytics dashboard built with **Django** and **Tailwind CSS**. It is designed for investors to track real-time stock data, analyze financial health metrics (Altman Z-Score, Volatility), and read the latest market news.

## 🚀 Features

* **Live Dashboard:** Real-time tracking of Top Gainers, Losers, and Key Indices.
* **Stock Analytics:** Deep dive into financial stability with Z-Score and Debt/Equity analysis.
* **News Feed:** Curated market headlines powered by the NewsAPI.
* **Responsive Design:** Fully responsive UI built with Tailwind CSS.
* **Secure Architecture:** API keys are hidden on the backend (Proxy Pattern).

## 🛠️ Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML5, Tailwind CSS, JavaScript (Vanilla)
* **Data:** NewsAPI, Custom Mock Data Engine

## ⚙️ Installation Guide

Follow these steps to run the project locally:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/sohamGGs/alpha_terminal.git](https://github.com/sohamGGs/alpha_terminal.git)
    cd alpha_terminal
    ```

2.  **Create a Virtual Environment:**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run Migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Start the Server:**
    ```bash
    python manage.py runserver
    ```

6.  **Access the App:**
    Open `http://127.0.0.1:8000` in your browser.

## 🔑 Configuration
To use the News feature, you must add your API Key in `core/views.py`:
```python
api_key = 'YOUR_NEWSAPI_KEY'
