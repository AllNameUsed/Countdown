import pygame
import sys
import time
import letters
import numbers

pygame.init()
pygame.mixer.init() 
pygame.mixer.music.set_volume(0.7) 

# Screen dimensions
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Countdown')

# Colors
BLUE = (0, 150, 255)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

# Fonts
FONT = pygame.font.SysFont('Arial', 36)
SMALL_FONT = pygame.font.SysFont('Arial', 24)

# Game states
MAIN_MENU = 'main_menu'
NUMBERS_GAME = 'numbers_game'
LETTERS_GAME = 'letters_game'
NUMBERS_TIMER = 'numbers_timer'
LETTERS_TIMER = 'letters_timer'
NUMBERS_RESULT = 'numbers_result'
LETTERS_RESULT = 'letters_result'

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)
    
def play_countdown_music():
    pygame.mixer.music.load('assets/countdown.mp3')
    pygame.mixer.music.play(loops=-1)

def main_menu(game_state, events):
    # Draw buttons
    numbers_button = pygame.Rect(WIDTH/2 - 100, HEIGHT/2 - 50, 200, 50)
    letters_button = pygame.Rect(WIDTH/2 - 100, HEIGHT/2 + 20, 200, 50)

    pygame.draw.rect(SCREEN, WHITE, numbers_button)
    pygame.draw.rect(SCREEN, WHITE, letters_button)

    draw_text('Numbers', FONT, BLACK, SCREEN, WIDTH/2, HEIGHT/2 - 25)
    draw_text('Letters', FONT, BLACK, SCREEN, WIDTH/2, HEIGHT/2 + 45)

    # Event handling
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if numbers_button.collidepoint((mx, my)):
                game_state = NUMBERS_GAME
            elif letters_button.collidepoint((mx, my)):
                game_state = LETTERS_GAME
    return game_state

def numbers_game_ui(game_state, events, numbers_selections):
    big_buttons = []
    small_buttons = []

    # Draw number slots and choices
    for i in range(6):
        x = 100 + i * 110
        y = HEIGHT/2 - 50
        slot_rect = pygame.Rect(x, y, 100, 150)
        pygame.draw.rect(SCREEN, WHITE, slot_rect, 2)

        if len(numbers_selections) > i:
            draw_text(numbers_selections[i], SMALL_FONT, WHITE, SCREEN, x + 50, y + 75)
        else:
            big_button = pygame.Rect(x, y, 100, 70)
            small_button = pygame.Rect(x, y + 80, 100, 70)
            big_buttons.append(big_button)
            small_buttons.append(small_button)
            pygame.draw.rect(SCREEN, WHITE, big_button)
            pygame.draw.rect(SCREEN, WHITE, small_button)
            draw_text('Big', SMALL_FONT, BLACK, SCREEN, x + 50, y + 35)
            draw_text('Small', SMALL_FONT, BLACK, SCREEN, x + 50, y + 115)

    # Start button
    start_button = pygame.Rect(WIDTH/2 - 50, HEIGHT - 100, 100, 50)
    pygame.draw.rect(SCREEN, WHITE, start_button)
    draw_text('Start', FONT, BLACK, SCREEN, WIDTH/2, HEIGHT - 75)

    # Event handling
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            for i in range(6):
                if len(numbers_selections) < 6:
                    big_button = pygame.Rect(100 + i * 110, HEIGHT/2 - 50, 100, 70)
                    small_button = pygame.Rect(100 + i * 110, HEIGHT/2 + 30, 100, 70)
                    if big_button.collidepoint((mx, my)):
                        numbers_selections.append('Big')
                    elif small_button.collidepoint((mx, my)):
                        numbers_selections.append('Small')
            if start_button.collidepoint((mx, my)) and len(numbers_selections) == 6:
                game_state = NUMBERS_TIMER
                play_countdown_music()  
    return game_state, numbers_selections

