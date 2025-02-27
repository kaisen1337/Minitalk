Detailed Documentation on sigaction
and Signal Handling – Every Little Detail

------------------------------------------------
Introduction to   aa Signals:
Signals are messages from the OS.
They notify processes about events.
Examples: SIGINT, SIGTERM, SIGSEGV.
Signals let processes communicate and react.
They can stop, pause, or change process flow.
Understanding signals is key in Unix systems.

------------------------------------------------
Types of Signals:
There are two main groups:
1. Standard Signals (fixed behavior)
   - Examples: SIGINT, SIGTERM, SIGSEGV.
2. Real-Time Signals (can queue and carry data)
   - Named from SIGRTMIN to SIGRTMAX.
Standard signals have default actions.
Real-time signals can be queued.
Each signal has a unique number.

------------------------------------------------
Signal Actions:
When a signal is received, a process can:
- Use the default action.
- Ignore the signal.
- Catch it with a custom handler.
Default action may terminate the process.
Ignoring means no reaction.
Catching means executing a function.

------------------------------------------------
What is sigaction?
sigaction is a system call.
It sets how to handle a signal.
It is more powerful than signal().
It offers extra control and information.
It does not reset your handler automatically.
It gives you robust, reliable handling.

------------------------------------------------
Syntax of sigaction:
int sigaction(int signum,
              const struct sigaction *act,
              struct sigaction *oldact);
Parameters:
- signum: The signal number (e.g., SIGINT).
- act: Pointer to new settings.
- oldact: Pointer to save old settings.
Returns 0 on success, -1 on error.
It configures how your process reacts to signals.

------------------------------------------------
The struct sigaction:
This structure defines signal behavior.
It contains several fields:

Field: sa_handler
- A pointer to a simple handler.
- It takes one int (the signal number).
- Use for basic signal handling.

Field: sa_sigaction
- A pointer to an advanced handler.
- Takes three parameters: signal number, siginfo_t pointer, context.
- Use when extra details are needed.
- Requires the flag SA_SIGINFO.

Field: sa_mask
- A signal set of type sigset_t.
- Blocks signals during the handler.
- Prevents interference from other signals.
- Set using helper functions (e.g., sigemptyset).

Field: sa_flags
- Flags to modify handler behavior.
- Common flags:
  • SA_SIGINFO: Use sa_sigaction.
  • SA_RESTART: Restart interrupted system calls.
  • SA_NODEFER: Do not block the current signal.
- Configure these to fine-tune behavior.  Field: sa_restorer
- An obsolete field.
- Do not use in modern code.

------------------------------------------------
The sigset_t Type:
sigset_t represents a set of signals.
It is used to block or allow signals.
It holds multiple signals in a bitmask.
It is controlled by specific functions.
Understanding sigset_t is crucial.

------------------------------------------------
Manipulating Signal Sets:
Use these functions to work with sigset_t:

sigemptyset(&set):
- Initializes set to empty.
- Removes all signals.
- Always call this first.

sigfillset(&set):
- Fills set with all signals.
- Useful for blocking everything temporarily.

sigaddset(&set, signum):
- Adds a specific signal.
- Example: sigaddset(&set, SIGINT);
- Blocks SIGINT during execution.

sigdelset(&set, signum):
- Removes a signal from the set.
- Example: sigdelset(&set, SIGINT);

sigismember(&set, signum):
- Checks if signal is in set.
- Returns 1 if present, 0 if not.

------------------------------------------------
The siginfo_t Structure:
siginfo_t provides extra signal details.
It is used with SA_SIGINFO.
It helps in debugging and advanced handling.
Its fields include:

si_signo:
- The received signal number.
- Identifies the signal.

si_errno:
- Holds an error number.
- Shows error details if present.

si_code:
- Gives a code for the signal cause.
- Explains why the signal was sent.

si_pid:
- The sender's process ID.
- Tells who sent the signal.

si_uid:
- The sender's user ID.
- Helps verify the sender.

