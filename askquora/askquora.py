#!/bin/python

from sys import argv
from colorama import init, Fore, Style
from bs4 import BeautifulSoup
from os import popen
import requests
import textwrap

def cli():
	argv.pop(0)
	init(autoreset=True)
	headers = {"User-agent": "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13"}

	if len(argv) == 0:
		print('Usage: askquora <your question>')
		exit()
	query = ' '.join(argv)
	link = 'https://www.quora.com/search?q=' + query.replace(' ', '+')
	results = requests.get(link, headers=headers).text

	soup = BeautifulSoup(results, 'html.parser')
	questions = soup.find_all('a', {'class':'question_link'})

	width = int((popen('stty size', 'r').read().split())[1])
	color = True
	numb = 1

	for question in questions:
		if color:
			prefix = Fore.RED + Style.BRIGHT + '{0: <4}'.format(str(numb) + '.')
		else:
			prefix = Fore.MAGENTA + Style.BRIGHT + '{0: <4}'.format(str(numb) + '.')
		wrapper = textwrap.TextWrapper(initial_indent=prefix, width=width, subsequent_indent='    ')
		print wrapper.fill(question.get_text())
		color = not color
		numb += 1

	print('')
	print('Choose a Question')

	while True:
		selection = int(raw_input('> '))
		if selection <= len(questions) and selection >= 1:
			break
		else:
			print('Choose a valid number!')

	link = 'http://quora.com' + questions[selection-1]['href']
	ques_page = (requests.get(link, headers=headers).text)
	ques_page = ques_page.replace('<b>', Fore.YELLOW).replace('</b>', Fore.RED)
	ques_page = ques_page.replace('<a', Fore.BLUE + '<a').replace('</a>', Fore.RED + '</a>')
	ques_page = ques_page.replace('<br />', '\n')

	print('')
	soup = BeautifulSoup(ques_page, 'html.parser')

	try:
		answer = Fore.RED + Style.BRIGHT + soup.find('div', {'class':'ExpandedQText ExpandedAnswer'}).get_text()
		print answer
	except AttributeError:
		print 'Sorry, this question has not been answered yet..'
	exit()

if __name__=='__main__':
	cli()
