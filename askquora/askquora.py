#!/usr/bin/env python

from colorama import init, Fore, Style
from bs4 import BeautifulSoup
import os
import sys
import random
import requests
import textwrap
import argparse


# parse positional and optional arguments
def parse_args():
    parser = argparse.ArgumentParser(
        description='Quora Q&A right from the command-line')

    parser.add_argument(
        'query',
        metavar='QUERY',
        type=str,
        nargs='*',
        help='the question to find the answer of')
    parser.add_argument(
        '-n',
        '--no-color',
        help='do not colorize or style text',
        action='store_true')

    return parser


# random headers help increase rate limit
def random_header():
    HEADERS = (
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100 101 Firefox/22.0',
        'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko)',
        'Chrome/19.0.1084.46 Safari/536.5',
        'Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko)',
        'Chrome/19.0.1084.46', 'Safari/536.5',
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13'
    )

    return random.choice(HEADERS)


# receive user selected question
def get_input_link(links):
    while True:
        selection = int(input('> '))

        if selection <= len(links) and selection >= 1:
            break
        else:
            print('Choose a valid number!')

    return links[selection - 1]


# duckduckgo links are different from actual webpage links
def duckduckgo_links(query):
    header = {'User-agent': random_header()}

    page = requests.get(
        'https://duckduckgo.com/html/?q=' + query + ' site:quora.com',
        headers=header).text
    soup = BeautifulSoup(page, 'html.parser')

    possible_links = soup.find_all('a', {'class': 'result__a'})

    return possible_links


# decode a duckduckgo link to actual webpage link
def decode_result(link):
    header = {'User-agent': random_header()}
    inner_link = 'https://duckduckgo.com' + link['href']

    page = requests.get(inner_link, headers=header).text
    soup = BeautifulSoup(page, 'html.parser')

    link = (soup.find('script').get_text()).replace(
        'window.parent.location.replace("', '').replace('");', '')

    return link


# show title of the question
def show_title(link, numb, color=None):
    width = int((os.popen('stty size', 'r').read().split())[1])

    if color is None:
        Fore.RED = ''
        Fore.MAGENTA = ''
        Style.BRIGHT = ''

    if color:
        prefix = Fore.RED + Style.BRIGHT + '{0: <4}'.format(str(numb) + '.')
    else:
        prefix = Fore.MAGENTA + Style.BRIGHT + '{0: <4}'.format(
            str(numb) + '.')

    wrapper = textwrap.TextWrapper(
        initial_indent=prefix, width=width, subsequent_indent='    ')

    print(wrapper.fill(
        link.replace('https://www.quora.com/', '').replace(
            '?share=1', '').replace('-', ' ') + '?'))


# decode all links and display title of all questions
def correct_links(possible_results, colored):
    links = []
    numb = 1
    color = True

    for result in possible_results[:10]:
        link = decode_result(result)
        if is_question(link):
            if colored:
                show_title(link, numb, color)
            else:
                show_title(link, numb)
            links.append(link)

            color = not color
            numb += 1

    return links


# check if the link is a quora question
def is_question(link):
    if link.startswith('https://www.quora.com/') and not link.startswith(
            'https://www.quora.com/topic/') and not link.startswith(
                'https://www.quora.com/profile/'):
        return True
    else:
        return False


# display answer to user chosen question
def answer_question(link, colored=False):
    header = {'User-agent': random_header()}

    ques_page = requests.get(link, headers=header).text
    ques_page = ques_page.replace('<br />', '\n')
    ques_page = ques_page.replace('</p>', '\n\n')

    if colored:
        ques_page = ques_page.replace('<b>', Fore.YELLOW).replace(
            '</b>', Fore.RED)
        ques_page = ques_page.replace('<a', Fore.BLUE + '<a').replace(
            '</a>', Fore.RED + '</a>')

    soup = BeautifulSoup(ques_page, 'html.parser')

    try:
        answer = soup.find('div', {'class':
                                   'ExpandedQText ExpandedAnswer'}).get_text()
    except AttributeError:
        answer = 'Sorry, this question has not been answered yet..'

    if colored:
        answer = Fore.RED + Style.BRIGHT + answer

    return answer


# parse the query into a searchable query
def generate_search_query(query):
    query = (' '.join(query)).replace(' ', '+')
    return query


# the main function
def askquora(query, colored):
    query = generate_search_query(query)

    encoded_links = duckduckgo_links(query)
    question_links = correct_links(encoded_links, colored)

    print('\nChoose a Question:')
    question_link = get_input_link(question_links)

    if colored:
        answer = answer_question(question_link, colored)
    else:
        answer = answer_question(question_link)

    print('\n' + answer)


if __name__ == '__main__':

    parser = parse_args()

    # do not pass filename as positional argument
    raw_args = sys.argv[1:]
    args = parser.parse_args(raw_args)

    if not args.query:
        parser.print_help()
        exit()

    init(autoreset=True)

    # python2 compatibility
    if sys.version_info < (3, 0):
        input = raw_input

    query = args.query
    colored = not args.no_color

    try:
        askquora(query, colored)
    except KeyboardInterrupt:
        print('')

    exit()
