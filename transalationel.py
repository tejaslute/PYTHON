def transational(phrase):
    transational1=""
    for letter in phrase:
        if letter in ("aeioAEIOU"):
            transational1=transational1+"h"
        else:
            transational1=transational1+letter
    return transational1


print(transational("hello"))