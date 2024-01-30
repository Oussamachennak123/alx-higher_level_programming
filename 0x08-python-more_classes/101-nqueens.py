#!/usr/bin/python3
import sys


def solve_n_queens(N):
    def can_place(pos, os_positions):
        for a in range(len(os_positions)):
            if os_positions[a] == pos or \
                    os_positions[a] - a == pos - len(os_positions) or \
                    os_positions[a] + a == pos + len(os_positions):
                return False
        return True

    def place_queen(os_positions, target_row, N):
        if target_row == N:
            result.append(os_positions)
            return
        for column in range(N):
            if can_place(column, os_positions):
                place_queen(os_positions + [column], target_row + 1, N)

    result = []
    place_queen([], 0, N)
    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_n_queens(N)
    for sol in solutions:
        print([[i, sol[i]] for i in range(N)])
