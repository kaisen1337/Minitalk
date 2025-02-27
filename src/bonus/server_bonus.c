/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   server_bonus.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nkasimi <nkasimi@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/02/19 21:16:31 by nkasimi           #+#    #+#             */
/*   Updated: 2025/02/19 21:18:12 by nkasimi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../minitalk.h"

void	helper(pid_t *checker, siginfo_t *info, int *bit, char *c)
{
	if (*checker == 0)
		*checker = info->si_pid;
	else if (*checker != info->si_pid)
	{
		*c = 0;
		*bit = 0;
		*checker = info->si_pid;
	}
}

void	signal_handler(int signal, siginfo_t *info, void *context)
{
	static int		bit;
	static char		c;
	static pid_t	checker;

	(void)context;
	helper(&checker, info, &bit, &c);
	if (signal == SIGUSR1)
		c |= (1 << (7 - bit));
	bit++;
	if (bit == 8)
	{
		if (c == '\0')
			kill(checker, SIGUSR1);
		write(1, &c, 1);
		c = 0;
		bit = 0;
	}
	usleep(50);
	kill(checker, SIGUSR2);
}

int	main(void)
{
	struct sigaction	sa;

	ft_printf("Server PID: %d\n", getpid());
	ft_printf("Waiting...\n");
	sa.sa_sigaction = signal_handler;
	sa.sa_flags = SA_SIGINFO;
	sigemptyset(&sa.sa_mask);
	sigaction(SIGUSR1, &sa, NULL);
	sigaction(SIGUSR2, &sa, NULL);
	while (1)
		pause();
	return (0);
}
