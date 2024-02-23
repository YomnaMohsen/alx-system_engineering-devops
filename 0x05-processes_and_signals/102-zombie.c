#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}
int main() 
{
    pid_t child_pid; // Fork returns process ID
    int i;

    for (i = 0; i < 5; i++)
    {
        child_pid = fork();
        if (child_pid > 0) 
        {
        // Parent process

         sleep(1);

        }
        else 
        {
        // Child process
        
        exit(0);    // Child exits
        
        }
    }
    infinite_while();
    return (0);
}
