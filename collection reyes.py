# Jorge Reyes
# CSS 225

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889
# Total 7 errors

# Name Error: author was mispelled
authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"}
# SyntaxError: invalid syntax
# SyntaxError: '{' was never closed
for author ,date in authors.items():
    # SyntaxError: invalid syntax
    print(author + " died in " + date)
# SyntaxError where the parentheses weren't added
# NameError where %s and % where added in print delete them
# SyntaxError where + was supposed to be added between died in and date

