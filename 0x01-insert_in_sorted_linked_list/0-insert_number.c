#include "lists.h"

/**
 * insert_node - Inserts a a new node in a sorted linked list
 * @head: head of the linked list
 * @number: value of the number of the node that will be inserted
 * Return: address of the new node or Null on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
  /* allocates the memory for the new node */
  listint_t *new_node = malloc(sizeof(listint_t));
  /* stores the head of the linked list */
  listint_t *current_node = *head;

  if (new_node)
  {
    new_node->n = number;
    new_node->next = NULL;
    if (*head == NULL || (*head)->n >= new_node->n)
    {
      new_node->next = *head;
      *head = new_node;
    }
    else
    {
      while (current_node->next && current_node->next->n < new_node->n)
        {
          current_node = current_node->next;
        }
        new_node->next = current_node->next;
        current_node->next = new_node;
    }
    return (new_node);
  }
  return (NULL);
}
