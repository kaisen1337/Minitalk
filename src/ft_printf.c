/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nkasimi <nkasimi@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/12/30 20:50:29 by nkasimi           #+#    #+#             */
/*   Updated: 2025/02/13 17:42:12 by nkasimi          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "minitalk.h"

void	ft_putchar(char c, int *counter)
{
	write(1, &c, 1);
	(*counter)++;
}

void	ft_putstr(char *str, int *counter)
{
	if (!str)
		str = "(null)";
	while (*str)
	{
		ft_putchar(*str, counter);
		str++;
	}
}

void	ft_putnbr(int nb, int *counter)
{
	long	n;

	n = nb;
	if (n < 0)
	{
		ft_putchar('-', counter);
		n = -n;
	}
	if (n >= 10)
	{
		ft_putnbr(n / 10, counter);
	}
	ft_putchar(n % 10 + '0', counter);
}

void	format_specifier(va_list arguements, char specifier, int *counter)
{
	if (specifier == 'd' || specifier == 'i')
		ft_putnbr(va_arg(arguements, int), counter);
	else if (specifier == 's')
		ft_putstr((char *)va_arg(arguements, char *), counter);
}

int	ft_printf(const char *str, ...)
{
	va_list	arguements;
	int		counter;
	int		i;

	i = 0;
	counter = 0;
	va_start(arguements, str);
	while (str[i])
	{
		if (str[i] == '%')
		{
			i++;
			format_specifier(arguements, str[i], &counter);
		}
		else
			ft_putchar(str[i], &counter);
		i++;
	}
	va_end(arguements);
	return (counter);
}
