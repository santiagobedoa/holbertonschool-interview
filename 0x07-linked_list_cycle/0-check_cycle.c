#include <stdio.h>
#include <stdlib.h>
#include "lists.h"


/**
 * check_cycle: check if a linked list has a loop
 * @list: head of the linked list
 *
 * Return: 1 if loop, 0 otherwise
 */
int check_cycle(listint_t *list)
{
  listint_t *slow = list;
  listint_t *fast = list;

  while (slow && fast && fast->next)
  {
    slow = slow->next;
    fast = fast->next->next;

    if (slow == fast)
    {
      return 1;
    }
  }
  return 0;
}
