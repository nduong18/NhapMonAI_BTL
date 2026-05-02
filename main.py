import pygame
import sys
from maze_logic import Maze

# Khởi tạo Pygame
pygame.init()

# Cấu hình cửa sổ
WIDTH = 800
HEIGHT = 600
CELL_SIZE = 40
FPS = 20 # Tốc độ vẽ (tăng lên để vẽ nhanh hơn, giảm để chậm lại)

# Tính toán số cột và hàng
cols = WIDTH // CELL_SIZE
rows = HEIGHT // CELL_SIZE

# Thiết lập màn hình
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mô phỏng DFS tạo Mê Cung")
clock = pygame.time.Clock()

# Bảng màu (Color Palette)
DARK_GREY = (30, 30, 30)              # Nền ô chưa đi qua
VISITED_COLOR = (100, 200, 255)       # Xanh dương nhạt: ô đã đi qua
EXPLORED_COLOR = (50, 100, 200)       # Xanh dương đậm: ô đã quay lui (xong)
CURRENT_COLOR = (255, 100, 100)       # Đỏ: Đầu dò hiện tại
NEXT_COLOR = (100, 255, 100)          # Xanh lá: Ô sắp tiến tới
WALL_COLOR = (255, 255, 255)          # Trắng: Tường

def draw_cell(screen, cell, color, cell_size):
    """
    Hàm vẽ một ô với màu nền và các bức tường.
    """
    x = cell.x * cell_size
    y = cell.y * cell_size
    
    # Vẽ nền của ô (nếu có màu khác nền tối)
    if color != DARK_GREY:
        pygame.draw.rect(screen, color, (x, y, cell_size, cell_size))
    
    # Vẽ các bức tường
    # walls = [Top, Right, Bottom, Left]
    thickness = 2
    if cell.walls[0]:
        pygame.draw.line(screen, WALL_COLOR, (x, y), (x + cell_size, y), thickness)
    if cell.walls[1]:
        pygame.draw.line(screen, WALL_COLOR, (x + cell_size, y), (x + cell_size, y + cell_size), thickness)
    if cell.walls[2]:
        pygame.draw.line(screen, WALL_COLOR, (x + cell_size, y + cell_size), (x, y + cell_size), thickness)
    if cell.walls[3]:
        pygame.draw.line(screen, WALL_COLOR, (x, y + cell_size), (x, y), thickness)

def main():
    # Khởi tạo ma trận mê cung
    maze = Maze(cols, rows)
    
    # Lấy Generator từ hàm DFS của Thành viên 1
    generator = maze.generate_dfs_yield(0, 0)
    
    # Tập hợp để lưu các ô đã quay lui (hoàn tất duyệt để đổi màu)
    explored_cells = set()
    
    current_cell = None
    next_cell = None
    
    running = True
    maze_completed = False
    
    while running:
        # 1. Xử lý sự kiện Pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Bấm phím SPACE để chơi lại khi đã xong
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and maze_completed:
                    maze = Maze(cols, rows)
                    generator = maze.generate_dfs_yield(0, 0)
                    explored_cells.clear()
                    maze_completed = False
                    current_cell = None
                    next_cell = None
        
        # 2. Cập nhật logic từ Generator (Mỗi vòng lặp nhích 1 bước)
        if not maze_completed:
            try:
                # Dùng hàm next() để "gọi" generator nhả ra dữ liệu
                current_cell, next_cell = next(generator)
                
                # Ý nghĩa: next_cell là None nghĩa là hàm của bạn đang YIELD trường hợp Backtrack
                if next_cell is None:
                    explored_cells.add(current_cell)
                    
            except StopIteration:
                # Khi thuật toán chạy xong 100%, generator ném lỗi StopIteration
                maze_completed = True
                current_cell = None
                next_cell = None
                print("Tạo mê cung hoàn tất! Bấm phím SPACE để tạo lại.")
        
        # 3. Vẽ giao diện (Render)
        screen.fill(DARK_GREY)
        
        # Vẽ tất cả các ô trong mê cung
        for x in range(cols):
            for y in range(rows):
                cell = maze.grid[x][y]
                color = DARK_GREY
                
                if cell in explored_cells:
                    color = EXPLORED_COLOR
                elif cell.visited:
                    color = VISITED_COLOR
                
                draw_cell(screen, cell, color, CELL_SIZE)
        
        # Vẽ đè ô hiện tại (đầu dò) và ô next để làm nổi bật animation
        if current_cell and not maze_completed:
            draw_cell(screen, current_cell, CURRENT_COLOR, CELL_SIZE)
        if next_cell:
            draw_cell(screen, next_cell, NEXT_COLOR, CELL_SIZE)
            
        # Cập nhật màn hình
        pygame.display.flip()
        
        # 4. Điều chỉnh tốc độ khung hình (FPS)
        clock.tick(FPS)
        
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
