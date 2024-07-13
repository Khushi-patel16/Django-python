# from django.core.mail.backends.smtp import EmailBackend

# class CustomEmailBackend(EmailBackend):
#     def _send(self, email_message):
#         try:
#             self.connection.starttls()
#         except TypeError:
#             # Handle the TypeError by passing only necessary arguments
#             self.connection.starttls()
#         return super()._send(email_message)

# from django.core.mail.backends.smtp import EmailBackend
# import smtplib
# 
# class CustomEmailBackend(EmailBackend):
    # def open(self):
        # """
        # Ensure the connection is open. If it is not, then open it.
        # """
        # if self.connection:
            # return False
# 
        # try:
            # self.connection = self.get_connection()
            # self.connection.ehlo()
# 
            # if self.use_tls:
                # self.connection.starttls()  # Ensure no arguments are passed here
                # self.connection.ehlo()
# 
            # if self.username and self.password:
                # self.connection.login(self.username, self.password)
            # return True
        # except smtplib.SMTPException:
            # if not self.fail_silently:
                # raise
            # return False
# 
    # def _send(self, email_message):
        # try:
            # self.open()
            # return super()._send(email_message)
        # finally:
            # self.close()
# 


from django.core.mail.backends.smtp import EmailBackend
import smtplib

class CustomEmailBackend(EmailBackend):
    def open(self):
        """
        Ensure the connection is open. If it is not, then open it.
        """
        if self.connection:
            return False

        try:
            self.connection = smtplib.SMTP(self.host, self.port)
            self.connection.ehlo()

            if self.use_tls:
                self.connection.starttls()  # Ensure no arguments are passed here
                self.connection.ehlo()

            if self.username and self.password:
                self.connection.login(self.username, self.password)
            return True
        except smtplib.SMTPException:
            if not self.fail_silently:
                raise
            return False

    def close(self):
        """
        Close the connection to the email server.
        """
        if self.connection is None:
            return
        try:
            self.connection.quit()
        except smtplib.SMTPException:
            if not self.fail_silently:
                raise
        finally:
            self.connection = None

    def _send(self, email_message):
        try:
            self.open()
            return super()._send(email_message)
        finally:
            self.close()
