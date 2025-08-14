# SOKOLIKI Ход дрона 2025

Использование Анализатора партии Stockfish:
1. Перед запуском установить на локальное устройство Stockfish Engine
(https://stockfishchess.org/download/), для MacOS ввести в терминал команду "brew install stockfish".
2. После установки проверить работоспособность Stockfish. Для этого в консоль нужно ввести комманду stockfish. В виде ответа должно появиться приглашение:
Stockfish 16.1 by the Stockfish developers
uci
3. Далее нужно прописать путь для Stockfish в $PATH. Для этого нужно прописать команду в консоль (MacOS): 
echo 'export PATH="$PATH:~/bin/stockfish"' >> ~/.bashrc
source ~/.bashrc
4. Далее, остается установить библиотеку python-chess. Для этого нужно прописать в терминал pip3 install python-chess. 

После этого анализатор готов к работе. Для того, чтобы просчитать ходы и инициализировать положение на доске используется FEN-код. (Он имеет примерно такой вид: "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR  w  KQkq  -  0  1"). Замените содержимое переменной fen для изменения FEN-кода. 