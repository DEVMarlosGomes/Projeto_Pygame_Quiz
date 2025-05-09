import pygame
import sys

pygame.init()

# Tela
WIDTH, HEIGHT = 1920, 1080 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎮 Gênio Quiz Atualizado")

# Fontes
font = pygame.font.SysFont("comic sans ms", 28)
big_font = pygame.font.SysFont("comic sans ms", 48, bold=True)
small_font = pygame.font.SysFont("comic sans ms", 18)
tiny_font = pygame.font.SysFont("comic sans ms", 16)

# Cores
BG_COLOR = (255, 255, 255)
TEXT_COLOR = (0, 0, 0)
OPTION_COLOR = (200, 230, 255)
OPTION_SELECTED_COLOR = (100, 180, 255)
CORRECT_COLOR = (0, 200, 100)
WRONG_COLOR = (230, 50, 50)

# Imagens
credit_image = pygame.image.load("TelaCréditos.png")
credit_image = pygame.transform.scale(credit_image, (WIDTH, HEIGHT))

# Perguntas
questions = [
    {"question": "🌍 Qual país sediou a Copa do Mundo de 2022?", "options": ["Brasil", "Catar", "Alemanha"], "correct": 1},
    {"question": "🦠 Em que ano a pandemia de COVID-19 foi declarada?", "options": ["2019", "2020", "2021"], "correct": 1},
    {"question": "🚀 Qual bilionário fez o primeiro voo suborbital em 2021?", "options": ["Elon Musk", "Jeff Bezos", "Mark Zuckerberg"], "correct": 1},
    {"question": "🧠 Qual é o maior órgão do corpo humano?", "options": ["Fígado", "Cérebro", "Pele"], "correct": 2},
    {"question": "🔢 Quanto é 9 x 7?", "options": ["63", "72", "56"], "correct": 0},
    {"question": "🇧🇷 Qual é a capital do Brasil?", "options": ["São Paulo", "Rio de Janeiro", "Brasília"], "correct": 2},
    {"question": "🐶 Quantas patas tem uma aranha?", "options": ["6", "8", "10"], "correct": 1},
    {"question": "🎬 Qual filme ganhou o Oscar de Melhor Filme em 2020?", "options": ["1917", "Parasita", "Coringa"], "correct": 1},
    {"question": "⚡ Quem descobriu a eletricidade?", "options": ["Isaac Newton", "Albert Einstein", "Benjamin Franklin"], "correct": 2},
    {"question": "🎵 Qual cantor ficou famoso com 'Blinding Lights'?", "options": ["The Weeknd", "Drake", "Bruno Mars"], "correct": 0},
    {"question": "🧊 Qual é a fórmula química da água?", "options": ["H2O", "CO2", "NaCl"], "correct": 0},
    {"question": "🌌 Quantos planetas há no sistema solar?", "options": ["7", "8", "9"], "correct": 1},
    {"question": "🦄 Quantas cores tem o arco-íris?", "options": ["6", "7", "8"], "correct": 1},
    {"question": "🖥️ Quem criou a Microsoft?", "options": ["Steve Jobs", "Bill Gates", "Mark Zuckerberg"], "correct": 1},
    {"question": "🔒 O que significa a sigla 'www'?", "options": ["World Web Wide", "World Wide Web", "Web World Wide"], "correct": 1},
    {"question": "🧩 CHARADA: O que é pequeno de dia e grande à noite?", "options": ["Sombra", "Estrela", "Lua"], "correct": 0},
    {"question": "❓ CHARADA: O que tem dentes mas não morde?", "options": ["Tesoura", "Pente", "Garfo"], "correct": 1},
    {"question": "🕵️ CHARADA: Quanto mais você tira, maior fica. O que é?", "options": ["Buraco", "Segredo", "Roupa"], "correct": 0},
    {"question": "🧮 Qual o resultado de (2 + 2) x 2?", "options": ["6", "8", "10"], "correct": 0},
    {"question": "🏛️ Quem foi o primeiro presidente do Brasil?", "options": ["Getúlio Vargas", "Deodoro da Fonseca", "Dom Pedro II"], "correct": 1},
    {"question": "📅 Em que ano o Brasil foi descoberto?", "options": ["1500", "1492", "1822"], "correct": 0},
    {"question": "🎮 Qual console pertence à Nintendo?", "options": ["Xbox", "PlayStation", "Switch"], "correct": 2},
    {"question": "🧪 Qual elemento tem símbolo 'O'?", "options": ["Ouro", "Oxigênio", "Ósmio"], "correct": 1},
    {"question": "🐢 Qual desses animais é um réptil?", "options": ["Sapo", "Jacaré", "Golfinho"], "correct": 1},
    {"question": "🧙 CHARADA: Qual a palavra que começa e termina com a mesma letra, mas tem apenas uma letra?", "options": ["Letra", "Envelope", "Livro"], "correct": 1}
]

