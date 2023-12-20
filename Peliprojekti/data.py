import pygame

pygame.font.init()
font = pygame.font.Font("font.ttf")

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
}

# Useful color values
color = {
    "green": (3, 252, 73),
    "red": (240, 67, 55)
}