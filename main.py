from tkinter import *

root = Tk()
root.geometry('500x500+0+0')
root.title('ficha de cadastro com radio button')

Label(root,text='cadastro de pessoa').pack()

def imprimir():
    print('''......................
sexo    : {}
idade   : {}
e. civil: {}
motivo  : {}
horário : {}
......................'''.format(sexo.get(),idade.get(),estado.get(),motivo.get(),horario.get()))

sexo = StringVar()
idade = StringVar()
estado = StringVar()
motivo = StringVar()
horario = StringVar()


Label(root,text='sexo:').place(x=10,y=10)
sexo_m = Radiobutton(root,text='masculino', value='masculino',variable=sexo)
sexo_m.place(x=10,y=25)
sexo_f = Radiobutton(root,text='feminino', value='feminino',variable=sexo)
sexo_f.place(x=10,y=45)


Label(root,text='idade:').place(x=10,y=80)
idade_1 = Radiobutton(root,text='entre 1-17 anos', value='criança',variable=idade)
idade_1.place(x=10,y=95)
idade_20 = Radiobutton(root,text='entre 18-40 anos', value='adulto',variable=idade)
idade_20.place(x=10,y=115)
idade_40 = Radiobutton(root,text='mais de 40', value='idoso',variable=idade)
idade_40.place(x=10,y=135)


Label(root,text='estado civil:').place(x=10,y=170)
solteiro = Radiobutton(root,text='solteiro', value='solteiro',variable=estado)
solteiro.place(x=10,y=185)
casado = Radiobutton(root,text='casado', value='casado',variable=estado)
casado.place(x=10,y=205)
viuvo = Radiobutton(root,text='viuvo', value='viuvo',variable=estado)
viuvo.place(x=10,y=225)


Label(root,text='motivo:').place(x=10,y=260)
m_agendamento = Radiobutton(root,text='agendamento', value='agendamento',variable=motivo)
m_agendamento.place(x=10,y=275)
m_reuniao = Radiobutton(root,text='reuniao', value='reuniao',variable=motivo)
m_reuniao.place(x=10,y=295)
m_reclamacao = Radiobutton(root,text='reclamação', value='reclamacao',variable=motivo)
m_reclamacao.place(x=10,y=315)


Label(root,text='horarios:').place(x=10,y=350)
manha1 = Radiobutton(root,text='manhã: 7h-9h30m', value='manha1',variable=horario)
manha1.place(x=10,y=365)
manha2 = Radiobutton(root,text='manhã: 9h45m-11h', value='manha2',variable=horario)
manha2.place(x=10,y=385)
tarde1 = Radiobutton(root,text='tarde: 13h-15h30m', value='tarde1',variable=horario)
tarde1.place(x=10,y=405)
tarde2 = Radiobutton(root,text='tarde: 15h45m-17h', value='tarde2',variable=horario)
tarde2.place(x=10,y=425)

btn = Button(root,text='imprimir',command=imprimir)
btn.place(x=10,y=460)

root.mainloop()