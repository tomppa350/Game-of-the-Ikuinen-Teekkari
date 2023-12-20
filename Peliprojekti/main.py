import pygame
import data
import math
import converter

pygame.init()
pygame.display.set_caption("Game of the Ikuinen Teekkari")

# variables
score = 0
img = data.img
txt = data.txt
font = data.font
color = data.color
button_pressed = False
screen = pygame.display.set_mode((1280, 720))
hitbox = pygame.Rect(50,225,460,130)
FPS = pygame.time.Clock()

# Upgrades
upgrade = [
    {"level": 0, "cost": 10}, # Multitask
    {"level": 0, "cost": 20}, # Motivation
    {"level": 0, "cost": 30}, # Number of GPTs
    {"level": 0, "cost": 40}, # GPT version
    {"level": 0, "cost": 50}, # Graduate
]

# Load images
for png in data.img.keys():
    img[png] = pygame.image.load(img[png])

# Texture and image surface scaling
img["panosta"] = pygame.transform.scale_by(img["panosta"], 10)
img["top_bar"] = pygame.transform.scale_by(img["top_bar"], 3.2)
img["upgrade_zone"] = pygame.transform.scale_by(img["upgrade_zone"], 6)
img["upgrade_unit"] = pygame.transform.scale_by(img["upgrade_unit"], 4)
txt["opintopisteet"] = pygame.transform.scale_by(txt["opintopisteet"], 3)

# Main loop
while True:

    # Dynamic variables
    mousepos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        # Score button animation and functionality
        if (event.type == pygame.MOUSEBUTTONDOWN and hitbox.collidepoint(mousepos)) or event.type == pygame.KEYDOWN:
            img["panosta_scaled"] = pygame.transform.scale(img["panosta"], (456, 126))
            button_pressed = True
        if (event.type == pygame.MOUSEBUTTONUP and hitbox.collidepoint(mousepos)) or event.type == pygame.KEYUP:
            button_pressed = False
            score += (upgrade[0]["level"]+1)*(upgrade[1]["level"]+1)

        # Purchase system
        for i in range(5):
            if score >= upgrade[i]["cost"]:
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect(825, 100*(i+1), 400, 75).collidepoint(mousepos):
                    upgrade[i]["level"] += int(1)
                    score -= upgrade[i]["cost"]

    # Updates to dynamic texts
    txt["score"] = font.render(converter.convert_num(score), 1, 0)
    txt["score"] = pygame.transform.scale_by(txt["score"], 3)
    txt["upgrade0_level"] = font.render(f"Multitaskauskyky {upgrade[0]["level"]}", True, 0)
    txt["upgrade1_level"] = font.render(f"Motivaatiotaso {upgrade[1]["level"]}", True, 0)
    txt["upgrade2_level"] = font.render(f"ChatGPT lkm {upgrade[2]["level"]}", True, 0)
    txt["upgrade3_level"] = font.render(f"Versio:  GPT-{upgrade[3]["level"]}", True, 0)
    txt["upgrade4_level"] = font.render(f"Rank {upgrade[4]["level"]}", True, 0)
    for i in range(5):
        txt[f"upgrade{i}_cost"] = font.render(f"Hinta {upgrade[i]["cost"]} OP", True, 0)
        txt[f"upgrade{i}_level"] = pygame.transform.scale_by(txt[f"upgrade{i}_level"], 2)
    

    screen.fill((200, 200, 200))

    # img positions
    if button_pressed:
        screen.blit(img["panosta_scaled"], (52, 227))
    else:
        screen.blit(img["panosta"], (50, 225))
    screen.blit(img["top_bar"], (0, 0))
    screen.blit(img["upgrade_zone"], (800, 75))

    for i in range(5):
        if score >= upgrade[i]["cost"]:
            pygame.draw.rect(screen, color["green"], (825, 100*(i+1), 400, 75))
        else:
            pygame.draw.rect(screen, color["red"], (825, 100*(i+1), 400, 75))

    # txt positions
    screen.blit(txt["opintopisteet"], (50, 75))
    screen.blit(txt["score"], (55, 150))  
    for i in range(5):
        screen.blit(txt[f"upgrade{i}_level"], (830, 100*(i+1)+5))
        screen.blit(txt[f"upgrade{i}_cost"], (830, 100*(i+1)+50))

    # Clock
    FPS.tick(60)
    pygame.display.flip()
