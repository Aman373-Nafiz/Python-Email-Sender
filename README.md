# 📧 Python Email Sender  

A simple Python project that demonstrates how to send emails using the built-in **SMTP (Simple Mail Transfer Protocol)** library.  
This project allows you to send automated emails directly from Python without needing external packages.  

---

## 🚀 Features  
- Send plain text emails  
- Use Python’s built-in `smtplib` (no external dependency)  
- Secure authentication with your email credentials  
- Can be extended to send HTML emails, attachments, or bulk emails  

---

## 🛠️ Technologies Used  
- **Python 3.x**  
- **smtplib** (built-in Python library)  
- **email.mime** (for email formatting)  

---

## 📂 Project Structure  
Email-Sender/
│── email_sender.py # Main script to send email
│── README.md # Documentation


---

## ⚙️ How It Works  

1. Connects to an SMTP server (e.g., Gmail: `smtp.gmail.com`).  
2. Logs in using your email and app password.  
3. Creates an email message (subject + body).  
4. Sends it to the recipient’s email address.  

---

## ▶️ Usage  

1. Clone the repo:  
   ```bash
   git clone https://github.com/your-username/email-sender.git
   cd email-sender
2. Open email_sender.py and update with your credentials:
sender_email = "your_email@gmail.com"
sender_password = "your_app_password"
receiver_email = "recipient@gmail.com"
3. Run the Script:
python email_sender.py

