import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("Sahil.kanthaliya@gmail.com", "8239939112")


    # message
message_success = "Achieved your desired accuracy without tweeking . Congrats "


    # sending the mail
s.sendmail("Sahil.kanthaliya@gmail.com", message_success)


    # terminating the session
s.quit()
