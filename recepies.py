def pos_tagging(sentence):
    return ' '.join(map( lambda x:  x[0]+'/'+x[1], nltk.pos_tag(sentence.split(' '))))
