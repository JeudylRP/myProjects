#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int BOARD_SIZE = 8;
char board[BOARD_SIZE][BOARD_SIZE];

// Inicializa el tablero con las piezas en sus posiciones iniciales
void initializeBoard()
{
    // Colocar peones
    for (int i = 0; i < BOARD_SIZE; i++)
    {
        board[1][i] = 'P'; // Peones blancos
        board[6][i] = 'p'; // Peones negros
    }

    // Colocar torres
    board[0][0] = board[0][7] = 'T';
    board[7][0] = board[7][7] = 't';

    // Colocar caballos
    board[0][1] = board[0][6] = 'C';
    board[7][1] = board[7][6] = 'c';

    // Colocar alfiles
    board[0][2] = board[0][5] = 'A';
    board[7][2] = board[7][5] = 'a';

    // Colocar reinas y reyes
    board[0][3] = 'Q';
    board[0][4] = 'K';
    board[7][3] = 'q';
    board[7][4] = 'k';

    // Espacios vacíos
    for (int i = 2; i < 6; i++)
    {
        for (int j = 0; j < BOARD_SIZE; j++)
        {
            board[i][j] = '.';
        }
    }
}

// Imprime el tablero
void printBoard()
{
    for (int i = 0; i < BOARD_SIZE; i++)
    {
        for (int j = 0; j < BOARD_SIZE; j++)
        {
            cout << board[i][j] << " ";
        }
        cout << endl;
    }
}

// Verifica si el movimiento es válido (implementación muy básica)
bool isValidMove(int x1, int y1, int x2, int y2)
{
    // Ejemplo simple: solo permite moverse a un espacio vacío
    return board[x2][y2] == '.';
}

// Mueve una pieza
void movePiece(int x1, int y1, int x2, int y2)
{
    if (isValidMove(x1, y1, x2, y2))
    {
        board[x2][y2] = board[x1][y1];
        board[x1][y1] = '.';
    }
    else
    {
        cout << "Movimiento no válido." << endl;
    }
}

int main()
{
    initializeBoard();
    printBoard();

    int x1, y1, x2, y2;
    while (true)
    {
        cout << "Introduce las coordenadas de la pieza a mover (fila columna): ";
        cin >> x1 >> y1;
        cout << "Introduce las coordenadas a donde mover la pieza (fila columna): ";
        cin >> x2 >> y2;

        movePiece(x1, y1, x2, y2);
        printBoard();
    }

    return 0;
}