current_question = 0
score = 0
selected = 0
game_over = False
in_start_screen = True
show_wrong_animation = False
show_credits = False


def draw_start_screen():
    screen.fill(BG_COLOR)
    title = big_font.render("PyGame Quiz", True, TEXT_COLOR)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - 50))

    left_text = tiny_font.render("Senai Morvan - SP - BR", True, TEXT_COLOR)
    screen.blit(left_text, (10, HEIGHT - 30))

    right_text = tiny_font.render("Group Pygame : Marlos, Leticia, Juan, Leonardo", True, TEXT_COLOR)
    screen.blit(right_text, (WIDTH - right_text.get_width() - 10, HEIGHT - 30))

    pygame.display.flip()


def draw_question():
    screen.fill(BG_COLOR)
    q = questions[current_question]
    title_text = big_font.render(f"Pergunta {current_question + 1}/{len(questions)}", True, TEXT_COLOR)
    screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, 30))

    question_lines = q["question"].split("\n")
    for idx, line in enumerate(question_lines):
        question_text = font.render(line, True, TEXT_COLOR)
        screen.blit(question_text, (100, 120 + idx * 35))

    for i, option in enumerate(q["options"]):
        box_rect = pygame.Rect(150, 240 + i * 100, 980, 70)
        color = OPTION_SELECTED_COLOR if i == selected else OPTION_COLOR
        pygame.draw.rect(screen, color, box_rect, border_radius=15)
        text = font.render(option, True, TEXT_COLOR)
        screen.blit(text, (box_rect.x + 20, box_rect.y + 20))

    pygame.display.flip()


def draw_end_screen():
    screen.fill(BG_COLOR)
    emoji = "🎉" if score > len(questions) * 0.8 else "👍" if score > 0 else "😅"
    msg = "Parabéns!" if score > len(questions) * 0.8 else "Bom trabalho!" if score > 0 else "Tente novamente!"
    color = CORRECT_COLOR if score > len(questions) * 0.8 else (255, 165, 0) if score > 0 else WRONG_COLOR

    result_text = big_font.render(f"{emoji} {msg}", True, color)
    score_text = font.render(f"Você acertou {score} de {len(questions)} perguntas.", True, TEXT_COLOR)

    screen.blit(result_text, (WIDTH//2 - result_text.get_width()//2, HEIGHT//2 - 80))
    screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2 + 10))
    pygame.display.flip()
    pygame.time.wait(5000)
    show_credits_screen()


def draw_wrong_animation():
    screen.fill(WRONG_COLOR)
    text = big_font.render("❌ LOOSER! Você errou!", True, (255, 255, 255))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(3000)


def show_credits_screen():
    scroll_y = HEIGHT
    while scroll_y > -200:
        screen.blit(credit_image, (0, 0))
        credit_lines = [
            "Marlos Gomes (P.O)",
            "Leonardo Silva (Scrum Master)",
            "Leticia Rosa (DEV & Scrum Master)",
            "Juan (DEV)"
        ]
        for i, line in enumerate(credit_lines):
            text = big_font.render(line, True, (255, 255, 255))
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, scroll_y + i * 60))
        pygame.display.flip()
        pygame.time.wait(50)
        scroll_y -= 5

# Loop principal
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)
    if show_wrong_animation:
        draw_wrong_animation()
        in_start_screen = True
        current_question = 0
        score = 0
        selected = 0
        show_wrong_animation = False
        continue

    if in_start_screen:
        draw_start_screen()
    elif not game_over:
        draw_question()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if in_start_screen:
                in_start_screen = False
            elif not game_over:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(questions[current_question]["options"])
                elif event.key == pygame.K_UP:
                    selected = (selected - 1) % len(questions[current_question]["options"])
                elif event.key == pygame.K_RETURN:
                    if selected == questions[current_question]["correct"]:
                        score += 1
                        current_question += 1
                        selected = 0
                        if current_question >= len(questions):
                            game_over = True
                            draw_end_screen()
                    else:
                        show_wrong_animation = True

pygame.quit()
sys.exit()
