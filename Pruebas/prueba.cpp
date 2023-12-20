#include <iostream>

struct Nodo
{
    int valor;
    Nodo *punteroSiguiente;
};

void imprimirLista(Nodo *cabeza)
{
    Nodo *nodoActual = cabeza;
    while (nodoActual != nullptr)
    {
        std::cout << nodoActual->valor;
        if (nodoActual->punteroSiguiente != nullptr)
        {
            std::cout << " -> ";
        }
        nodoActual = nodoActual->punteroSiguiente;
    }
    std::cout << std::endl;
}

int main()
{
    Nodo *cabeza = new Nodo();
    cabeza->valor = 1;

    Nodo *segundo = new Nodo();
    segundo->valor = 2;

    Nodo *tercero = new Nodo();
    tercero->valor = 3;

    Nodo *cuarto = new Nodo();
    cuarto->valor = 4;

    cabeza->punteroSiguiente = segundo;
    segundo->punteroSiguiente = tercero;
    tercero->punteroSiguiente = cuarto;

    imprimirLista(cabeza);
}
