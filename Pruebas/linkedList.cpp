#include <iostream>

struct Node
{
    int value;
    Node *next;
};
void printList(Node *head)
{
    Node *currentNode = head;
    while (currentNode != nullptr)
    {
        std::cout << currentNode->value;

        if (currentNode->next != nullptr)
        {
            std::cout << " -> ";
        }

        currentNode = currentNode->next;
    }
    std::cout << std::endl;
}

int main()
{
    Node *head = new Node();
    head->value = 1;

    Node *second = new Node();
    second->value = 2;

    Node *third = new Node();
    third->value = 3;

    Node *fourth = new Node();
    fourth->value = 4;

    head->next = second;
    second->next = third;
    third->next = fourth;
    
    

    printList(head);

    return 0;
}
