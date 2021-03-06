prose = """Hi mom,

Just writing to tell you that I've quit my job as a OCCUPATION and I'm moving to COUNTRY. The truth is, I've always been passionate about PLURAL_NOUN, and COUNTRY is the best place in the world to build a career around them. I'll need to start small-- At first, all I'll be allowed to do is to VERB near them, but when people see how ADJECTIVE I can be, I'm sure to rise to the top.

Don't worry about me, and tell dad to take good care of my PERSONAL_ITEM. I'll be sure to call every HOLIDAY.

Love,

NAME"""

replacements = [
    ["Occupation? ", "OCCUPATION"],
    ["Moving to Country? ", "COUNTRY"],
    ["Passionate about? ", "PLURAL_NOUN"],
    ["What you will do at your job? ", "VERB"],
    ["Professional quality? ", "ADJECTIVE"],
    ["Name a personal item? ", "PERSONAL_ITEM"],
    ["Favorite Holiday? ", "HOLIDAY"],
    ["Your name? ", "NAME"],
]

# we've managed to separate our data from our logic
for prompt, placeholder in replacements:
    prose = prose.replace(placeholder, input(prompt))

print(prose)
