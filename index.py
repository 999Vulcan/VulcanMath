# -*- coding: utf-8 -*-
import webapp2

from drills import * #@UnusedWildImport

GACode = """
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-RZFHL0Q2FQ"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-RZFHL0Q2FQ');
</script>
"""

HTMLHead = '<html><head><meta name="theme-color" content="#3C8DF6"><title>√ulcan Mind Math</title>' + GACode + """
    <meta property="og:image" content="https://vulcanmath.vulakh.us/ThinkingCap.jpg" />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="https://vulcanmath.vulakh.us" />
    <meta property="og:title" content="√ulcan Mind Math" />
    <meta property="twitter:image" content="https://vulcanmath.vulakh.us/ThinkingCap.jpg" />
    <meta property="twitter:title" content="√ulcan Mind Math" />""" + '</head><body>'

class PrintFractions(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(HTMLHead + "<font size=5>\n<pre>")
        for s in BuildFractions(27, 6, 45, 2, 9): self.response.out.write(s)

class PrintKGMath1(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(HTMLHead + "<font size=5>\n<pre>")
        for s in KGMath1(39, 10, 50): self.response.out.write(s)

class PrintMult1(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(HTMLHead + "<font size=5>\n<pre>")
        for s in Mult1(39, 12): self.response.out.write(s)

class PrintKGMath2(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(HTMLHead + "<font size=5>\n<pre>")
        for s in KGMath2(39, 10, 90, 99): self.response.out.write(s)

class Gosha(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(HTMLHead + "<font size=5>\n<pre>")
        for s in KGMath2(39, 1, 9, 10): self.response.out.write(s)

class PrintMultiplication(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(HTMLHead + "<font size=5>\n<pre>")
        for s in Multiplication(39, 11, 90, 2, 9): self.response.out.write(s)

class PrintBinomials(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(HTMLHead + "<font size=5>\n<pre>")
        for s in Binomials(32, 2, 20, 30): self.response.out.write(s)

class PrintEq1(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(HTMLHead + "<font size=5>\n<pre>")
        for s in Equations1(39, 15, 49): self.response.out.write(s)
        
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(HTMLHead + 
"""
<center>
<a href="Gosha"><img src="ThinkingCap.jpg" width="200" height="242"></a>
<font face=Arial>
<table border=1 cellpadding=15><tr><td><center>
<b>√</b>ulcan Mind Math
<font size=-1>
<br><br>
<form action="KGMath1" method="get">
  <div><input type="submit" style="width:140px; background-color:white; cursor:pointer" value=" a + b "></div>
</form>
<form action="KGMath2" method="get">
  <div><input type="submit" style="width:140px; background-color:white; cursor:pointer" value=" a &plusmn; b "></div>
</form>
<form action="Mult1" method="get">
  <div><input type="submit" style="width:140px; background-color:white; cursor:pointer" value=" a &times; b "></div>
</form>
<form action="Equations1" method="get">
  <div><input type="submit" style="width:140px; background-color:white; cursor:pointer" value=" x &plusmn; a = b "></div>
</form>
<form action="Multiplication" method="get">
  <div><input type="submit" style="width:140px; background-color:white; cursor:pointer" value=" a &times; b &plusmn; c"></div>
</form>
<form action="Fractions" method="get">
  <div><input type="submit" style="width:140px; background-color:white; cursor:pointer" value=" a/b &plusmn; c/d "></div>
</form>
<form action="Binomials" method="get">
  <div><input type="submit" style="width:140px; background-color:white; cursor:pointer" value="(ax &plusmn; b) &times; (cx &plusmn; d)"></div>
</form>

</td></tr></table>

<center>
<font size=1>Click. Print. Fold. Refresh. Repeat.</font>
<br><br><br>
<img src="/GAE.gif"width="120" height="30" hspace="3">
<img src="/Python.jpg"width="70" height="28">
<br>
<img src="/gcp-logo-small.png"width="189" height="25" hspace="5">
<br>
<br>
<font size=2>
&copy; 2012 <a href="http://999Vulcan.vulakh.us">⁹⁹⁹√ulcan™</a>

""")

app = webapp2.WSGIApplication([('/Binomials', PrintBinomials),
                              ('/Fractions', PrintFractions),
                              ('/Multiplication', PrintMultiplication),
                              ('/Equations1', PrintEq1),
                              ('/KGMath1', PrintKGMath1),
                              ('/KGMath2', PrintKGMath2),
                              ('/Mult1', PrintMult1),
                              ('/Gosha', Gosha),
                              ('/.*', MainPage)])
