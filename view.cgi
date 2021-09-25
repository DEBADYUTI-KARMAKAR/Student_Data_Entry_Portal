#!C:\Users\Adimin\AppData\Local\Programs\Python\Python37\python.exe
import mysql.connector
print('Content-Type:text/html\r\n\r\n')
con = mysql.connector.connect(
		host = 'localhost',
		user = 'root',
		database = 'pydb',
		password = ''
	)
cursor = con.cursor()

cursor.execute('select * from pytb')

data = cursor.fetchall()

print("<!DOCTYPE html>")
print("<html><head><title>Welcome</title>")
print("<meta name = 'viewport' content = 'width=device-width,initial-scale=1.0'/>")
print(" <link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css'>")
print("<script src='https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js'></script>")
print("<script src='https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js'></script>")
print("</head>")
print("<body>")
print("<table class='table table-borderd table-hover'><tr>")
print("<th>Action</th>")
print("<th>Name</th>")
print("<th>Age</th>")
print("<th>Gender</th>")
print("<th>City</th>")
print("<th>Email</th>")
print("<th>Phone</th>")


for d in data:
	print("<tr>")
	print("<td><a href='edit.cgi?id={}'class='btn btn-primary'>Edit</a>&nbsp;<a href='delete.cgi?id={}'class='btn btn-danger'>Delete</a></td>".format(d[0],d[0]))
	print("<td>{}</td>".format(d[1]))
	print("<td>{}</td>".format(d[2]))
	print("<td>{}</td>".format(d[3]))
	print("<td>{}</td>".format(d[4]))
	print("<td>{}</td>".format(d[5]))
	print("<td>{}</td>".format(d[6]))
	print("</tr>")

print("</table>")
print("</body>")
print("</html>")