from flask import render_template, request, redirect, url_for
from app import app

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
        "status": "Offline",
        "ph": "No data",
        "suhu": "No Data",
    },
]
resource_data = [
    {
        "image_path": "image/r1.png",
        "title": "Tips Membuat Kolam Ikan Konsumsi di Pekarangan",
    },
    {
        "image_path": "image/r2.png",
        "title": "Cara Budidaya Ternak Ikan Mujair Paling Lengkap dan Mudah",
    },
    {
        "image_path": "image/r3.png",
        "title": "Jenis-Jenis Kolam Yang Sehat Untuk Ikan Ternak",
    },
]
laporan_data = [
    {
        "nama": "Kolam 1A",
        "jenis_ikan": "Mujair",
        "kualitas_air_avg": "Jernih",
    },
    {
        "nama": "Kolam 1B",
        "jenis_ikan": "Gabus",
        "kualitas_air_avg": "Jernih",
    },
    {
        "nama": "Kolam 1C",
        "jenis_ikan": "Lele",
        "kualitas_air_avg": "Jernih",
    },
    {
        "nama": "Kolam 2A",
        "jenis_ikan": "Mujair",
        "kualitas_air_avg": "Jernih",
    },
    {
        "nama": "Kolam 2B",
        "jenis_ikan": "Gabus",
        "kualitas_air_avg": "No Data",
    },
]


notification_data = [
    {
        "nama": "Kolam 1A",
        "kualitas_air": "Keruh",
        "more_information": "Oportet uti solum de actibus prosequtione et fugam, haec leniter et blandus et reservato.",
    },
    {
        "nama": "Kolam 1A",
        "kualitas_air": "Keruh",
        "more_information": "Oportet uti solum de actibus prosequtione et fugam, haec leniter et blandus et reservato.",
    },
    {
        "nama": "Kolam 1A",
        "kualitas_air": "Keruh",
        "more_information": "Oportet uti solum de actibus prosequtione et fugam, haec leniter et blandus et reservato.",
    },
    {
        "nama": "Kolam 1A",
        "kualitas_air": "Keruh",
        "more_information": "Oportet uti solum de actibus prosequtione et fugam, haec leniter et blandus et reservato.",
    },
    {
        "nama": "Kolam 1A",
        "kualitas_air": "Keruh",
        "more_information": "Oportet uti solum de actibus prosequtione et fugam, haec leniter et blandus et reservato.",
    },
]


@app.context_processor
def inject_notification_data():
    return dict(notification_data=notification_data)


@app.route("/")
def index():
    return render_template(
        "dashboard.html", kolam_data=kolam_data, resource_data=resource_data
    )


@app.route("/article")
def article():
    return render_template("article.html")


@app.route("/kolam/<name>")
def kolam(name):
    return render_template("kolam.html", name=name)


@app.route("/laporan")
def laporan():
    return render_template("laporan.html", laporan_data=laporan_data)


@app.route("/laporan-detail/<name>")
def detail_kolam(name):
    return render_template("detail_kolam.html", name=name)
