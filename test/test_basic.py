# -*- coding: UTF-8 -*-

from askquora import askquora

LINK = 'https://www.quora.com/What-are-the-best-ways-to-learn-how-to-program'

def test_answer():
    expect_line = 'Pick a project and work on it.'
    answer = askquora.answer_question(LINK)
    lines = answer.splitlines()
    line = lines[0]
    assert line == expect_line
