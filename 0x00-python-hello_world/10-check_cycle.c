#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return:  0-If there is no cycle 
 *          1-if there's a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *head, *tail;

	if (list == NULL)
		return (0);

	head = list;
	tail = list;

	while (tail != NULL&& tail->next != NULL)
	{
		head = head->next;
    tail = tail->next->next;
    
    if (head == tail)
      return (1);
	}

	return (0);
}
