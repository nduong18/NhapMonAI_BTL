import random


class Cell:
    def __init__(self, x, y):
        # Toa do x, y cua o trong ma tran
        self.x = x
        self.y = y

        # Trang thai danh dau o da duoc di qua
        self.visited = False

        # Mang luu trang thai 4 buc tuong: [Top, Right, Bottom, Left]
        # True nghia la tuong chua bi pha, False la da pha
        self.walls = [True, True, True, True]


class Maze:
    def __init__(self, cols, rows):
        # Kich thuoc ma tran (so cot, so hang)
        self.cols = cols
        self.rows = rows

        # Khoi tao ma tran 2 chieu chua cac doi tuong Cell
        self.grid = [[Cell(x, y) for y in range(rows)] for x in range(cols)]

    def index(self, x, y):
        # Kiem tra xem toa do co bi lech ra ngoai ban do khong
        if x < 0 or y < 0 or x > self.cols - 1 or y > self.rows - 1:
            return None
        return self.grid[x][y]

    def check_neighbors(self, cell):
        # Tao danh sach cac hang xom chua duoc tham
        neighbors = []

        top = self.index(cell.x, cell.y - 1)
        right = self.index(cell.x + 1, cell.y)
        bottom = self.index(cell.x, cell.y + 1)
        left = self.index(cell.x - 1, cell.y)

        # Neu ton tai va chua visited thi dua vao danh sach
        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)

        # Neu co it nhat 1 hang xom, chon ngau nhien 1 o
        if len(neighbors) > 0:
            return random.choice(neighbors)
        else:
            return None

    def remove_walls(self, a, b):
        # Tinh do lech toa do giua o hien tai (a) va o tiep theo (b) de pha tuong
        dx = a.x - b.x
        if dx == 1:
            # b nam ben trai a -> pha tuong trai cua a va tuong phai cua b
            a.walls[3] = False
            b.walls[1] = False
        elif dx == -1:
            # b nam ben phai a
            a.walls[1] = False
            b.walls[3] = False

        dy = a.y - b.y
        if dy == 1:
            # b nam phia tren a
            a.walls[0] = False
            b.walls[2] = False
        elif dy == -1:
            # b nam phia duoi a
            a.walls[2] = False
            b.walls[0] = False

    def generate_dfs_yield(self, start_x=0, start_y=0):
        # Khoi tao stack luu vet duong di
        stack = []

        # Chon o bat dau
        current = self.grid[start_x][start_y]
        current.visited = True
        stack.append(current)

        # Vong lap chinh cua DFS
        while len(stack) > 0:
            # Nhin vao o cuoi cung trong stack (khong xoa)
            current = stack[-1]

            # Tim hang xom
            next_cell = self.check_neighbors(current)

            if next_cell:
                # Da tim thay duong di moi
                next_cell.visited = True

                # Pha tuong giua 2 o
                self.remove_walls(current, next_cell)

                # Dua o moi vao stack
                stack.append(next_cell)

                # YIELD: Phat tin hieu cho UI biet la dang DI TOI
                yield current, next_cell
            else:
                # Gap ngo cut, lay o hien tai ra khoi stack
                stack.pop()

                # YIELD: Phat tin hieu cho UI biet la dang QUAY LUI (Backtrack)
                # Truyen next_cell la None de UI doi mau o current thanh mau "da duyet xong"
                yield current, None


if __name__ == "__main__":
    # Test voi ma tran nho 5x5 cho de nhin
    maze = Maze(5, 5)

    # Khoi tao generator
    generator = maze.generate_dfs_yield(0, 0)

    step = 1
    # Vong lap for tu dong goi next() tren generator cua ban
    for current, next_cell in generator:
        if next_cell is not None:
            print(f"Buoc {step}: Tien toi tu ({current.x}, {current.y}) -> ({next_cell.x}, {next_cell.y})")
        else:
            print(f"Buoc {step}: Quay lui tai ({current.x}, {current.y})")
        step += 1

    print("Tao me cung hoan tat!")