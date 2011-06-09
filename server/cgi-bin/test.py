#!/usr/bin/python

#the first cgi program

import cgi
  
def main():
        print "Content-type: text/html\n"
	print "<html> <head>\n";
	print "<title>Hello, world!</title>";
	print "</head>\n";
	print "<body>\n";
	print "<h1>Hello, world!</h1>\n";
	print "</body> </html>\n";
#	print "Content-type: text/html\n"
#	form = cgi.FieldStorage()	# parse query
#	if form.has_key("firstname") and form["firstname"].value != "":
#		print "<h1>Hello", form["firstname"].value, "</h1>"
#	else:
#		print "<h1>Error! Please enter first name.</h1>"

main()

