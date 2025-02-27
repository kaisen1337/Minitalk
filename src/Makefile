# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: nkasimi <nkasimi@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/07 16:32:32 by nkasimi           #+#    #+#              #
#    Updated: 2025/02/19 21:05:50 by nkasimi          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME         = server
NAME1        = client
NAME_BONUS   = server_bonus
NAME1_BONUS  = client_bonus

CC           = cc -g
FLAGS        = -Wall -Wextra -Werror

SSRC         = server.c
CSRC         = client.c
CMN          = ft_printf.c check_pid.c

SOBJ         = $(SSRC:.c=.o) $(CMN:.c=.o)
COBJ         = $(CSRC:.c=.o) $(CMN:.c=.o)

all: $(NAME) $(NAME1)

$(NAME): $(SOBJ)
	$(CC) $(FLAGS) $(SOBJ) -o $(NAME)

$(NAME1): $(COBJ)
	$(CC) $(FLAGS) $(COBJ) -o $(NAME1)

%.o: %.c
	$(CC) $(FLAGS) -c $< -o $@

SSRCB        = bonus/server_bonus.c
CSRCB        = bonus/client_bonus.c

SBOBJ        = $(SSRCB:.c=.o) $(CMN:.c=.o)
CBOBJ        = $(CSRCB:.c=.o) $(CMN:.c=.o)

bonus: $(NAME_BONUS) $(NAME1_BONUS)

$(NAME_BONUS): $(SBOBJ)
	$(CC) $(FLAGS) $(SBOBJ) -o $(NAME_BONUS)

$(NAME1_BONUS): $(CBOBJ)
	$(CC) $(FLAGS) $(CBOBJ) -o $(NAME1_BONUS)

bonus/%.o: bonus/%.c
	$(CC) $(FLAGS) -c $< -o $@

clean:
	rm -f $(SOBJ) $(COBJ) $(SBOBJ) $(CBOBJ)

fclean: clean
	rm -f $(NAME) $(NAME1) $(NAME_BONUS) $(NAME1_BONUS)

re: fclean all

.PHONY: all bonus clean fclean re
