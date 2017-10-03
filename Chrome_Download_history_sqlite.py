import csv
import os
import sqlite3 as sql
import datetime

def getFiletime(dtms):
	if(dtms == 0):
		return (0)
	else:
		seconds, micros = divmod(dtms, 1000000)
		days, seconds = divmod(seconds, 86400)
		return str(datetime.datetime(1601, 1, 1) + (datetime.timedelta(days, seconds, micros)))

def State(state):
	if(state == 0):
		msg = str(('Download in progress'))
		return msg
	elif(state == 1):
		msg = str(('Download completed'))
		return msg
	elif(state == 2):
		msg = str(('Download cancelled'))
		return msg
	elif(state == 3):
		msg = str(('Download interrupted'))
		return msg
	elif(state == 4):
		msg = str(('Maximum download state reached'))
		return msg

def Danger_Type(danger):
	if(danger == 0):
		msg = str(('Not dangerous'))
		return msg
	elif(danger == 1):
		msg = str(('File dangerous to system (*.pdf)'))
		return msg
	elif(danger == 2):
		msg = str(('File URLs is malicious'))
		return msg
	elif(danger == 3):
		msg = str(('File content is malicious'))
		return msg
	elif(danger == 4):
		msg = str(('Potentially dangerous (*.exe)'))
		return msg
	elif(danger == 5):
		msg = str(('Unknown/Uncommon content'))
		return msg
	elif(danger == 6):
		msg = str(('Dangerous, used ignore it'))
		return msg
	elif(danger == 7):
		msg = str(('File from dangerous host'))
		return msg
	elif(danger == 8):
		msg = str(('Dangerous to browser'))
		return msg
	elif(danger == 9):
		msg = str(('Maximum (internal)'))
		return msg

def Interrupt_Reason(reason):
	if(reason == 0):
		msg = str(('Not interrupted'))
		return msg
	elif(reason == 1):
		msg = str(('Generic file operation failure'))
		return msg
	elif(reason == 2):
		msg = str(('Access to file denied'))
		return msg
	elif(reason == 3):
		msg = str(('Not enough free space'))
		return msg
	elif(reason == 5):
		msg = str(('File name is too long'))
		return msg
	elif(reason == 6):
		msg = str(('File is too large for file system'))
		return msg
	elif(reason == 7):
		msg = str(('Virus infected file'))
		return msg
	elif(reason == 10):
		msg = str(('File in use (transient error)'))
		return msg
	elif(reason == 11):
		msg = str(('File blocked by local policy'))
		return msg
	elif(reason == 12):
		msg = str(('File security check failed'))
		return msg
	elif(reason == 13):
		msg = str(('Download revive error'))
		return msg
	elif(reason == 20):
		msg = str(('Generic network failure'))
		return msg
	elif(reason == 21):
		msg = str(('Network operation timed out'))
		return msg
	elif(reason == 22):
		msg = str(('Connection lost'))
		return msg
	elif(reason == 23):
		msg = str(('Server has gone offline'))
		return msg
	elif(reason == 24):
		msg = str(('Network request invalid'))
		return msg
	elif(reason == 30):
		msg = str((' Server operation failed'))
		return msg
	elif(reason == 31):
		msg = str((' Unsupported range request'))
		return msg
	elif(reason == 32):
		msg = str(('Request does not meet precondition'))
		return msg
	elif(reason == 33):
		msg = str(('Server does not have requested data'))
		return msg
	elif(reason == 40):
		msg = str(('User cancelled download'))
		return msg
	elif(reason == 41):
		msg = str(('User shut down the browser'))
		return msg
	elif(reason == 50):
		msg = str(('Browser crashed (internal only)'))
		return msg
userhome = os.path.expanduser('~')          

# USER_NAME = os.path.split(userhome)[-1]  

conn = sql.connect(r"C:\Users\gayou\AppData\Local\Google\Chrome\User Data\Default\History")
cur = conn.cursor()
cur.execute("SELECT * FROM downloads")

rows = cur.fetchall()
for num,row in enumerate(rows):
	print ('Downloads list [' + str(num + 1) + ']' + '\n''GUID ' +  ': ' + (row[1]) 
		+ '\n' + 'Current_Path: ' + (row[2]) + '\n' + 'Target_Path: ' + (row[3])
		+ '\n' + 'Start_Download_Time: ' + getFiletime((row[4])) + '\n' + 'Recieved_Bytes: ' + str(row[5]) + ' Bytes'
		+ '\n' + 'Total_Bytes: ' + str(row[6]) + ' Bytes' + '\n' + 'State: ' + State((row[7]))
		+ '\n' + 'Danger_Type: ' + Danger_Type(row[8]) + '\n' + 'Interrupt_Reason: ' + str(Interrupt_Reason((row[9])))
		+ '\n' + 'URL: ' , (row[15]) + '\n' + 'Site_lastmodified_Time: ' + (row[23])
		+ '\n' + 'File_Type: ' + (row[24]))
	print ('-------------------------------------------------------------------------------------')
conn.close()

#username 변경 가능하게 해야함.