import pygame

pygame.font.init()
font = pygame.font.Font("font.ttf")

# Longer text elements for overlay screens
sentence = {
    "main_screen": [
        "Hei, ja tervetuloa opiskelemaan meille tänne Turun yliopistoon!",
        " ",
        "Kerrytä opintopisteitä klikkailemalla suurta [PANOSTA] painiketta, ",
        "tai näppäilemällä mitä tahansa näppäintä näppäimistölläsi.",
        " ",
        "Kehitä osaamistasi ostamalla päivityksiä näytön oikealla puolella",
        "sijaitsevasta valikosta",
        " ",
        "Pidä hauskaa ja muista valmistua tavoiteajassa!"
    ],
    "win_screen": [
        "Onneksi olkoon, valmistuit diplomi-insinööriksi tavoiteajassa!",
        " ",
        "Voit joko valmistua ja siirtyä työelämään, tai voit jatkaa opiskelijaelämää",
        "korkeamman tutkinnon toivossa.",
        " ",
        "Huom! diplomi-insinööriä korkeammille tutkinnoille ei ole asetettu konkreettista",
        "aikarajaa. Älä kuitenkaan opiskele kuolemaasi asti, sillä se olisi erittäin",
        "kuormittavaa valtion taloudelle!"
    ],
    "lose_screen": [
        ": (",
        " ",
        "Voi ei! Näyttää pahasti siltä, että et onnistunut suorittamaan diplomi-insinööri-",
        "tutkintoasi määräajassa, ja yliopisto on päättänyt evätä kaikki opintosuorituksesi.",
        " ",
        "Voit joko aloittaa uuden koulutuksen painamalla [reset], tai luovuttaa painamalla",
        "[lopeta]."
    ],
    "kick_screen": [
        "Näyttäisi siltä, että olet käyttänyt sen verran aikaa opiskeluun, että se uhkaa haitata",
        "jo valtiomme taloutta. Emme voi antaa moisen jatkua, joten kansia on hartaan",
        "pohdinnan jälkeen tullut siihen tulokseen, että teidät on potkittava pihalle",
        "laitoksestamme. Eiköhän jo nimittäin noin korkealla tutkinnolla rupea",
        "parempipalkkaisiakin töitä löytymään.",
        " ",
        "Onnea ja menestystä",
        "Kanslia"
    ]
}

# Definitions for visuals
img = {
    "panosta": "panosta.png",
    "panosta_scaled": "panosta.png",
    "top_bar": "top_bar.png",
    "upgrade_zone": "upgrade_zone.png",
    "upgrade_unit": "upgrade_unit.png"
    }

# Definitions for static text elements
txt = {
    "opintopisteet": font.render("Opintopisteet: ", True, 0),
    "reset": font.render("Reset", True, 0),
    "sulje": font.render("Sulje", True, 0),
    "jatka": font.render("Jatka", True, 0),
    "lopeta": font.render("Lopeta", True, 0),
    "pvm": font.render("Päivämäärä:", True, 0),
    "opiskeluoikeus": font.render("Opiskeluoikeus päättyy:", True, 0),
    "tj": font.render("Tänään jäljellä (TJ):", True, 0),
    "main_screen": [font.render(i, True, 0) for i in sentence["main_screen"]],
    "win_screen": [font.render(i, True, 0) for i in sentence["win_screen"]],
    "lose_screen": [font.render(i, True, 0) for i in sentence["lose_screen"]],
    "kick_screen": [font.render(i, True, 0) for i in sentence["kick_screen"]]
}

# Useful color values
color = {
    "green": (3, 252, 73),
    "red": (240, 67, 55),
    "grey": (150, 150, 150)
}

# Rank (name, rank up cost, multiplier)
rank = [
    ("Fuksi", 10**6, 1),
    ("2. vsk", 10**9, 2),
    ("3. vsk", 10**12, 3),
    ("Kandidaatti", 10**15, 4),
    ("Kandidaatti (4. vsk)", 10**18, 5),
    ("Kandidaatti (5. vsk)", 10**21, 6),
    ("Diplomi-insinööri", 10**24, 7),
    ("Tohtori", 10**30, 8.5),
    ("Tohtori+", 10**36, 10.3),
    ("Tohtori++", 10**42, 12),
    ("Tohtori+++", 10**48, 13.7),
    ("Tohtori++++", 10**54, 15.3),
    ("Tohtori+++++", 10**60, 16.8),
    ("Tohtori++++++", 10**66, 18.3)
]