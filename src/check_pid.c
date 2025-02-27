/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   check_pid.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nkasimi <nkasimi@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/02/18 16:08:50 by nkasimi           #+#    #+#             */
/*   Updated: 2025/02/18 16:10:06 by nkasimi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "minitalk.h"

pid_t	ch_pid(char *str)
{
	int		i;
	pid_t	pid;

	i = 0;
	while (str[i])
	{
		if (!(str[i] >= '0' && str[i] <= '9'))
			exit((ft_printf("Pid not valid\n"), 1));
		i++;
	}
	pid = atoi(str);
	if (pid == 0)
		exit((ft_printf("Pid not valid\n"), 1));
	return (pid);
}
