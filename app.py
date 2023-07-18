from flask import Flask, request, render_template
from flask_uploads import UploadSet, configure_uploads, IMAGES
from itertools import chain
import pymssql

app = Flask(__name__)
app.secret_key = 'mew'

photos = UploadSet('photos', IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = 'static'
configure_uploads(app, photos)
# connect to database
conn = pymssql.connect(host='localhost',
                       user='wgz',
                       password='12012611',
                       database='HMS',
                       charset='utf8')

cursor = conn.cursor()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/MedicineInventory', methods=["GET", "POST"])
def MedicineInventory():
    if request.method == 'POST':
        MID = request.form['MID']
        Quantity = request.form['MQuantity']

        cursor.execute("SELECT Medicine_ID FROM Medicine")
        MedicineE = cursor.fetchall()
        if MID not in chain.from_iterable(MedicineE):
            return render_template('ModifyInventory.html', msg="MODIFICATION FAILED")

        sql = "update Medicine set Mquantity= %s where Medicine_ID = %s"
        val = (Quantity, MID)
        cursor.execute(sql, val)
        conn.commit()

    cursor.execute("SELECT * FROM Medicine")
    data = cursor.fetchall()
    return render_template('MedicineInventory.html', medicinedata=data)


@app.route('/ModifyInventory', methods=["GET", "POST"])
def ModifyInventory():
    return render_template('ModifyInventory.html')


@app.route('/SectionPatient', methods=["GET", "POST"])
def SectionPatient():
    cursor.execute(
        "select Ddept, count(*) from prescription a1, doctor a2 where a1.Doctor_ID = a2.Doctor_ID group by Ddept")
    data = cursor.fetchall()
    return render_template('SectionPatient.html', patientdata=data)


app.run(port=5000, debug=True)
