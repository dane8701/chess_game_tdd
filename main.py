from piece import Piece


movement_range = {
    'pawn': [(1, 0)],  
    'rook': [(-1, 0), (0, 1), (1, 0), (0, -1)],  
    'knight': [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)],  
    'bishop': [(-1, -1), (-1, 1), (1, 1), (1, -1)],  
    'queen': [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)],  
    'king': [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)],  
}

capture_range = {
    'pawn': [(-1, -1), (-1, 1)],  
    'rook': [(-1, 0), (0, 1), (1, 0), (0, -1)],  
    'knight': [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)],  
    'bishop': [(-1, -1), (-1, 1), (1, 1), (1, -1)],  
    'queen': [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)],  
    'king': [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)],  
}

chess_board = [[' ' for _ in range(8)] for _ in range(8)]

white_pieces = []
for piece_type in movement_range:
    white_pieces.extend([Piece('white', piece_type, movement_range[piece_type], capture_range[piece_type]) for _ in range(2 if piece_type != 'pawn' else 8)])


black_pieces = []
for piece_type in movement_range:
    black_pieces.extend([Piece('black', piece_type, movement_range[piece_type], capture_range[piece_type]) for _ in range(2 if piece_type != 'pawn' else 8)])


for i in range(8):
    chess_board[1][i] = white_pieces[i]  
chess_board[0][0] = white_pieces[8]  
chess_board[0][7] = white_pieces[9]  
chess_board[0][1] = white_pieces[10]  
chess_board[0][6] = white_pieces[11]  
chess_board[0][2] = white_pieces[12]  
chess_board[0][5] = white_pieces[13]  
chess_board[0][3] = white_pieces[14]  
chess_board[0][4] = white_pieces[15]  


for i in range(8):
    chess_board[6][i] = black_pieces[i]  
chess_board[7][0] = black_pieces[8]  
chess_board[7][7] = black_pieces[9]  
chess_board[7][1] = black_pieces[10]  
chess_board[7][6] = black_pieces[11]  
chess_board[7][2] = black_pieces[12]  
chess_board[7][5] = black_pieces[13]  
chess_board[7][3] = black_pieces[14]  
chess_board[7][4] = black_pieces[15]


print()
Piece.move_piece(chess_board, (1, 0), (2, 0))  
Piece.move_piece(chess_board, (2, 0), (3, 0))  
Piece.move_piece(chess_board, (3, 0), (4, 0))  
Piece.move_piece(chess_board, (4, 0), (5, 0))  
Piece.move_piece(chess_board, (5, 0), (6, 1))
Piece.move_piece(chess_board, (6, 1), (7, 0))
print()


for row in chess_board:
    for piece in row:
        if isinstance(piece, Piece):
            print(piece, end=' ')
        else:
            print(piece, end=' ')
    print()