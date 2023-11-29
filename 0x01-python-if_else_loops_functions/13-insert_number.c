#include "lists.h"

/**
 * insert_node - this function inserts a number,
 * into a sorted singly-linked list
 * @head: a pointer the head of the linked list
 * @number: the number to put in
 * Return: NULL if the function fails
 * Otherwise - a pointer to the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->k = number;

	if (node == NULL || node->k >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->k < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
