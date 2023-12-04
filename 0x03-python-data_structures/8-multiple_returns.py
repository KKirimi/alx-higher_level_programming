#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
    if sentence:
        ken_len = len(sentence)
    else:
        ken_len = 0
    return (ken_len, sentence if not sentence else sentence[:1])
