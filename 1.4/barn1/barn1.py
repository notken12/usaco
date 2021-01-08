"""
ID: kendotz1
LANG: PYTHON3
TASK: barn1
"""

from io import TextIOBase


def get_occupied_stalls_from_file(file: TextIOBase, _occupied_stall_count: int) -> list:
    _occupied_stalls = []
    for i in range(_occupied_stall_count):
        _occupied_stalls.append(int(file.readline().strip()))
    return _occupied_stalls


def sort_stalls_asc(_stalls:list) -> list:
    _stalls.sort()
    return _stalls


def get_gaps(_stalls: list) -> list:
    gaps = []
    for i in range(len(_stalls) - 1):
        curr = _stalls[i]
        _next = _stalls[i + 1]
        if _next - curr > 1:
            gaps.append([curr + 1, _next - 1])
    return gaps


def sort_gaps_by_size_desc(_gaps: list) -> list:
    _gaps.sort(key=lambda a: a[1] - a[0], reverse=True)
    return _gaps


def sort_gaps_by_start_asc(_gaps:list) -> list:
    _gaps.sort(key=lambda a: a[0])
    return _gaps


def cut_board(board: list, gap: list) -> list:
    board1 = [board[0], gap[0] - 1]
    board2 = [gap[1] + 1, board[1]]
    return [board1, board2]


def get_boards(_stalls: list, _max_boards: int) -> list:
    boards = []
    if _max_boards >= len(_stalls):
        return [[x, x] for x in _stalls]

    gaps = sort_gaps_by_size_desc(get_gaps(_stalls))
    cut_marks = sort_gaps_by_start_asc(gaps[:_max_boards - 1])  # get first n boards and sort them asc

    initial_board = [_stalls[0], _stalls[-1]]
    boards.append(initial_board)
    for i in range(_max_boards - 1):
        cut = cut_board(boards[i], cut_marks[i])
        boards[i] = cut[0]
        boards.append(cut[1])
    return boards


def get_covered_stalls(_boards: list) -> int:
    total = 0
    for board in _boards:
        total += board[1] - board[0] + 1
    return total


fin = open('barn1.in', 'r')
fout = open('barn1.out', 'w')

params = fin.readline().strip().split(' ')

max_boards = int(params[0])
stall_count = int(params[1])
occupied_stall_count = int(params[2])

occupied_stalls = sort_stalls_asc(get_occupied_stalls_from_file(fin, occupied_stall_count))
fout.write(str(get_covered_stalls(get_boards(occupied_stalls, max_boards))) + '\n')
