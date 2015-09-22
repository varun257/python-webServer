#!/usr/bin/python
# Import socket module
import socket

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
s = socket.socket (socket.AF_INET, socket.SOCK_STREAM, proto=0)

# Assign a port number
serverPort = 8080

# Bind the socket to server address and server port
host = 'localhost' # Get local machine name
port = 8080                # Reserve a port for your service.
s.bind((host, port))
print "getting hostnmame"
print socket.gethostname()

# Listen to at most 1 connection at a time
s.listen(1)

# Server should be up and running and listening to the incoming connections
while True:
	print 'Ready to serve...'
	
	# Set up a new connection from the client
	connectionSocket, addr = s.accept() # c is client socket
	print "Got connection from", addr
	
	# If an exception occurs during the execution of try clause
	# the rest of the clause is skipped
	# If the exception type matches the word after except
	# the except clause is executed
	try:
		# Receive the request message from the client
		BUFFER_SIZE = 20
		message = connectionSocket.recv(BUFFER_SIZE)
		# Extract the path of the requested object from the message
		# The path is the second part of HTTP header, identified by [1]
		filename = message.split()[1]
		print 'filename'
		print filename
		# Because the extracted path of the HTTP request includes 
		# a character '\', we read the path from the second character 
		f = open(filename[1:])
		# Store the entire contenet of the requested file in a temporary buffer
		outputdata = f.read()
		# Send the HTTP response header line to the connection socket
		connectionSocket.send("<html><head></head><h1>My Home Page</h1></html>\r\n")

		# Send the content of the requested file to the connectionsn socket
		for i in range(0, len(outputdata)):  
			connectionSocket.send(outputdata[i])
		connectionSocket.close()

	except IOError:
		print 'io error'
		# Send HTTP response message for file not found
		connectionSocket.send("<html><head><h1>404</h1></head>")
		connectionSocket.send("<body><h2 style='color:red'>File not found</h2></body></html>\r\n")
		# Close the client connection socket
		connectionSocket.close()

#Close the Socket
s.close()

