# This script shows what HINTING means
#   Hint is used to force types (casting) and are easily recongnized (eg.: -> str = def returns str type)

# 1 hinting a def and its arguments
def headline(text: str, align: bool = True) -> str: # align only accepts bool and default = True ; text only accepts str
    if align:
        return f"{text.title()}\n{'-' * len(text)}" # title() means proper CAPS when align is passed as True
    else:
        return f"{text.title()}".center(150, "+") # .center(x,y) means padding center with 150 + signs

print(headline("*python type checking*", align=True))

print(headline("|python type checking|", align=False))

print(headline(123_000, align=False)) # text is not str therefore is a type error 

print(headline("Alejandro")) # align is not passed therefore in method becomes True by default