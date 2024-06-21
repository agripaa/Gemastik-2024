from flask import render_template, request, redirect, url_for
from app import app


@app.route("/")
def index():
    kolam_data = [
        {
            "nama": "Kolam 1A",
            "jenis_ikan": "Mujair",
            "kualitas_air": "Jernih",
            "status": "Online",
            "ph": "Normal",
            "suhu": "Normal",
        },
        {
            "nama": "Kolam 1B",
            "jenis_ikan": "Gabus",
            "kualitas_air": "Jernih",
            "status": "Online",
            "ph": "Normal",
            "suhu": "Normal",
        },
        {
            "nama": "Kolam 1C",
            "jenis_ikan": "Lele",
            "kualitas_air": "Jernih",
            "status": "Online",
            "ph": "Normal",
            "suhu": "Normal",
        },
        {
            "nama": "Kolam 2A",
            "jenis_ikan": "Mujair",
            "kualitas_air": "Jernih",
            "status": "Online",
            "ph": "Normal",
            "suhu": "Normal",
        },
        {
            "nama": "Kolam 2A",
            "jenis_ikan": "Gabus",
            "kualitas_air": "No data",
            "status": "offline",
            "ph": "No data",
            "suhu": "No Data",
        },
    ]
    return render_template("dashboard.html", kolam_data=kolam_data)
