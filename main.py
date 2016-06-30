#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2

html_form = """
    <!doctype html>
    <html lang="en">
        <head>
            <meta charset="utf-8"/>
            <title>Pata!</title>
        </head>
        <body>
        <h1>Pata Word</h1> 
            <form method="post">
         <label for="firstWord">First Word: </label>
         <input name="firstWord" type="text" value=""><br>
         
         <label for="secondWord">Second Word: </label>
         <input name="secondWord" type="text" value=""><br>
         
         <input name="" type="submit" value="Pata It!">
         </form>
        </body>
    </html>
    """

def buildPata(first_word, second_word):
    new_word = ""
    if first_word > second_word:
        for ii in range(0, len(second_word)):
            new_word += first_word[ii] + second_word[ii]
    for ii in range(len(second_word)+1, len(first_word)):
            new_word += first_word[ii]
    else:
        for ii in range(0, len(first_word)):
            new_word += first_word[ii] + second_word[ii]
        for ii in range(len(first_word)+1, len(second_word)):
            new_word += second_word[ii]
    return new_word


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(html_form)
    def post(self):
        first_word = self.request.get("firstWord")
        second_word = self.request.get("secondWord")
        pata_word = buildPata(first_word, second_word)
        self.response.write("Your new word is " + pata_word + "!")


app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
