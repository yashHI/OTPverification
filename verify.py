from tkinter import *
from tkinter import messagebox
import smtplib
import random

root = Tk()
root.title("OTP Verification")
root.geometry("550x350")

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_email(receiver_email, otp):
    sender_email = '#############3@gmail.com'  # Replace with your Gmail email address
    sender_password = '######'  # Replace with your Gmail app password

    subject = 'OTP Verification'
    body = f'Your OTP is: {otp}'
    message = f'Subject: {subject}\n\n{body}'

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message)
        print('OTP sent successfully.')
    except Exception as e:
        print(f'Error sending OTP: {e}')

def verify_otp():
    user_input_otp = otp_entry.get()
    if user_input_otp == otp:
        messagebox.showinfo('OTP Verification', 'OTP verification successful.')
    else:
        messagebox.showerror('OTP Verification', 'OTP verification failed.')

def open_otp_verification_window():
    global otp, otp_entry
    receiver_email = gmail_entry.get()

    if receiver_email == "":
        messagebox.showerror('Invalid data', 'Please enter a valid Gmail address.')
        return

    otp = generate_otp()

    send_otp_email(receiver_email, otp)

    otp_verification_window = Toplevel(root)
    otp_verification_window.title('OTP Verification')
    otp_verification_window.geometry('300x150')

    label = Label(otp_verification_window, text='Enter the OTP sent to your email:')
    label.pack(pady=10)

    otp_entry = Entry(otp_verification_window, show='*')
    otp_entry.pack(pady=10)

    verify_button = Button(otp_verification_window, text='Verify OTP', command=verify_otp)
    verify_button.pack(pady=10)

# GUI components
header = Frame(root)
header.place(x=5, y=5)

head = Label(root, text="OTP Verification", font=('comic sans', 20))
head.pack(fill=X)

panel = Frame(root)
panel.place(x=5, y=70)

gmail_label = Label(panel, text="Gmail", font=('comic sans', 20))
gmail_label.grid(row=0, column=1, padx=10, pady=5)

gmail_entry = Entry(panel, font=('comic sans', 15), width=25)
gmail_entry.grid(row=0, column=2, padx=10, pady=5)

start = Button(panel, text="Send OTP", font=('comic sans', 20), command=open_otp_verification_window)
start.grid(row=1, column=1, columnspan=2, padx=10, pady=5)

root.mainloop()
