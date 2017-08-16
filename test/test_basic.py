# -*- coding: UTF-8 -*-

from askquora import askquora

LINK = 'https://www.quora.com/What-the-hell-am-I-doing-with-my-life'

def test_answer():
    expect_line = 'lol you are a funny writer. '
    answer = askquora.answer_question(LINK)
    lines = answer.splitlines()
    line = lines[0]
    assert line == expect_line
