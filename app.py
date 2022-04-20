from flask import Flask, render_template
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="flask"
)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------


@app.route('/show', methods=['GET', 'POST'])
def item():
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `items`;")

    myresult = mycursor.fetchall()
    # ----------------------------
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `items_stock`;")

    myresult1 = mycursor.fetchall()
    # -------------------------------------
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `items_intransit`;")

    myresult2 = mycursor.fetchall()
    return render_template('show.html', myresult=myresult, myresult1=myresult1, myresult2=myresult2)

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------


@app.route('/banana', methods=['GET', 'POST'])
def banana():
    mycursor = mydb.cursor()

    mycursor.execute("SELECT SUM(kgs) FROM items_stock WHERE sku = 1005;")

    myresult = mycursor.fetchall()
    # -------------------------------------------------------------
    mycursor = mydb.cursor()
    mycursor.execute("SELECT SUM(kgs) FROM items_intransit WHERE sku = 1005;")

    myresult1 = mycursor.fetchall()

    return render_template('banana.html', myresult=myresult, myresult1=myresult1)

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------


@app.route('/aloevera', methods=['GET', 'POST'])
def aloevera():
    mycursor = mydb.cursor()

    mycursor.execute("SELECT SUM(kgs) FROM items_stock WHERE sku = 1001;")

    myresult = mycursor.fetchall()
    # -------------------------------------------------------------
    mycursor = mydb.cursor()
    mycursor.execute("SELECT SUM(kgs) FROM items_intransit WHERE sku = 1001;")

    myresult1 = mycursor.fetchall()

    return render_template('aloevera.html', myresult=myresult, myresult1=myresult1)

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------


@app.route('/apple', methods=['GET', 'POST'])
def apple():
    mycursor = mydb.cursor()

    mycursor.execute("SELECT SUM(kgs) FROM items_stock WHERE sku = 1003;")

    myresult = mycursor.fetchall()
    # -------------------------------------------------------------
    mycursor = mydb.cursor()
    mycursor.execute("SELECT SUM(kgs) FROM items_intransit WHERE sku = 1003;")

    myresult1 = mycursor.fetchall()

    return render_template('apple.html', myresult=myresult, myresult1=myresult1)

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------


@app.route('/blueberry', methods=['GET', 'POST'])
def blueberry():
    mycursor = mydb.cursor()

    mycursor.execute("SELECT SUM(kgs) FROM items_stock WHERE sku = 1007;")

    myresult = mycursor.fetchall()
    # -------------------------------------------------------------
    mycursor = mydb.cursor()
    mycursor.execute("SELECT SUM(kgs) FROM items_intransit WHERE sku = 1007;")

    myresult1 = mycursor.fetchall()

    return render_template('blueberry.html', myresult=myresult, myresult1=myresult1)

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------


@app.route('/cheerysweet', methods=['GET', 'POST'])
def cheerysweet():
    mycursor = mydb.cursor()

    mycursor.execute("SELECT SUM(kgs) FROM items_stock WHERE sku = 1009;")

    myresult = mycursor.fetchall()
    # -------------------------------------------------------------
    mycursor = mydb.cursor()
    mycursor.execute("SELECT SUM(kgs) FROM items_intransit WHERE sku = 1009;")

    myresult1 = mycursor.fetchall()

    return render_template('cheerysweet.html', myresult=myresult, myresult1=myresult1)

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------


@app.route('/cherrytart', methods=['GET', 'POST'])
def cherrytart():
    mycursor = mydb.cursor()

    mycursor.execute("SELECT SUM(kgs) FROM items_stock WHERE sku = 1011;")

    myresult = mycursor.fetchall()
    # -------------------------------------------------------------
    mycursor = mydb.cursor()
    mycursor.execute("SELECT SUM(kgs) FROM items_intransit WHERE sku = 1011;")

    myresult1 = mycursor.fetchall()

    return render_template('cherrytart.html', myresult=myresult, myresult1=myresult1)


if __name__ == "__main__":
    app.run(debug=True, port=4040)
