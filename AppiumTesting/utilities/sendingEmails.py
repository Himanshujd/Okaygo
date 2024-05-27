import smtplib


server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("w2ajava@way2automation.com","Selenium@234")
server.sendmail("w2ajava@way2automation.com","trainer@way2automation.com","Hello how are you?")
server.quit()