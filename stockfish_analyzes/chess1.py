import chess
import chess.engine

engine_path = "stockfish"

def analyze_fen(fen, depth=5):
    engine = chess.engine.SimpleEngine.popen_uci(engine_path)  
    board = chess.Board(fen)  #Загрузка FEN позиции
    
    result = engine.analyse(board, chess.engine.Limit(depth=depth))  #Анализ
    engine.quit()  
    return result

fen = "r1b1kbnr/ppp2pp1/3p3p/4p3/3nP1P1/2NP1P1N/PPPKB2q/R1BQ4 w - - 0 11"
analysis = analyze_fen(fen)

#Валидация доски
board = chess.Board(fen)
print("Доска валидна:", board.is_valid())

print("Лучший ход:", analysis["pv"][0])
print("Оценка:", analysis["score"])
print("Все варианты:", analysis["pv"])