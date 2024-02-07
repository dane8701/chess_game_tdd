class Piece:
    def __init__(self, color, piece_type, movement_range, capture_range):
        self.color = color  
        self.piece_type = piece_type  
        self.has_moved = False  
        self.movement_range = movement_range  
        self.capture_range = capture_range  
        self.symbol = self.get_symbol()  

    def get_symbol(self):
        
        if self.color == 'white':
            color_symbol = '\u2654'  
        else:
            color_symbol = '\u265A'  

        if self.piece_type == 'pawn':
            return '\u265F' if self.color == 'white' else '\u2659'  
        elif self.piece_type == 'rook':
            return '\u265C' if self.color == 'white' else '\u2656'  
        elif self.piece_type == 'knight':
            return '\u265E' if self.color == 'white' else '\u2658'  
        elif self.piece_type == 'bishop':
            return '\u265D' if self.color == 'white' else '\u2657'  
        elif self.piece_type == 'queen':
            return '\u265B' if self.color == 'white' else '\u2655'  
        elif self.piece_type == 'king':
            return color_symbol

    def __str__(self):
        return self.symbol

    def get_possible_moves(self, current_position):
        possible_moves = []
        for move in self.movement_range:
            new_position = (current_position[0] + move[0], current_position[1] + move[1])
            
            if 0 <= new_position[0] <= 7 and 0 <= new_position[1] <= 7:
                possible_moves.append(new_position)
        
        return possible_moves
    
    def move_piece(board, start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        if not (0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8):
            print("Positions invalides.")
            return False
        piece = board[start_row][start_col]

        if piece == ' ':
            print("Aucune pièce à cette position.")
            return False
        possible_moves = piece.get_possible_moves((start_row, start_col))
        capture_moves = piece.capture_range

        if piece.piece_type == 'pawn':
            if (end_row, end_col) in possible_moves:
                if board[end_row][end_col] != ' ':
                    print("1")
                    print("Déplacement invalide pour cette pièce.")
                    return False
            elif (end_row, end_col) in capture_moves:
                if board[end_row][end_col] == ' ':
                    print("2")
                    print("Déplacement invalide pour cette pièce.")
                    return False
            else:
                if (end_row == 0 and piece.color == 'white') or (end_row == 7 and piece.color == 'black'):
                    print("Promotion du pion !")
                board[end_row][end_col] = piece
                board[start_row][start_col] = ' '
                print("La pièce a été déplacée avec succès.")
                return True
            
            if (end_row == 0 and piece.color == 'white') or (end_row == 7 and piece.color == 'black'):
                print("Promotion du pion !")
                
        board[end_row][end_col] = piece
        board[start_row][start_col] = ' '

        print("La pièce a été déplacée avec succès.")
        return True