si_addr:
- The faulting memory address.
- Used for SIGSEGV, SIGBUS, etc.

si_status:
- Exit status for SIGCHLD signals.
- Indicates termination details.

si_value:
- A union holding extra data.
- Used for real-time signals.

------------------------------------------------
How Does sigaction Work?
Steps to use sigaction:
1. Declare a struct sigaction variable.
2. Choose your handler function.
   - Use sa_handler for simple handlers.
   - Use sa_sigaction for extra details.
3. Initialize a signal set (sigset_t).
   - Call sigemptyset to clear the set.
   - Use sigaddset to add signals to block.
4. Set the desired flags in sa_flags.
   - Use SA_SIGINFO if using sa_sigaction.
5. Call sigaction with the signal number.
   - Pass your struct for new action.
   - Optionally save the old action.
6. Your process now handles signals as set.

------------------------------------------------
Example Code Walkthrough:
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// Advanced signal handler
void my_handler(int signum, siginfo_t *info, void *context) {
    (void)context;  // Unused parameter
    printf("Signal %d received.\n", signum);
    printf("Sender PID: %d\n", info->si_pid);
}

int main(void) {
    struct sigaction sa;
    sigset_t mask;
    
    // Initialize mask to empty
    sigemptyset(&mask);
    // Add SIGINT to the mask
    sigaddset(&mask, SIGINT);
    
    // Set the advanced handler function
    sa.sa_sigaction = my_handler;
    // Use the mask to block SIGINT during handler execution
    sa.sa_mask = mask;
    // Use SA_SIGINFO flag to get extra info
    sa.sa_flags = SA_SIGINFO;
    
    // Set action for SIGUSR1 signal
    if (sigaction(SIGUSR1, &sa, NULL) == -1) {
        perror("Error in sigaction");
        exit(EXIT_FAILURE);
    }
    
    printf("Process PID: %d\n", getpid());
    // Wait for signals indefinitely
    while (1) {
        pause();
    }
    return 0;
}

------------------------------------------------
Detailed Explanation of Example:
- my_handler is set as the advanced handler.
- It prints the signal number and sender PID.
- sigemptyset clears the mask.
- sigaddset adds SIGINT to block it.
- SA_SIGINFO flag tells sigaction to use my_handler with extra info.
- sigaction sets the action for SIGUSR1.
- The program prints its PID.
- pause() waits until a signal is received.
- When SIGUSR1 arrives, my_handler is called.

------------------------------------------------
More Details on Flags and Behavior:
SA_SIGINFO:
- Enables using sa_sigaction.
- Provides extra details via siginfo_t.
- Use this for advanced error handling.

SA_RESTART:
- Automatically restarts some system calls.
- Prevents system calls from failing due to signals.
- Use it if your program relies on system calls.

SA_NODEFER:
- Does not block the signal that triggered the handler.
- Allows the same signal to be received again.
- Useful in some reentrant situations.

------------------------------------------------
Common Pitfalls and Tips:
- Always initialize your sigset_t with sigemptyset.
- Use sigaddset to block signals that interfere.
- Check sigaction’s return value for errors.
- Avoid using obsolete fields like sa_restorer.
- Global variables in signal handlers can cause bugs.
- Test your code with simple examples first.
- Read system manuals for extra details.

------------------------------------------------
Summary:
- Signals are OS messages for events.
- sigaction sets custom actions for signals.
- struct sigaction defines the handler and mask.
- sa_handler and sa_sigaction set your function.
- sa_mask (sigset_t) blocks signals during execution.
- Use sigemptyset, sigaddset, and others to manage sets.
- siginfo_t gives extra details about signals.
- Flags like SA_SIGINFO and SA_RESTART modify behavior.
- Practice with examples to learn each detail.
- Mastering signal handling is vital for system code.

------------------------------------------------
Final Tips for Beginners:
Read each section slowly.
Write small programs to test ideas.
Use comments in your code.
Ask for help when confused.
Review and experiment often.
Practice builds deep understanding.
Happy coding and keep learning!
