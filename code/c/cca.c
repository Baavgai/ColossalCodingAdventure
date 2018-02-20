#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
#include "cca.h"


char *sanitizeCommandEntered(char *cmd) {
    bool lastSpace = true;
    char *s = cmd;
    char *d = cmd;
    // for(; *s!=' '; s++);
    for(; *s!='\0'; s++) {
        if (*s==' ') {
            if (!lastSpace) {
                *d++ = ' ';
                lastSpace = true;
            }
        } else if (isalpha(*s)) {
            *d++ = tolower(*s);
            lastSpace = false;
        }
    }
    if (d>cmd && *(d - 1)==' ') { --d; }
    *d= '\0';
    return cmd;
}

bool parseCommand(Command *cmd, const char *s) {
    if (sanitizeCommandEntered(strcpy(cmd->full, s))[0]==0) { 
        cmd->buffer[0] = 0;
        cmd->noun = cmd->verb = cmd->buffer;
        return false;
    } else {
        cmd->noun = cmd->verb = strcpy(cmd->buffer, cmd->full);
        for(; *(cmd->noun)!='\0'; cmd->noun++) {
            if (*(cmd->noun)==' ') {
                *(cmd->noun)='\0';
                cmd->noun++;
                break;
            }
        }
        return true;
    }
}

void loadUserCommand(Command *cmd) {
    char buffer[COMMAND_MAX];
    bool done = false;
    while(!done) {
        printf("> ");
        if(fgets(buffer, COMMAND_MAX - 1, stdin)) {
            done = parseCommand(cmd, buffer);
        }
    }
}


void displayWrap(const int width, const char *s) {
    int scanned, last;
    for(scanned = last = 0; s[scanned] != '\0'; scanned++) {
        if (scanned==width) {
            if (last==0) {
                for(;scanned!=0; s++, scanned--) { putchar(*s); }
            } else {
                for(;last!=0; s++, last--) { putchar(*s); }
                scanned = 0;
            }
            putchar('\n');
            for(;*s==' '; s++);
        }
        if (s[scanned]==' ') {
            last = scanned;
        } else if (s[scanned]=='\n') {
            for(;scanned!=0; s++, scanned--) { putchar(*s); };
            last = 0;
        }
    }
    if (*s!='\0') { printf("%s\n", s); } else { putchar('\n'); }
}


/*
void display(int width, const char *fmt, ...) {
    char buffer[2000];
    va_list args;
    va_start (args, fmt);
    vsnprintf (buffer, sizeof(buffer)-1, fmt, args);
    va_end (args);
    displayWrap(width, buffer);
}


void display(const char *fmt, ...) {
  char buffer[2000];
  va_list args;
  va_start (args, fmt);
  vsnprintf (buffer, sizeof(buffer)-1, fmt, args);
  va_end (args);
  displayWrap(buffer, 70);
}
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <stdarg.h>
#include <ctype.h>

void tprintf( int row, int col, char *fmt, ... )
 {
    va_list ap;
    char *p1, *p2;

    va_start( ap, fmt );
    p1 = va_arg( ap, char * );
    p2 = va_arg( ap, char * );
    printf( "%c[%2.2d;%2.2dH", ESCAPE, row, col );
    printf( fmt, p1, p2 );
    va_end( ap );
 }
*/
