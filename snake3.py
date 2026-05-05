import pygame as p
from random import randint as r

p.init()

# ---------------- SETTINGS ----------------
W, H, C = 800, 600, 10
gW, gH = W // C, H // C

win = p.display.set_mode((W, H))
p.display.set_caption("Snake Game")

# ---------------- SCORE FILE ----------------
def get_hiscores():
    #TO DO
# ---------------- UI ----------------
def draw_button(text, x, y, w, h):
    rect = p.Rect(x, y, w, h)
    mouse = p.mouse.get_pos()

    if rect.collidepoint(mouse):
        p.draw.rect(win, (100, 100, 100), rect)
    else:
        p.draw.rect(win, (50, 50, 50), rect)

    font = p.font.SysFont(None, 30)
    txt = font.render(text, True, (255, 255, 255))
    win.blit(txt, (x + w//2 - txt.get_width()//2,
                   y + h//2 - txt.get_height()//2))

    return rect


def draw_score(score):
    font = p.font.SysFont(None, 30)
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    win.blit(text, (10, 10))

# ---------------- HIGH SCORES ----------------
def high_score_screen():
    #TO DO
# ---------------- MENU ----------------
def menu_screen():
    font = p.font.SysFont(None, 60)

    while True:
        win.fill((10, 10, 10))

        title = font.render("SNAKE GAME", True, (128, 189, 11))
        win.blit(title, (W//2 - title.get_width()//2, 120))

        start = draw_button("START", W//2 - 50, 250, 100, 50)
        scores = draw_button("HIGH SCORES", W//2 - 75, 320, 150, 50)
        quitb = draw_button("QUIT", W//2 - 50, 390, 100, 50)

        p.display.update()

        for e in p.event.get():
            if e.type == p.QUIT:
                p.quit()
                exit()

            if e.type == p.MOUSEBUTTONDOWN:
                if start.collidepoint(e.pos):
                    return "start"
                if scores.collidepoint(e.pos):
                    high_score_screen()
                if quitb.collidepoint(e.pos):
                    p.quit()
                    exit()

# ---------------- GAME ----------------
def run_game():
    clk = p.time.Clock()

    s = [(10, 13), (10, 12), (10, 11)]
    d = "R"
    score = 0

    mv = {
        "U": (0, -1),
        "D": (0, 1),
        "L": (-1, 0),
        "R": (1, 0)
    }

    def food():
        while True:
            f = (r(0, gW - 1), r(0, gH - 1))
            if f not in s:
                return p.Rect(f[0] * C, f[1] * C, C, C)

    fd = food()

    while True:
        clk.tick(12)

        for e in p.event.get():
            if e.type == p.QUIT:
                p.quit()
                exit()

            if e.type == p.KEYDOWN:
                if e.key == p.K_UP and d != "D": d = "U"
                elif e.key == p.K_DOWN and d != "U": d = "D"
                elif e.key == p.K_LEFT and d != "R": d = "L"
                elif e.key == p.K_RIGHT and d != "L": d = "R"

        # Move snake
        x, y = s[0]
        dx, dy = mv[d]
        h = (x + dx, y + dy)
        s = [h] + s[:-1]

        # Death conditions → return to menu
        if not (0 <= h[0] < gW and 0 <= h[1] < gH):
            return

        if h in s[1:]:
            return

        win.fill((30, 30, 30))

        # Draw snake
        for x, y in s:
            p.draw.rect(win, (0, 200, 0), p.Rect(x * C, y * C, C, C))

        # Draw food
        p.draw.rect(win, (200, 50, 50), fd)

        # Eat food
        if h == (fd.x // C, fd.y // C):
            s.append(s[-1])
            fd = food()
            score += 1

        # Score
        draw_score(score)

        p.display.update()

# ---------------- MAIN LOOP ----------------
while True:
    choice = menu_screen()

    if choice == "start":
        run_game()
