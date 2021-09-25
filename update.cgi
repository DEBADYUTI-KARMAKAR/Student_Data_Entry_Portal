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

con = mysql.connector.connect(
	host = 'localhost',
	database = 'pydb',
	user = 'root',
	password = ''
	)
form = cgi.FieldStorage()

cname = form.getvalue('t1')
age = int(form.getvalue('t2'))
gender = form.getvalue('t3')
city = form.getvalue('t4')
email = form.getvalue('t5')
phone = form.getvalue('t6')

id = int(form.getvalue('hid'))

cursor = con.cursor()
cursor.execute("update pytb set cname='%s',age='%d',gender='%s',city='%s',email='%s',phone='%s' where id = '%d'"%(cname,age,gender,city,email,phone,id))

r=cursor.rowcount

if(r==1):
	print("<meta http-equiv='refresh' content='0, view.cgi'/>")
else :
	print("Unable to update !!")
con.commit()
con.close()

print("</body>")
print("</html>")