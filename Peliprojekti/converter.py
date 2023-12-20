import math

def convert_num(num: float) -> str:
    names = [
        "",
        "tuhatta",
        "miljoonaa",
        "biljoonaa",
        "triljoonaa",
        "kvadriljoonaa",
        "kvintiljoonaa",
        "sextiljoonaa",
        "septiljoonaa",
        "oktiljoonaa",
        "noniljoonaa",
        "desiljoonaa",
        "undesiljoonaa",
        "duodesiljoonaa",
        "tredesiljoonaa",
        "kvattuordesiljoonaa",
        "kvindesiljoonaa",
        "sexdesiljoonaa",
        "septendesiljoonaa",
        "oktodesiljoonaa",
        "novemdesiljoonaa",
        "vigintiljoonaa"
    ]

    for i in range(len(names)):
        if num >= 10**66:
            return "Liikaa, menisit jo töihin."
        if num%1000**(i+1) >= num:
            if i == 0:
                return str(int(num))
            else:
                return f"{str(round(num/(1000**i), 2))} {names[i]}"