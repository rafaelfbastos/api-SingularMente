import smtplib
import email.message
import os


class Email:
    def __init__(self, nome, mail, mensagem):
        self.corpo = f"""
                    <p> Nova mensagem enviada no Site Singularmente </p>
                    <p> Enviada por: {nome} </p>
                    <p>Contato: {mail} </p>
                    <hr>
                    <p>{mensagem}</p>
                     """

        self.msg = email.message.Message()
        self.msg['Subject'] = "Nova mensagem recebida"
        self.msg['From'] = os.environ["EMAIL"]
        self.msg['To'] = os.environ["EMAIL"]
        self.password = os.environ["EMAIL_PASSWORD"]
        self.msg.add_header('Content-Type', 'text/html')
        self.msg.set_payload(self.corpo)

        corpo2 = f"""
                            <p> Obrigado pelo contato </p>
                            <p> Sua mensagem foi recebida: </p>
                            <p>Att</p>
                            <p>SingularMente</p>
                             """

        self.msg2 = email.message.Message()
        self.msg2['Subject'] = "Obrigodo pelo contato"
        self.msg2['From'] = os.environ["EMAIL"]
        self.msg2['To'] = f'{mail}'
        self.password = os.environ["EMAIL_PASSWORD"]
        self.msg2.add_header('Content-Type', 'text/html')
        self.msg2.set_payload(corpo2)

    def enviar(self):
        try:
            s = smtplib.SMTP('smtp.gmail.com: 587')
            s.starttls()
            s.login(self.msg['From'], self.password)
            s.sendmail(self.msg['From'], [self.msg['To']],
                       self.msg.as_string().encode("utf-8"))
            s.sendmail(self.msg2['From'], [self.msg2['To']],
                       self.msg2.as_string().encode("utf-8"))
            s.quit()
            return True
        except Exception:
            return False
