# Backend Setup

## Prerequisites

* Python
* pip
* Neon PostgreSQL Database

---


## Install Dependencies

```bash
pip install -r requirements.txt
```

Required packages:

```txt
Flask
Flask-SQLAlchemy
psycopg2-binary
python-dotenv
Flask-Cors
requests
flask-limiter
```

---

## Environment Variables

Create a `.env` file in the project root and add your Neon database connection string:

```env
DATABASE_URL=your_neon_connection_string
```

Example:

```env
DATABASE_URL=postgresql://username:password@ep-xxxx.ap-southeast-1.aws.neon.tech/database_name?sslmode=require
```

---

## Run the Application

```bash
python app.py
```

The API will start on:

```txt
http://localhost:5000
```

---

## Rate Limiting

Default API limit:

```txt
60 requests per minute per IP address
```
