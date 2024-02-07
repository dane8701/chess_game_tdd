import unittest
from piece import Piece

class TestPiece(unittest.TestCase):
    def setUp(self):
        self.white_pawn = Piece('white', 'pawn', [(1, 0)], [(-1, -1), (-1, 1)])
        self.black_pawn = Piece('black', 'pawn', [(-1, 0)], [(1, -1), (1, 1)])
        self.black_knight = Piece('black', 'knight', [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)], [])
        # Initialisatoin des pièces pour chaque test
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

        self.chess_board = [[' ' for _ in range(8)] for _ in range(8)]

        white_pieces = []
        for piece_type in movement_range:
            white_pieces.extend([Piece('white', piece_type, movement_range[piece_type], capture_range[piece_type]) for _ in range(2 if piece_type != 'pawn' else 8)])


        black_pieces = []
        for piece_type in movement_range:
            black_pieces.extend([Piece('black', piece_type, movement_range[piece_type], capture_range[piece_type]) for _ in range(2 if piece_type != 'pawn' else 8)])


        for i in range(8):
            self.chess_board[1][i] = white_pieces[i]  
        self.chess_board[0][0] = white_pieces[8]  
        self.chess_board[0][7] = white_pieces[9]  
        self.chess_board[0][1] = white_pieces[10]  
        self.chess_board[0][6] = white_pieces[11]  
        self.chess_board[0][2] = white_pieces[12]  
        self.chess_board[0][5] = white_pieces[13]  
        self.chess_board[0][3] = white_pieces[14]  
        self.chess_board[0][4] = white_pieces[15]  


        for i in range(8):
            self.chess_board[6][i] = black_pieces[i]  
        self.chess_board[7][0] = black_pieces[8]  
        self.chess_board[7][7] = black_pieces[9]  
        self.chess_board[7][1] = black_pieces[10]  
        self.chess_board[7][6] = black_pieces[11]  
        self.chess_board[7][2] = black_pieces[12]  
        self.chess_board[7][5] = black_pieces[13]  
        self.chess_board[7][3] = black_pieces[14]  
        self.chess_board[7][4] = black_pieces[15]

    def test_get_possible_moves_pawn(self):
        self.assertEqual(self.chess_board[1][0].get_possible_moves((1, 0)), [(2, 0)])
        
    def test_create_piece_king_white(self):
        piece = Piece('white', 'king', [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)], [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)])
        self.assertTrue(isinstance(piece, Piece))
        
    def test_move_piece_valid(self):
        # Teste un déplacement valide
        self.assertTrue(Piece.move_piece(self.chess_board, (1, 0), (2, 0)))

    def test_move_piece_position_invalid(self):
        # Teste un déplacement invalide
        self.assertFalse(Piece.move_piece(self.chess_board, (1, 0), (2, -1)))
    
    def test_move_piece_invalid(self):
        # Teste un déplacement invalide
        self.assertFalse(Piece.move_piece(self.chess_board, (5, 0), (6, 0)))

    def test_move_piece_capture(self):
        # Place un pion noir sur le plateau pour tester la capture
        self.board[3][1] = self.black_pawn
        # Teste une capture valide par un pion blanc
        self.assertTrue(self.white_pawn.move_piece(self.board, (2, 0), (3, 1)))
        # Vérifie que le pion noir a été capturé
        self.assertIs(self.board[3][1], self.white_pawn)
        
    def test_move_piece_interchange(self):
        # Place un pion blanc et un pion noir sur le plateau pour tester l'interchange
        self.board[3][1] = self.black_pawn
        self.board[4][2] = self.white_pawn
        # Teste un déplacement valide d'un pion blanc
        self.assertTrue(self.white_pawn.move_piece(self.board, (4, 2), (3, 2)))
        # Teste un déplacement valide d'un pion noir
        self.assertTrue(self.black_pawn.move_piece(self.board, (3, 1), (4, 1)))
        self.assertIs(self.board[3][2], self.white_pawn)
        self.assertIs(self.board[4][1], self.black_pawn)

    def test_move_piece_invalid_capture(self):
        # Place un pion blanc et un cavalier noir sur le plateau pour tester une capture invalide
        self.board[3][1] = self.black_knight
        self.board[4][2] = self.white_pawn
        # Teste un déplacement invalide d'un pion blanc (tentative de capture)
        self.assertFalse(self.white_pawn.move_piece(self.board, (4, 2), (3, 1)))
        self.assertIs(self.board[4][2], self.white_pawn)
        self.assertIs(self.board[3][1], self.black_knight)

if __name__ == '__main__':
    unittest.main()
