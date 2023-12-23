import pygame
import data
import math
from datetime import datetime, timedelta

pygame.init()
pygame.display.set_caption("Game of the Ikuinen Teekkari")

# variables
score = 0
img = data.img
txt = data.txt
font = data.font
color = data.color
rank = data.rank
sentence = data.sentence
date_current = datetime.now()
date_deadline = date_current + timedelta(days=5*365)
rank_current = 0
overlay = True
button_pressed = False
upgrade_mode = "1x"
screen = pygame.display.set_mode((1280, 720))
hitbox = pygame.Rect(50,225,460,130)
FPS = pygame.time.Clock()

# Functions
def save():
    with open("savedata.txt", "w") as file:
        file.write(f"{str(score)} ")
        for i in range(4):
            file.write(f"{upgrade[i]["level"]} ")
            file.write(f"{upgrade[i]["cost"]} ")
        file.write(f"{rank_current} ")
        file.write(f"{upgrade[4]["cost"]} ")
        file.write(f"{str(date_current).replace(" ", "-")} ")
        file.write(f"{str(date_deadline).replace(" ", "-")}")

def load():
    with open("savedata.txt", "r") as file:
        global score, upgrade, rank_current, date_current, date_deadline
        savedata = []
        file = file.read()
        savedata = file.split(" ")
        score = float(savedata[0])
        for i in range(4):
            upgrade[i]["level"] = float(savedata[2*i+1])
            upgrade[i]["cost"] = float(savedata[2*i+2])
        upgrade[4]["level"] = rank[int(savedata[9])][0]
        upgrade[4]["cost"] = int(savedata[10])
        rank_current = int(savedata[9])
        date_current = datetime.strptime(savedata[11], "%Y-%m-%d-%H:%M:%S.%f")
        date_deadline = datetime.strptime(savedata[12], "%Y-%m-%d-%H:%M:%S.%f")
        

def reset():
    with open("savedata.txt", "w") as file:
        file.write(f"0 0 10 0 1000 0 10000 0 10000 0 1000000 {str(datetime.now()).replace(" ", "-")} {str(datetime.now()+timedelta(days=5*365)).replace(" ", "-")}")

def is_empty(file: str) -> bool:
    with open(file, "r") as content:
        content = content.read()
        if content == "":
            return True
        else:
            return False

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

def start_screen():
        global overlay
        while True:

            mousepos = pygame.mouse.get_pos()

            pygame.draw.rect(screen, (255, 255, 255), (100, 100, 1080, 520))
            pygame.draw.rect(screen, (47, 54, 153), (100, 100, 1080, 520), 6)
            pygame.draw.rect(screen, color["grey"], (590, 550, 100, 50), 0, 5)
            screen.blit(txt["sulje"], (600, 555))
            for i in range(len(txt["main_screen"])):
                screen.blit(txt["main_screen"][i], (150, 150+40*i))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect(590, 550, 100, 50).collidepoint(mousepos):
                    overlay = False
                    return overlay

            FPS.tick(60)
            pygame.display.flip()

def win_screen():
    complete_time = timedelta(days=5*365)-(date_deadline-date_current)
    txt["complete_time"] = font.render(f"Tutkinto suoritettu: {round(complete_time.days/365, 1)} vuodessa.", True, 0)
    txt["complete_time"] = pygame.transform.scale_by(txt["complete_time"], 2)
    while True:

        mousepos = pygame.mouse.get_pos()

        pygame.draw.rect(screen, (255, 255, 255), (100, 100, 1080, 520))
        pygame.draw.rect(screen, (47, 54, 153), (100, 100, 1080, 520), 6)
        pygame.draw.rect(screen, color["grey"], (660, 550, 120, 50), 0, 5)
        pygame.draw.rect(screen, color["grey"], (500, 550, 120, 50), 0, 5)
        screen.blit(txt["jatka"], (675, 555))
        screen.blit(txt["lopeta"], (500, 555))
        for i in range(len(txt["win_screen"])):
                screen.blit(txt["win_screen"][i], (150, 150+40*i))
        screen.blit(txt["complete_time"], (150, 500))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect(660, 550, 120, 50).collidepoint(mousepos):
                return None
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect(500, 550, 120, 50).collidepoint(mousepos):
                reset()
                exit()

        FPS.tick(60)
        pygame.display.flip()
    
