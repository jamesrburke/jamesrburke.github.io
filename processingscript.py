import cgi
form = cgi.FieldStorage()
x = form.getvalue('number')
x = x*2