import kivy
kivy.require("1.9.1")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView


Window.size = (400,600)


class Lgn(BoxLayout):
    def logar(self):
        usuario = self.ids.usuario.text
        senha = self.ids.senha.text

        if usuario == 'admin' and senha == 'master':
            janela.root_window.remove_widget(janela.root)
            janela.root_window.add_widget(Home())

        else:
            self.ids.msg.text = 'Usuário ou senha invalida'

    # def on_press_bt(self):
    #    janela.root_window.remove_widget(janela.root)
    #    janela.root_window.add_widget(Home())


class Home(BoxLayout):
    def home(self):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(Home())

    def consultar_aluno(self):
       janela.root_window.remove_widget(janela.root)
       janela.root_window.add_widget(Consultar_Aluno())

    def cadastrar_aluno(self):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(Cadastrar_Aluno())

    def consultar_anamnese(self):
       janela.root_window.remove_widget(janela.root)
       janela.root_window.add_widget(Consultar_Anamnese())

    def cadastrar_anamnese(self):
       janela.root_window.remove_widget(janela.root)
       janela.root_window.add_widget(Cadastrar_Anamnese())


class Consultar_Aluno(ScrollView):
   def consultar_aluno(self):
       pass

   def voltar(self):
       janela.root_window.remove_widget(janela.root)
       janela.root_window.add_widget(Home())

class Cadastrar_Aluno(BoxLayout):
    def cadastrar_aluno(self):
        pass

    def addaluno(self):
        texto = self.ids.texto.text
        self.ids.box.add_widget(Consultar_Aluno(text=texto))
        self.ids.texto.text = ''

    def voltar(self):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(Home())

class Consultar_Anamnese(BoxLayout):
    def consultar_anamnese(self):
        pass

    def voltar(self):
       janela.root_window.remove_widget(janela.root)
       janela.root_window.add_widget(Home())


class Cadastrar_Anamnese(BoxLayout):
    def cadastrar_anamnese(self):
        pass

    def addanamnese(self):
        texto = self.ids.texto.text
        self.ids.box.add_widget(Consultar_Anamnese(text=texto))
        self.ids.texto.text = ''

    def voltar(self):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(Home())

class Login(App):
    def build(self):
        return Lgn()

janela = Login()
janela.run()