def lose_screen():
    txt["reset"] = font.render("Reset", True, 1)
    txt["reset"] = pygame.transform.scale_by(txt["reset"], 2)
    while True:

        mousepos = pygame.mouse.get_pos()

        pygame.draw.rect(screen, (255, 255, 255), (100, 100, 1080, 520))
        pygame.draw.rect(screen, (47, 54, 153), (100, 100, 1080, 520), 6)
        pygame.draw.rect(screen, color["grey"], (660, 550, 120, 50), 0, 5)
        pygame.draw.rect(screen, color["grey"], (500, 550, 120, 50), 0, 5)
        screen.blit(txt["reset"], (673, 555))
        screen.blit(txt["lopeta"], (500, 555))
        for i in range(len(txt["lose_screen"])):
                screen.blit(txt["lose_screen"][i], (150, 150+40*i))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect(660, 550, 120, 50).collidepoint(mousepos):
                txt["reset"] = font.render("Reset", True, 1)
                txt["reset"] = pygame.transform.scale_by(txt["reset"], 1.3)
                reset()
                load()
                return None
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect(500, 550, 120, 50).collidepoint(mousepos):
                txt["reset"] = font.render("Reset", True, 1)
                txt["reset"] = pygame.transform.scale_by(txt["reset"], 2)
                reset()
                exit()

        FPS.tick(60)
        pygame.display.flip()

def kick_screen():
        global overlay
        while True:

            mousepos = pygame.mouse.get_pos()

            pygame.draw.rect(screen, (255, 255, 255), (100, 100, 1080, 520))
            pygame.draw.rect(screen, (47, 54, 153), (100, 100, 1080, 520), 6)
            pygame.draw.rect(screen, color["grey"], (580, 550, 120, 50), 0, 5)
            screen.blit(txt["lopeta"], (583, 555))
            for i in range(len(txt["kick_screen"])):
                screen.blit(txt["kick_screen"][i], (150, 150+40*i))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect(590, 550, 100, 50).collidepoint(mousepos):
                    reset()
                    exit()

            FPS.tick(60)
            pygame.display.flip()

# Upgrades
upgrade = [
    {"level": 0, "cost": 0}, # Multitask
    {"level": 0, "cost": 0}, # Motivation
    {"level": 0, "cost": 0}, # Number of GPTs
    {"level": 0, "cost": 0}, # GPT version
    {"level": 0, "cost": 0}, # Rank up
]

base_cost = [10, 1000, 100000, 100000]
price_multiplier = [1.1, 1.1, 1.3, 1.3]

# Load images
for png in data.img.keys():
    img[png] = pygame.image.load(img[png]).convert_alpha()

# Texture and image surface scaling
img["panosta"] = pygame.transform.scale_by(img["panosta"], 10)
img["top_bar"] = pygame.transform.scale_by(img["top_bar"], 3.2)
img["upgrade_zone"] = pygame.transform.scale_by(img["upgrade_zone"], 6)
img["upgrade_unit"] = pygame.transform.scale_by(img["upgrade_unit"], 4)
txt["opintopisteet"] = pygame.transform.scale_by(txt["opintopisteet"], 3)
txt["reset"] = pygame.transform.scale_by(txt["reset"], 1.3)
txt["sulje"] = pygame.transform.scale_by(txt["sulje"], 2)
txt["jatka"] = pygame.transform.scale_by(txt["jatka"], 2)
txt["lopeta"] = pygame.transform.scale_by(txt["lopeta"], 2)
txt["pvm"] = pygame.transform.scale_by(txt["pvm"], 2)
txt["tj"] = pygame.transform.scale_by(txt["tj"], 2)
txt["opiskeluoikeus"] = pygame.transform.scale_by(txt["opiskeluoikeus"], 2)
for i in range(len(txt["main_screen"])):
            txt["main_screen"][i] = pygame.transform.scale_by(txt["main_screen"][i], 1.5)
for i in range(len(txt["win_screen"])):
            txt["win_screen"][i] = pygame.transform.scale_by(txt["win_screen"][i], 1.5)
