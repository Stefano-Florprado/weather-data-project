Weather Data Pipeline

📌 Project Overview

This project is an automated weather data pipeline built in Python using the OpenWeather API.

The application periodically collects real-time weather data for multiple cities, stores the data in a SQLite database, and exports it into a CSV file for further analysis.

The goal of the project was to learn the fundamentals of:

* API integration
* HTTP requests
* JSON data extraction
* SQL databases
* ETL pipelines
* automation in Python

---

Features

* Real-time weather data collection
* Multiple city support
* SQLite database storage
* CSV export
* Automated execution with scheduler
* SQL analytical queries
* Modular project structure

---

Tech Stack

* Python
* SQLite
* Pandas
* Requests
* OpenWeather API
* Python-dotenv

---

Pipeline Workflow

The pipeline follows a basic ETL architecture:

1. **Extract**
   * Weather data retrieved from OpenWeather API
2. **Transform**
   * JSON response parsed into structured Python dictionaries
3. **Load**
   * Data stored in:
     * SQLite database
     * CSV file

The pipeline automatically repeats every 60 seconds.

---

Project Structure

weather-data-project/
│
├── main.py
├── db.py
├── csv_utils.py
├── meteo.db
├── meteo.csv
├── .env
├── .gitignore
└── README.md

---

Environment Variables

Create a `.env` file:

```env
API_KEY=your_openweather_api_key
```

---

Database Schema

The SQLite database contains the following table:

| Column      | Type    |
| ----------- | ------- |
| id          | INTEGER |
| citta       | TEXT    |
| temperatura | REAL    |
| umidita     | REAL    |
| meteo       | TEXT    |
| vento       | REAL    |
| data        | TEXT    |

---

📈 Future Improvements

* Logging system
* Dashboard with Streamlit
* Docker containerization
* Cloud deployment
* Historical weather analysis

---

🎯 What I Learned

Through this project I learned:

* how APIs work
* how to send HTTP requests
* JSON parsing
* SQL fundamentals
* modular Python programming
* ETL pipeline basics
* data persistence and automation

---

👨‍💻 Author

Zenon Stefano Flor Prado
