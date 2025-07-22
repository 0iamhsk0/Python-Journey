import random
import curses
import time

def main(stdscr):
    # Initialize
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)
    
    sh, sw = stdscr.getmaxyx()
    
    # Make sure we have enough space
    if sh < 10 or sw < 20:
        stdscr.addstr(0, 0, "Terminal too small! Need at least 10x20")
        stdscr.refresh()
        stdscr.getch()
        return

    # Initial snake position
    snk_x = sw//4
    snk_y = sh//2
    snake = [
        [snk_y, snk_x],
        [snk_y, snk_x-1],
        [snk_y, snk_x-2]
    ]

    # Food position
    food = [sh//2, sw//2]
    
    key = curses.KEY_RIGHT
    score = 0

    while True:
        next_key = stdscr.getch()
        key = key if next_key == -1 else next_key

        # Exit on 'q'
        if next_key == ord('q'):
            break

        # Check if snake hits wall or itself
        if (snake[0][0] in [0, sh-1] or 
            snake[0][1] in [0, sw-1] or 
            snake[0] in snake[1:]):
            stdscr.addstr(sh//2, sw//2-5, "GAME OVER!")
            stdscr.addstr(sh//2+1, sw//2-10, "Press any key to exit")
            stdscr.refresh()
            stdscr.getch()
            break

        new_head = [snake[0][0], snake[0][1]]

        # Movement
        if key == curses.KEY_DOWN:
            new_head[0] += 1
        elif key == curses.KEY_UP:
            new_head[0] -= 1
        elif key == curses.KEY_LEFT:
            new_head[1] -= 1
        elif key == curses.KEY_RIGHT:
            new_head[1] += 1

        snake.insert(0, new_head)

        # Check if food eaten
        if snake[0] == food:
            score += 1
            food = None
            while food is None:
                nf = [
                    random.randint(1, sh-2),
                    random.randint(1, sw-2)
                ]
                food = nf if nf not in snake else None
        else:
            tail = snake.pop()
            try:
                stdscr.addch(tail[0], tail[1], ' ')
            except:
                pass

        # Clear screen and redraw
        stdscr.clear()
        
        # Draw border
        for i in range(sh):
            try:
                stdscr.addch(i, 0, '|')
                stdscr.addch(i, sw-1, '|')
            except:
                pass
        for i in range(sw):
            try:
                stdscr.addch(0, i, '-')
                stdscr.addch(sh-1, i, '-')
            except:
                pass
        
        # Draw snake
        for segment in snake:
            try:
                stdscr.addch(segment[0], segment[1], '#')
            except:
                pass
        
        # Draw food
        try:
            stdscr.addch(food[0], food[1], '*')
        except:
            pass
        
        # Display score and instructions
        try:
            stdscr.addstr(1, 2, f"Score: {score}")
            stdscr.addstr(2, 2, "Use arrow keys to move, 'q' to quit")
        except:
            pass
        
        stdscr.refresh()
        time.sleep(0.1)

if __name__ == '__main__':
    curses.wrapper(main)
