#ifndef CCA_H
#define CCA_H

#include <stdbool.h>
#include <stdarg.h>
#define COMMAND_MAX 100
typedef struct {
    char full[COMMAND_MAX];
    char *verb, *noun;
    char buffer[COMMAND_MAX];
} Command;

char *sanitizeCommandEntered(char *);
bool parseCommand(Command *, const char *);
void loadUserCommand(Command *);
void displayWrap(const int width, const char *s);
// void display(int width, const char *fmt, ...);

#define MK_DISPLAY_WIDTH_BUFFSIZE(WIDTH,MAX_BUFF) void display(const char *fmt, ...) { \
    char buffer[MAX_BUFF]; \
    va_list args; \
    va_start (args, fmt); \
    vsnprintf (buffer, MAX_BUFF-1, fmt, args); \
    va_end (args); \
    displayWrap(WIDTH, buffer); \
}

#define MK_DISPLAY_WIDTH(WIDTH) MK_DISPLAY_WIDTH_BUFFSIZE(WIDTH,2000)
#define MK_DISPLAY MK_DISPLAY_WIDTH(75)

#endif
