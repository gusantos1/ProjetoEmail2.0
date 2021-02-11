import sys
import json
import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from janelaemail import *
from janelaassinatura import *
from janelacandidatos import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox

lista_candidatos = []
lista_assinatura = []

class Principal(QMainWindow, Ui_MainWindow):
    """Janela principal do programa."""
    def __init__(self):
        super().__init__(parent=None)
        super().setupUi(self)

        #Cliques
        self.btn_json.clicked.connect(self.abrir_json)
        self.rdbtn_gmail.clicked.connect(self.radio_gmail)
        self.rdbtn_hotmail.clicked.connect(self.radio_hotmail)
        self.rdbtn_yahoo.clicked.connect(self.radio_yahoo)
        self.rdbtn_outros.clicked.connect(self.radio_outros)
        self.btn_assinatura.clicked.connect(self.abrir_assinatura)
        self.btn_enviar.clicked.connect(self.enviar)
        self.btn_candidatos.clicked.connect(self.candidatos)

        #Config user
        self.candidados_reprovados = None
        self.user_host = None
        self.user_port = None
        self.btn_enviar.setToolTip('Enviar para todos os candidatos.')
        self.btn_candidatos.setToolTip('Mostrar todos os candidatos.')

        # Tela texto
        self.textEdit.setToolTip('Escreva seu email.')
        self.textEdit.setAcceptRichText(False)  # Retira formatações de texto colados.


    def abrir_assinatura(self):
        """Abre a tela de assinatura para inserir uma assinatura digital."""
        self.Assinatura = Assinatura()
        self.Assinatura.show()

    def abrir_json(self):
        """Função que abre dados dos candidatos em json."""
        arquivo = QFileDialog.getOpenFileName(self,
                                              caption='Abrir arquivo json',
                                              directory=QtCore.QDir.currentPath(),
                                              filter='json(*.json)')
        try:
            dir_arquivo = arquivo[0]
            self.diretorio_json.setText(dir_arquivo)
            with open(dir_arquivo, 'r') as reprovados:
                global lista_candidatos
                self.candidados_reprovados = json.load(reprovados)
                lista_candidatos.append(self.candidados_reprovados)
        except:
            pass

    #Configuração dos Radio Buttons
    def radio_gmail(self):
        #Setter no btn radio gmail
        self.le_host.setText('smtp.gmail.com')
        self.sb_port.setValue(587)
        #Getter no LineEdit
        self.user_host = self.le_host.text()
        self.user_port = self.sb_port.text()

    def radio_hotmail(self):
        # Setter no btn radio gmail
        self.le_host.setText('smtp.live.com')
        self.sb_port.setValue(465)
        # Getter no LineEdit
        self.user_host = self.le_host.text()
        self.user_port = self.sb_port.text()

    def radio_yahoo(self):
        # Setter no btn radio gmail
        self.le_host.setText('smtp.mail.yahoo.com')
        self.sb_port.setValue(465)
        # Getter no LineEdit
        self.user_host = self.le_host.text()
        self.user_port = self.sb_port.text()

    def radio_outros(self):
        # Setter no btn radio gmail
        self.le_host.setText('')
        self.sb_port.setValue(0)
        # Getter no LineEdit
        self.user_host = self.le_host.text()
        self.user_port = self.sb_port.text()

    #Botão Enviar
    def enviar(self):
        texto = self.textEdit.toPlainText()
        self.user_email = self.le_email.text()
        self.user_senha = self.le_senha.text()
        try:
            for candidato, email in self.candidados_reprovados.items():
                with open('main.html', 'r', encoding='utf-8') as html:
                    template = Template(html.read())
                    body = template.substitute(mensagem=texto,
                                               nome=candidato,
                                               assinatura=lista_assinatura[0] if len(lista_assinatura) > 0 else '')
                    #Criando Mensagem
                    msg = MIMEMultipart()
                    msg['from'] = 'Torpedo de emails 2.0'
                    msg['to'] = email['email']
                    msg['subject'] = 'Resultado do processo seletivo.'
                    send = MIMEText(body, 'html', 'utf-8')
                    msg.attach(send)

                    with smtplib.SMTP(host=self.user_host,
                                      port=self.user_port) as smtp:
                        smtp.ehlo()
                        smtp.starttls()
                        smtp.login(self.user_email, self.user_senha)
                        smtp.send_message(msg)
        except(Exception) as erro:
            if type(erro) == AttributeError or type(erro) == TypeError:
                QMessageBox.about(self, 'Alerta', 'Preencha os dados corretamente.')
            else:
                QMessageBox.about(self, 'Alerta', 'Confira seus dados de autenticação e tente novamente.'
                                                  '\nSeu email não foi enviado.')
        else:
            QMessageBox.about(self, 'Concluido', 'Sua mensagem foi enviada com sucesso.')

    def candidatos(self):
        """Abre a tela de candidatos"""
        self.candidatos = Candidatos()
        self.candidatos.show()


class Assinatura(QMainWindow, Ui_AssDigital):
    def __init__(self):
        super().__init__(parent=None)
        super().setupUi(self)
        self.btn_box.button(self.btn_box.Ok).clicked.connect(self.salva_assinatura)
        self.btn_box.button(self.btn_box.Cancel).clicked.connect(self.close)

    def salva_assinatura(self):
        try:
            global lista_assinatura
            lista_assinatura.append(self.le_assinatura.text())
        except:
            pass
        finally:
            self.close()


class Candidatos(QMainWindow, Ui_Candidatos):
    def __init__(self):
        super().__init__(parent=None)
        super().setupUi(self)
        try:
            for candidatos in lista_candidatos:
                for index, candidato in enumerate(candidatos.items()):
                    texto = f"{index+1}° {candidato[0]} : {candidato[1]['email']}"
                    self.lw_candidatos.addItem(texto)
        except:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tela = Principal()
    tela.show()
    sys.exit(app.exec_())
