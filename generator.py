#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from flask import Flask, render_template, request, url_for
app = Flask(__name__)
app.debug = True

class Counter(object):
    def __init__(self):
        self.nb = 0

    def inc(self):
        self.nb += 1

    def get(self):
        return str(self.nb)

    def __str__(self):
        return str(self.nb)

class Dict(object):
    def __init__(self):
        self.dic = {}

    def get(self, url):
        return self.dic[url]

    def set(self, url, nb):
        self.dic[url] = nb

    def in_(self, url):
        return url in self.dic

    def dump(self):
        html = ""
        for url, nb in self.dic.items():
            html += "%s: %s<br />\n" % (nb, url)
            if int(nb) == math.ceil(len(self.dic) / 2):
                html += "</div><div class=\"bdp\">\n"
        return html

# define the different kinds of CV here
@app.route('/normal', methods=['GET'])
def disp_CV():
    return render_template("normal.html", nb=Counter(), urls_dic=Dict())

@app.route('/engineer', methods=['GET'])
def disp_engineer():
    return render_template("engineer.html", nb=Counter(), urls_dic=Dict())

@app.route('/sysadmin', methods=['GET'])
def disp_sysadmin():
    return render_template("sysadmin.html", nb=Counter(), urls_dic=Dict())

if __name__ == "__main__":
    app.run()