def letters_game_ui(game_state, events, letters_selections):
    vowel_buttons = []
    consonant_buttons = []

    # Draw letter slots and choices
    for i in range(9):
        x = 50 + i * 80
        y = HEIGHT/2 - 50
        slot_rect = pygame.Rect(x, y, 70, 150)
        pygame.draw.rect(SCREEN, WHITE, slot_rect, 2)

        if len(letters_selections) > i:
            draw_text(letters_selections[i], SMALL_FONT, WHITE, SCREEN, x + 35, y + 75)
        else:
            vowel_button = pygame.Rect(x, y, 70, 70)
            consonant_button = pygame.Rect(x, y + 80, 70, 70)
            vowel_buttons.append(vowel_button)
            consonant_buttons.append(consonant_button)
            pygame.draw.rect(SCREEN, WHITE, vowel_button)
            pygame.draw.rect(SCREEN, WHITE, consonant_button)
            draw_text('Vowel', SMALL_FONT, BLACK, SCREEN, x + 35, y + 35)
            draw_text('Cons', SMALL_FONT, BLACK, SCREEN, x + 35, y + 115)

    # Start button
    start_button = pygame.Rect(WIDTH/2 - 50, HEIGHT - 100, 100, 50)
    pygame.draw.rect(SCREEN, WHITE, start_button)
    draw_text('Start', FONT, BLACK, SCREEN, WIDTH/2, HEIGHT - 75)

    # Event handling
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            for i in range(9):
                if len(letters_selections) < 9:
                    vowel_button = pygame.Rect(50 + i * 80, HEIGHT/2 - 50, 70, 70)
                    consonant_button = pygame.Rect(50 + i * 80, HEIGHT/2 + 30, 70, 70)
                    if vowel_button.collidepoint((mx, my)):
                        letters_selections.append('Vowel')
                    elif consonant_button.collidepoint((mx, my)):
                        letters_selections.append('Cons')
            if start_button.collidepoint((mx, my)) and len(letters_selections) == 9:
                game_state = LETTERS_TIMER
                play_countdown_music()  
    return game_state, letters_selections

