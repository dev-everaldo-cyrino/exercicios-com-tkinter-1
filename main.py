from tkinter import *

root = Tk()
root.geometry('500x500+0+0')
root.title('ficha de cadastro com radio button')

Label(root,text='cadastro de pessoa').pack()

sexo = StringVar()
idade = StringVar()
estado = StringVar()
motivo = StringVar()
horario = StringVar()

sexo_m = Radiobutton(root,text='masculino', value='masculino',variable=sexo)
sexo_m.pack()
sexo_f = Radiobutton(root,text='feminino', value='feminino',variable=sexo)
sexo_f.pack()


idade_1 = Radiobutton(root,text='entre 1-17 anos', value='criança',variable=idade)
idade_1.pack()
idade_20 = Radiobutton(root,text='entre 18-40 anos', value='adulto',variable=idade)
idade_20.pack()
idade_40 = Radiobutton(root,text='mais de 40', value='idoso',variable=idade)
idade_40.pack()


solteiro = Radiobutton(root,text='solteiro', value='solteiro',variable=estado)
solteiro.pack()
casado = Radiobutton(root,text='casado', value='casado',variable=estado)
casado.pack()
viuvo = Radiobutton(root,text='viuvo', value='viuvo',variable=estado)
viuvo.pack()


m_agendamento = Radiobutton(root,text='agendamento', value='agendamento',variable=motivo)
m_agendamento.pack()
m_reuniao = Radiobutton(root,text='reuniao', value='reuniao',variable=motivo)
m_reuniao.pack()
m_reclamacao = Radiobutton(root,text='reclamação', value='reclamacao',variable=motivo)
m_reclamacao.pack()


manha1 = Radiobutton(root,text='manhã: 7h-9h30m', value='manha1',variable=horario)
manha1.pack()
manha2 = Radiobutton(root,text='manhã: 9h45m-11h', value='manha2',variable=horario)
manha2.pack()
tarde1 = Radiobutton(root,text='tarde: 13h-15h30m', value='tarde1',variable=horario)
tarde1.pack()
tarde2 = Radiobutton(root,text='tarde: 15h45m-17h', value='tarde2',variable=horario)
tarde2.pack()

btn = Button(root,text='imprimir')
btn.pack()

root.mainloop()