import login
import app

f = open('isLog.txt', "r")
to_read = f.read(1024).split(',')
if to_read[0] == 'logged in':
    app.ChatApplication(to_read[1])
else:
    login.login()