def main():
    clock = pygame.time.Clock()
    game_state = MAIN_MENU
    running = True

    numbers_selections = []
    letters_selections = []
    numbers_values = []
    letters_values = []

    start_time = None

    goal_number = None
    goal_solution = None


    while running:
        SCREEN.fill(BLUE)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        if game_state == MAIN_MENU:
            game_state = main_menu(game_state, events)
            numbers_selections = []
            letters_selections = []

        elif game_state == NUMBERS_GAME:
            game_state, numbers_selections = numbers_game_ui(game_state, events, numbers_selections)
            if game_state == NUMBERS_TIMER:
                numbers_values = numbers.generate_numbers(numbers_selections)
                # Generate the goal number and solution
                goal_number, goal_solution = numbers.generate_random_goal(numbers_values)
                start_time = time.time()

        elif game_state == LETTERS_GAME:
            game_state, letters_selections = letters_game_ui(game_state, events, letters_selections)
            if game_state == LETTERS_TIMER:
                letters_values = letters.generate_letters(letters_selections)
                start_time = time.time()

        elif game_state == NUMBERS_TIMER:
            # Display goal number
            draw_text(f'Goal: {goal_number}', FONT, WHITE, SCREEN, WIDTH/2, 50)

            # Display numbers
            for i in range(6):
                x = 100 + i * 110
                y = HEIGHT/2 - 50
                slot_rect = pygame.Rect(x, y, 100, 150)
                pygame.draw.rect(SCREEN, WHITE, slot_rect)
                if numbers_values:
                    draw_text(str(numbers_values[i]), FONT, BLACK, SCREEN, x + 50, y + 75)
                else:
                    draw_text('?', FONT, BLACK, SCREEN, x + 50, y + 75)

            # Display timer
            elapsed_time = time.time() - start_time
            remaining_time = max(0, 30 - elapsed_time)
            draw_text(f'Time: {int(remaining_time)}', FONT, WHITE, SCREEN, WIDTH/2, 100)

            if remaining_time <= 0:
                # Reveal button
                reveal_button = pygame.Rect(WIDTH/2 - 100, HEIGHT - 100, 200, 50)
                pygame.draw.rect(SCREEN, WHITE, reveal_button)
                draw_text('Answer', FONT, BLACK, SCREEN, WIDTH/2, HEIGHT - 75)
                for event in events:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mx, my = pygame.mouse.get_pos()
                        if reveal_button.collidepoint((mx, my)):
                            game_state = NUMBERS_RESULT


        elif game_state == LETTERS_TIMER:
            # Display letters
            for i in range(9):
                x = 50 + i * 80
                y = HEIGHT/2 - 50
                slot_rect = pygame.Rect(x, y, 70, 150)
                pygame.draw.rect(SCREEN, WHITE, slot_rect)
                if letters_values:
                    draw_text(letters_values[i], FONT, BLACK, SCREEN, x + 35, y + 75)
                else:
                    draw_text('?', FONT, BLACK, SCREEN, x + 35, y + 75)

            # Display timer
            elapsed_time = time.time() - start_time
            remaining_time = max(0, 30 - elapsed_time)
            draw_text(f'Time: {int(remaining_time)}', FONT, WHITE, SCREEN, WIDTH/2, 50)

            if remaining_time <= 0:
                # Reveal button
                reveal_button = pygame.Rect(WIDTH/2 - 100, HEIGHT - 100, 200, 50)
                pygame.draw.rect(SCREEN, WHITE, reveal_button)
                draw_text('Answer', FONT, BLACK, SCREEN, WIDTH/2, HEIGHT - 75)
                for event in events:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mx, my = pygame.mouse.get_pos()
                        if reveal_button.collidepoint((mx, my)):
                            game_state = LETTERS_RESULT

        elif game_state == NUMBERS_RESULT:
            pygame.mixer.music.stop()
            # Display the solution
            draw_text('Solution:', FONT, WHITE, SCREEN, WIDTH/2, HEIGHT/2 - 50)
            draw_text(goal_solution, FONT, WHITE, SCREEN, WIDTH/2, HEIGHT/2)

            # Back button
            back_button = pygame.Rect(WIDTH/2 - 50, HEIGHT - 100, 100, 50)
            pygame.draw.rect(SCREEN, WHITE, back_button)
            draw_text('Back', FONT, BLACK, SCREEN, WIDTH/2, HEIGHT - 75)
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    if back_button.collidepoint((mx, my)):
                        game_state = MAIN_MENU

        elif game_state == LETTERS_RESULT:
            pygame.mixer.music.stop()
            # Display the top 5 words
            top_words = letters.find_top_words(letters_values)
            
            # Define the area where we want to display the words
            total_display_height = 300  # Total height for displaying words (adjust as needed)
            top_margin = HEIGHT / 2 - total_display_height / 2  # Starting Y position
            spacing = total_display_height / (len(top_words) + 1)  # Calculate spacing between lines
            
            # Draw the heading
            heading_y = top_margin
            draw_text('Top 5 Words:', FONT, WHITE, SCREEN, WIDTH/2, heading_y)
            
            # Draw each word with even spacing
            for idx, word in enumerate(top_words):
                y_position = heading_y + (idx + 1) * spacing
                draw_text(f"{idx+1}. {word}", FONT, WHITE, SCREEN, WIDTH/2, y_position)
            
            # Back button
            back_button = pygame.Rect(WIDTH/2 - 50, HEIGHT - 100, 100, 50)
            pygame.draw.rect(SCREEN, GRAY, back_button)
            draw_text('Back', FONT, BLACK, SCREEN, WIDTH/2, HEIGHT - 75)
            
            # Event handling for the back button
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    if back_button.collidepoint((mx, my)):
                        game_state = MAIN_MENU


        pygame.display.flip()
        clock.tick(30)
        
    pygame.mixer.music.stop()
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
