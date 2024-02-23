#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
/**
 *infinite_while - provides some delay
 *Return: int
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 *main - main entry for program
 *Return: int 0 on success
 */
int main(void)
{
	pid_t child_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid > 0)
		{
			/*parent*/
			sleep(1);
		}
		else
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}
	infinite_while();
	return (0);
}
