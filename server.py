import os
import http.server
import socketserver
import nltk, re
nltk.download('punkt' )
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize, sent_tokenize, WhitespaceTokenizer
from nltk import pos_tag

from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        msg = 'Hello! you requested %s' % (self.path)
        self.wfile.write(msg.encode())
        text_sen = text = """This Paraphrasing tool is primarily developed to simplify the writing process, enabling you to restate the content at phrase, sentence, and paragraph levels. It modifies the diction and syntactic structures, making the content completely unique and error-free.

        🎯 Paraphrase	Plagiarism Free
        ✍ Maintain	Readability, Uniqueness, Creativity
        💲 Free	Free Unlimited Access
        🗺️ Languages	EN ID DE FR ES and more
        It works effectively to rewrite the content in a way that removes plagiarism, maintains readability, and makes the content considerably more appealing.

        Leverage any of its four paraphrasing modes to rewrite the content as required. It enables you to rewrite the content using the standard, fluency, creative, or smarter paraphrasing modes, each of which resonates with a distinct writing style."""

        tokens_positions = list(WhitespaceTokenizer().span_tokenize(text))  # Tokenize to spans to get start/end positions: [(0, 3), (4, 9), ... ]
        tokens = WhitespaceTokenizer().tokenize(text)  # Tokenize on a string lists: ["man", "walks", "into", ... ]
        token_s = nltk.pos_tag(tokens)
        #text_sen_words = replace_all(text_sen, token_s)
        for key, value in token_s:
          text_sen = re.sub(r'\b'+key+r'\b', '<span class="'+value+'">'+key+'</span>', text_sen)

        words = []
        for i in range(len(token_s)):
            text, tag = token_s[i]  # Get tag
            start, end = tokens_positions[i]  # Get token start/end
            #if tag == "NN" or tag == "VBZ":
            words.append((start, end, tag))

        #print(words)
        text_sen = text_sen.replace('\n','.\n <br>')
        sent_tokenize_list = sent_tokenize(text_sen);
        #print(sent_tokenize_list)
        #for index, item in enumerate(sent_tokenize_list):
        #    print(index)
        #    print(item)
        #    sent_tokenize_list += "<span class='sen-{index}'>"+item+"</span>"

        #print(sent_tokenize_list);


        print(text_sen)
        #print(word_tokenize(text_sen))
        #print(sent_tokenize(text_sen))

port = int(os.getenv('PORT', 80))
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()
