# Weather ETL Analytics

## Overview

**Weather ETL Analytics** is an ETL (Extract, Transform, Load) pipeline that fetches weather data from the OpenWeather API, filters it based on conditions such as rain or clouds, and stores the filtered data into a PostgreSQL database for further analysis.

The project is designed to be extendable, with the goal of automating the ETL process using **Apache Airflow** for scheduling and orchestration.

---

## Key Features

- **Data Extraction**: Retrieves weather data from the OpenWeather API.
- **Data Filtering**: Filters weather data based on specific conditions such as rain or clouds and a temperature threshold of >20°C.
- **Data Loading**: Stores the filtered data in a PostgreSQL database.
- **Automation**: Uses Apache Airflow to automate the process, ensuring regular and consistent data updates.

---

## Project Structure


---

## Prerequisites

Before running the project, ensure you have the following installed:

1. **Python 3.x** (recommended version: 3.7 or higher)
2. **PostgreSQL** (set up and running on localhost or a cloud instance)
3. **Airflow** (optional, if you want to automate the process)
4. **OpenWeather API Key** (sign up at [OpenWeather](https://openweathermap.org/api) to get your key)

---

## Setup Instructions

### Step 1: Install Dependencies

1. Create and activate a virtual environment:

   ```bash
   python -m venv venv
