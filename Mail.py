import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("Sahil.kanthaliya@gmail.com", "8239939112")


    # message
message = "Your accuracy is less than 90% .Try again"


    # sending the mail
s.sendmail("Sahil.kanthaliya@gmail.com", message)


    # terminating the session
s.quit()
