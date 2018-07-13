import re

text = """Giraffes have aroused the curiousity of __Plural_Noun__
    since earliest times. the giraffe is the tallest of all living
    __Plural_Noun__ , but scientists are unable to explain how it
    got it's long __Part_of_the_Body__. The giraffe's tremendous
    height, which might reach __Number__ __Plural_Noun__, comes from
    its legs and __Bodypart__."""

def mad_libs(mls):
    hints = re.findall("__.*?__", mls)
    if hints is not None:
        for word in hints:
            q = "Enter a {}".format(word)
            new = input(q)
            mls = mls.replace(word, new, 1)
        print('\n')
        mls = mls.replace("\n", "")
        print(mls)
    else:
        print("invalid madlib")

mad_libs(text)
