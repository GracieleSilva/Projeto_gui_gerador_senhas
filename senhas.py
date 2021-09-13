import PySimpleGUI as sg
import os, random, string

def geradorSenhas(length, chars):
	if len(chars)<0:
		chars = string.ascii_letters
	random.seed = (os.urandom(1024))
	return ''.join(random.choice(chars) for i in range(length))

sg.theme('dark grey 9')
layout = [
	[sg.Text('This is my sample text', size=(20, 1), key='-text-')],
	# [
	# 	sg.CB('Letras', key='-letra-', change_submits=True),
	# 	sg.CB('Numeros', key='-numeros-', change_submits=True),
	# 	sg.CB('Caracteres', key='-caracteres-', change_submits=True)
	# ],
	[sg.Slider((6, 20), default_value=12, size=(14, 20), orientation='h', key='-slider-', change_submits=True), sg.Text('Tamanho da Senha')],
	[sg.Text('Font string = '), sg.Input(enable_events=True, size=(25, 1), key='-fontstring-')],
	[sg.Button('Gera'), sg.Button('Exit')]
]

window = sg.Window('My First App', layout)

font_string=""

while True:
	event, values = window.read()

	if event in (None, 'Exit'):
		break
	if event in ('Gera'):
		string= string.ascii_letters+string.digits+'!@#$%^&*()'
		font_string = geradorSenhas(int(values['-slider-']), string)

	window['-fontstring-'].update(font_string)

window.close()