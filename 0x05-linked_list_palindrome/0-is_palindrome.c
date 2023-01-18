#include "lists.h"

/**
 * reverse_linked_list - function that reverse a linked list
 * @head: head of the linked list
 * Return: void
 */
void reverse_linked_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
        	current->next = prev;
        	prev = current;
        	current = next;
    	}

    	*head = prev;
}

/**
 * is_palindrome - checks if a linked list is palindrome
 * @head: head of the linked list
 * Return: 1 if the linked list is palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *copy_1 = *head;
	listint_t *copy_2 = *head;
	listint_t *copy_3 = *head;
	int num_of_nodes = 0;
	int half = 0;

	if (*head == NULL)
	{
		return (1);
	}
	while (copy_1)
	{
		num_of_nodes += 1;
		copy_1 = copy_1->next;
	}
	while (half != (num_of_nodes / 2))
	{
		half += 1;
		copy_2 = copy_2->next;
	}
	reverse_linked_list(&copy_2);
	while (copy_3 && copy_2)
	{
		if (copy_3->n != copy_2->n)
		{
			return (0);
		}
		copy_3 = copy_3->next;
		copy_2 = copy_2->next;
	}
	return (1);
}
