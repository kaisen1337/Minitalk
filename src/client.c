/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   client.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nkasimi <nkasimi@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/02/07 18:20:12 by nkasimi           #+#    #+#             */
/*   Updated: 2025/02/19 21:20:54 by nkasimi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "minitalk.h"

void	hand_chack(int sig)
{
	(void)sig;
}

int	send(pid_t num, int c)
{
	int	bit;
	int	result;

	bit = 7;
	while (bit >= 0)
	{
		if (c & (1 << bit))
			result = kill(num, SIGUSR1);
		else
			result = kill(num, SIGUSR2);
		if (result == -1)
			return (-1);
		usleep(100000);
		bit--;
	}
	return (0);
}

int	message_sender(pid_t num, char *str)
{
	int	i;
	int	result;

	i = 0;
	while (str[i])
	{
		result = send(num, str[i]);
		if (result == -1)
			return (-1);
		i++;
	}
	return (0);
}

int	main(int ac, char **av)
{
	struct sigaction	sa_client;
	pid_t				pid;
	int					result;

	if (ac == 3)
	{
		pid = ch_pid(av[1]);
		sa_client.sa_handler = hand_chack;
		sigemptyset(&sa_client.sa_mask);
		sa_client.sa_flags = 0;
		if (sigaction(SIGUSR2, &sa_client, NULL) == -1)
			exit((ft_printf("sigaction error\n"), 1));
		result = message_sender(pid, av[2]);
		if (result == -1)
			ft_printf("message fail\n");
		send(pid, '\0');
	}
	return (0);
}