for i in range(len(txt["lose_screen"])):
            txt["lose_screen"][i] = pygame.transform.scale_by(txt["lose_screen"][i], 1.5)
for i in range(len(txt["kick_screen"])):
            txt["kick_screen"][i] = pygame.transform.scale_by(txt["kick_screen"][i], 1.5)

# Hard reset (empty savedata.txt)
if is_empty("savedata.txt") == True:
    reset()
    load()
else:
    load()

# Main loop
while True:

    screen.fill((200, 200, 200))

    # Dynamic variables
    mousepos = pygame.mouse.get_pos()
    tj = date_deadline - date_current

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save()
            exit()

        # Score button animation and functionality
        if (event.type == pygame.MOUSEBUTTONDOWN and hitbox.collidepoint(mousepos)) or event.type == pygame.KEYDOWN:
            img["panosta_scaled"] = pygame.transform.scale(img["panosta"], (456, 126))
            button_pressed = True
        if (event.type == pygame.MOUSEBUTTONUP and hitbox.collidepoint(mousepos)) or event.type == pygame.KEYUP:
            button_pressed = False

            # Score formula (Manual)
            score += (upgrade[0]["level"]+1)*(upgrade[1]["level"]+1)**rank[rank_current][2]

        # Upgrade mode button
        if upgrade_mode == "1x" and pygame.Rect(825, 600, 75, 40).collidepoint(mousepos) and event.type == pygame.MOUSEBUTTONDOWN:
            upgrade_mode = "max"
        elif upgrade_mode == "max" and pygame.Rect(825, 600, 75, 40).collidepoint(mousepos) and event.type == pygame.MOUSEBUTTONDOWN:
            upgrade_mode = "1x"

        cost_max = [0, 0, 0, 0]
        level_max = [0, 0, 0, 0]
        for i in range(4):
            while True:
                cost_max[i] += base_cost[i]*price_multiplier[i]**(upgrade[i]["level"]+level_max[i])
                if cost_max[i] > score:
                    cost_max[i] -= base_cost[i]*price_multiplier[i]**(upgrade[i]["level"]+level_max[i])
                    break
                level_max[i] += 1

        # Reset button
        if pygame.Rect(930, 10, 75, 30).collidepoint(mousepos) and event.type == pygame.MOUSEBUTTONDOWN:
            reset()
            load()

        # Purchase system
        for i in range(4):
            if score >= upgrade[i]["cost"]:
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect(825, 100*(i+1), 400, 75).collidepoint(mousepos):
                    if upgrade_mode == "1x":
                        upgrade[i]["level"] += 1
                        score -= upgrade[i]["cost"]
                    elif upgrade_mode == "max":
                        upgrade[i]["level"] += level_max[i]
                        score -= cost_max[i]
        if score >= upgrade[4]["cost"]:
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.Rect(825, 100*5, 400, 75).collidepoint(mousepos):
                rank_current += 1
                score -= upgrade[4]["cost"]
                upgrade[4]["cost"] = rank[rank_current][1]
                upgrade[4]["level"] = rank[rank_current][0]
                if rank_current == 6:
                    win_screen()

    # Upgrade cost scaling
    for i in range(4):
        upgrade[i]["cost"] = base_cost[i] * price_multiplier[i]**upgrade[i]["level"]

    # Score formula
    score += upgrade[2]["level"]*upgrade[3]["level"]**(rank[rank_current][2]*1.2)

    # Updates to dynamic texts
    txt["score"] = font.render(convert_num(score), True, 0)
    txt["score"] = pygame.transform.scale_by(txt["score"], 3)
    txt["current_time"] = font.render(date_current.strftime("%d.%m.%Y"), True, 0)
    txt["current_time"] = pygame.transform.scale_by(txt["current_time"], 2)
    txt["deadline"] = font.render(date_deadline.strftime("%d.%m.%Y"), True, 0)
    txt["deadline"] = pygame.transform.scale_by(txt["deadline"], 2)
    txt["tj_time"] = font.render(str(f"{tj.days} päivää"), True, 2)
    txt["tj_time"] = pygame.transform.scale_by(txt["tj_time"], 2)
    if rank_current >= 6:
        txt["deadline"] = font.render("-.-.-", True, 0)
        txt["deadline"] = pygame.transform.scale_by(txt["deadline"], 2)
        txt["tj_time"] = font.render("- päivää", True, 2)
        txt["tj_time"] = pygame.transform.scale_by(txt["tj_time"], 2)
    
    if upgrade_mode == "1x":
        txt["upgrade0_level"] = font.render(f"Multitaskaus {convert_num(upgrade[0]["level"])}", True, 0)
        txt["upgrade1_level"] = font.render(f"Motivaatiokerroin {convert_num(upgrade[1]["level"])}", True, 0)
        txt["upgrade2_level"] = font.render(f"ChatGPT lkm {convert_num(upgrade[2]["level"])}", True, 0)
        txt["upgrade3_level"] = font.render(f"Versio:  GPT-{convert_num(upgrade[3]["level"])}", True, 0)
        txt["upgrade4_level"] = font.render(f"Rank {upgrade[4]["level"]}", True, 0)
    elif upgrade_mode == "max":
        txt["upgrade0_level"] = font.render(f"Multitaskaus {convert_num(upgrade[0]["level"])}+{level_max[0]}", True, 0)
        txt["upgrade1_level"] = font.render(f"Motivaatiokerroin {convert_num(upgrade[1]["level"])}+{level_max[1]}", True, 0)
        txt["upgrade2_level"] = font.render(f"ChatGPT lkm {convert_num(upgrade[2]["level"])}+{level_max[2]}", True, 0)
        txt["upgrade3_level"] = font.render(f"Versio:  GPT-{convert_num(upgrade[3]["level"])}+{level_max[3]}", True, 0)
        txt["upgrade4_level"] = font.render(f"Rank {upgrade[4]["level"]}", True, 0)
    txt["upgrade_mode"] = font.render(upgrade_mode, True, 0)
    txt["upgrade_mode"] = pygame.transform.scale_by(txt["upgrade_mode"], 2)
    for i in range(5):
        txt[f"upgrade{i}_cost"] = font.render(f"Rank up {convert_num(upgrade[i]["cost"])} op", True, 0)
        txt[f"upgrade{i}_level"] = pygame.transform.scale_by(txt[f"upgrade{i}_level"], 2)

    # sprite placement
    screen.blit(img["top_bar"], (0, 0))
    screen.blit(img["upgrade_zone"], (800, 75))
    pygame.draw.rect(screen, color["grey"], (825, 600, 75, 40), 0 , 5) # upgrade mode
    pygame.draw.rect(screen, color["grey"], (930, 10, 75, 30), 0, 5) # reset
    if button_pressed:
        screen.blit(img["panosta_scaled"], (52, 227))
    else:
        screen.blit(img["panosta"], (50, 225))

    for i in range(5):
        if score >= upgrade[i]["cost"]:
            pygame.draw.rect(screen, color["green"], (825, 100*(i+1), 400, 75))
        else:
            pygame.draw.rect(screen, color["red"], (825, 100*(i+1), 400, 75))

    # txt placement
    screen.blit(txt["opintopisteet"], (50, 75))
    screen.blit(txt["score"], (55, 150))  
    screen.blit(txt["reset"], (934, 12))
    screen.blit(txt["upgrade_mode"], txt["upgrade_mode"].get_rect(center=(860, 620)))
    screen.blit(txt["current_time"], (55, 450))
    screen.blit(txt["deadline"], (55, 550))
    screen.blit(txt["pvm"], (55, 400))
    screen.blit(txt["opiskeluoikeus"], (55, 500))
    screen.blit(txt["tj"], (55, 600))
    screen.blit(txt["tj_time"], (55, 650))
    for i in range(5):
        screen.blit(txt[f"upgrade{i}_level"], (830, 100*(i+1)+5))
        screen.blit(txt[f"upgrade{i}_cost"], (830, 100*(i+1)+50))

    # Tutorial
    if overlay == True:
        start_screen()

    # Game over menu
    if tj.days <= 0 and rank_current < 6:
        lose_screen()
    
    # Secret ending
    if score >= 1e+66:
         kick_screen()

    # Clock
    date_current += timedelta(minutes=73)
    FPS.tick(60)
    pygame.display.flip()