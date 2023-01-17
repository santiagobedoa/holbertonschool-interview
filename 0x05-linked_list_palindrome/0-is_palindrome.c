#include "lists.h"

/**
 * is_palindrome - checks if a linked list is palindrome
 * @head: head of the linked list
 * Return: 1 if the linked list is palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head) {
  listint_t *hare = *head;
  listint_t *tortoise = *head;
  listint_t *first_half = *head;
  listint_t *second_half;

  if (*head == NULL)
    return (1);

  while (1) {
    hare = hare->next->next;
    if (hare == NULL) {
      second_half = tortoise->next;
      break;
    }
    if (hare->next == NULL) {
      second_half = tortoise->next->next;
      break;
    }

    tortoise = tortoise->next;
  }

  reverse_linked_list(&second_half);

  while (first_half && second_half) {
    if (first_half->n != second_half->n) {
      return (0);
    }
    first_half = first_half->next;
    second_half = second_half->next;
  }
  return (1);
}

/**
 * reverse_linked_list - function that reverse a linked list
 * @head: double pointer to the head of the linked list 
 * Return: pointer to the head of the reversed linked list
 */
void reverse_linked_list(listint_t **head) {
  listint_t *current = *head;
  listint_t *prev = NULL;
  listint_t *next = NULL;

  printf("reverse_linked_list");
  while (current != NULL) {
    next = current->next;
    current->next = prev;
    prev = current;
    current = next;
  }

  *head = prev;
}
