#ifndef LISTS_H
#define LISTS_H

#inlcude <stdlib.h>
/**
 * struct listint_s-singly linked list
 * @n:integer
 * @next:pointer to the next node
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
}listint_t;

#endif
