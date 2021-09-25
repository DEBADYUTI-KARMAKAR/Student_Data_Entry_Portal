#!C:\Users\Adimin\AppData\Local\Programs\Python\Python37\python.exe
import mysql.connector,cgi,cgitb
print('Content-Type:text/html\r\n\r\n')
print("<!DOCTYPE html>")
print("<html><head><title>Welcome</title>")
print("<meta name = 'viewport' content = 'width=device-width,initial-scale=1.0'/>")
print(" <link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css'>")
print("<script src='https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js'></script>")
print("<script src='https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js'></script>")
print("</head>")
print("<body>")
cgitb.enable()

form = cgi.FieldStorage()

id = int(form.getvalue('id'))

con = mysql.connector.connect(
	host='localhost',
	database='pydb',
	user='root',
	password=''
	)
cursor = con.cursor()
cursor.execute("select * from pytb where id = '%d'"%(id))
data = cursor.fetchall()

print("<h1> Update Records : </h1>")
print("<form class='container' name='frm' method='post' action='update.cgi'>")

for d in data:
	print("Name:<input type='text' name='t1' value='{}' class='form-control'/><br/>".format(d[1]))
	print("Age:<input type='text' name='t2' value='{}' class='form-control'/><br/>".format(d[2]))
	print("Gender:<input type='text' name='t3' value='{}' class='form-control'/><br/>".format(d[3]))
	print("City:<input type='text' name='t4' value='{}' class='form-control'/><br/>".format(d[4]))
	print("Email:<input type='text' name='t5' value='{}' class='form-control'/><br/>".format(d[5]))
	print("Phone:<input type='text' name='t6' value='{}' class='form-control'/><br/>".format(d[6]))
	print("<input type='hidden' name='hid' value='{}'/>".format(d[0]))

print("<button type='submit' class='btn btn-success'>Update</button>")
print("</form>")
print("</body>")
print("</html>")
con.close()