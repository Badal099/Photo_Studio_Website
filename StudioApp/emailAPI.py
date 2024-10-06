def sendEMAIL(email,name,phone,message):
    import smtplib 
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
	
    me = "badalchouhan295@gmail.com"
    you = email

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Confirmation mail by PhotoShop"
    msg['From'] = me
    msg['To'] = you

    html = """<html>
  					<head></head>
  					<body>
    					<h1>Welcome to PhotoShop</h1>
    					<h3>Hello! This is """+name+""" .</h3>
    					<p>"""+message+"""</p>
    					<h3>"""+phone+"""</h3> 
                        <p>This is our Contact. Please Call, if Any Query.</p>
                        <p>Otherwise,Please make the Payment. Our Account details is - </p>		
  					</body>
				</html>
	"""
	
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login("badalchouhan295@gmail.com", "xxxxxxxxx") 
	
    part2 = MIMEText(html, 'html')

    msg.attach(part2)
	
    s.sendmail(me,you,str(msg)) 
    s.quit() 
    print("mail send successfully....")
