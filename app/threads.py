from django.core.mail import send_mail
from django.conf import settings
import threading


class send_contact_email(threading.Thread):
    def __init__(self, em, nm):
        self.em = em
        self.nm = nm
        threading.Thread.__init__(self)
    def run(self):
        try:
            subject = "Thanks for filling up the Contact Us Form."
            message = f"Hay {self.nm} !\nThanks for filling up the Contact Form.\nWe will reachout to you as soon as possible."
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject , message ,email_from ,[self.em])
        except Exception as e:
            print(e)


class send_subject_change_email(threading.Thread):
    def __init__(self, email_list):
        self.email_list = email_list
        threading.Thread.__init__(self)
    def run(self):
        try:
            subject = "Elective Subject Chnage Request"
            message = f"There is a request the change the elective subject. Kindly check your dashboard."
            email_from = settings.EMAIL_HOST_USER
            print("Email send started")
            send_mail(subject , message ,email_from ,self.email_list)
            print("Email send finished")
        except Exception as e:
            print(e)
