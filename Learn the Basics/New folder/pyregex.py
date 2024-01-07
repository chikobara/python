import re

file_handler = open(
    "/media/chiko/Data/Coding/python/Learn the Basics/New folder/mbox-short.txt"
)

for line in file_handler:
    line = line.rstrip()
    if re.search("From: ?", line):
        print(line)


"""
Symbol	Matches
?	zero or one of the preceding group.
*	zero or more of the preceding group.
+	one or more of the preceding group.
{n}	exactly n of the preceding group.
{n,}	n or more of the preceding group.
{,m}	0 to m of the preceding group.
{n,m}	at least n and at most m of the preceding p.
{n,m}? or *? or +?	performs a non-greedy match of the preceding p.
^spam	means the string must begin with spam.
spam$	means the string must end with spam.
.	any character, except newline characters.
\d, \w, and \s	a digit, word, or space character, respectively.
\D, \W, and \S	anything except a digit, word, or space, respectively.
[abc]	any character between the brackets (such as a, b, ).
[^abc]	any character that isn’t between the brackets.

"""
