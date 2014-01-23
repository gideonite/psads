#!/usr/bin/python


def read_tag(html, i):
    '''
    html, current index -> tag, index to continue at.
    '''
    tag_chrs = []
    for i in range(i, len(html)):
        ch = html[i]
        tag_chrs.append(ch)
        if ">" == ch:
            return "".join(tag_chrs), i

def balance(html):
    '''
    string -> bool.
    Tests whether all the html tags are balanced.
    '''
    i = 0
    tags = []
    while i < len(html):
        ch = html[i]

        if "<" == ch:
            tag, i = read_tag(html, i)

            if "/" in tag:
                try:
                    tags.pop()
                except IndexError:
                    return False
            else:
                tags.append(tag)

        i+=1
    if len(tags) != 0:
        return False

    return True


    return html.split(" ")

html1 = '''
<html>
   <head>
      <title>
         Example
      </title>
   </head>

   <body>
      <h1>Hello, world</h1>
   </body>
</html>
'''
assert balance(html1)

html1 = '''
   <head>
      <title>
         Example
      </title>
   </head>

   <body>
      <h1>Hello, world</h1>
   </body>
</html>
'''
assert not balance(html1)

html2 = '''
<html>
   <head>
      <title>
         Example
      </title>
   </head>

   <body>
      <h1>Hello, world</h1>
   </body>
'''
assert not balance(html2)

html3 = '''
<html>
   <head>
      <title>
         Example
      </title>
   </head>

   <body>
      <h1>Hello, world</h1>
   </body>
'''
assert not balance(html3)

html4 = '''
<html>
   <head>
      <title>
         Example
   </head>

   <body>
      <h1>Hello, world</h1>
   </body>
</html>
'''
assert not balance(html4)
