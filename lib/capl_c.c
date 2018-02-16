#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
#include "capl_c.h"

typedef struct StateNode_s {
  int zone;
  char *key;
  int value;
  struct StateNode_s *next;

} StateNode;

struct State_s {
  StateNode *top;
};


char *lowerAll(char *s) {
  char *p = s;
  for(; *p!='\0'; p++) { *p = tolower(*p); }
  return s;
}

bool simatch(const char *x, const char *y) {
  for(; *x!='\0' && *y!='\0' && tolower(*x)==tolower(*y); x++, y++);
  return *x=='\0' && *y=='\0';
}

State *stateCreate() {
  State *s = malloc(sizeof(State));
  s->top = NULL;
  return s;
}

StateNode *stateNodeCreate(int zone, const char *key, int value, StateNode *next) {
  StateNode *n = malloc(sizeof(StateNode));
  n->zone = zone;
  n->key = lowerAll(strcpy(malloc(strlen(key) + 1), key));
  n->value = value;
  n->next = next;
  return n;
}

StateNode *stateFind(State *s, int zone, const char *key, StateNode **prior) {
  StateNode *x = s->top;
  if (prior) { *prior = NULL; }
  if (s->top && x->zone==zone && simatch(key, x->key)) {
    return x;
  } else if (s->top) {
    StateNode *p = s->top;
    for(; p->next; p = p->next) {
      x = p->next;
      if (x->zone==zone && simatch(key, x->key)) {
        if (prior) { *prior = p; }
        return x;
      }
    }
  }
  return NULL;
}

void stateDump(State *s) {
  StateNode *p = s->top;
  for(; p; p = p->next) {
    printf("%d %s = %d\n", p->zone, p->key, p->value);
  }
}

void stateDestroy(State *s) {
  while(s->top) {
    StateNode *p = s->top;
    s->top = s->top->next;
    free(p->key);
    free(p);
  }
  free(s);
}

void stateSet(State *s, int zone, const char *key, int value) {
  StateNode *found = stateFind(s, zone, key, NULL);
  if (found) {
    found->value = value;
  } else {
    s->top = stateNodeCreate(zone, key, value, s->top);
  }
}

int stateGet(State *s, int zone, const char *key) {
  StateNode *found = stateFind(s, zone, key, NULL);
  return found ? found->value : -1;
}

bool stateHas(State *s, int zone, const char *key) {
  return stateFind(s, zone, key, NULL) ? true : false;
}

void stateDel(State *s, int zone, const char *key) {
  StateNode *prior;
  StateNode *found = stateFind(s, zone, key, &prior);
  if (found) {
    if (prior==NULL) {
      s->top = s->top->next;
    } else {
      prior->next = found->next;
    }
    free(found->key);
    free(found);
  }
}


#define BUFF_SIZE 500
void userInput(ParsedCommand *cmd) {
    bool done = false;
    while(!done) {
        printf("> ");
        if(fgets(cmd->cmd, sizeof(cmd->cmd)-1, stdin)) {
            switch(sscanf( cmd->cmd, "%s %s", cmd->verb, cmd->noun )) {
                case 1: *(cmd->noun) = 0;
                case 2: done = true;
            }
        }
        strcpy(cmd->cmd, cmd->verb);
        if (*(cmd->noun) != 0) {
          strcat(strcat(cmd->cmd, " "), cmd->noun);
        }
        
    }
}
// DISPLAY_WIDTH
void display(const char *s) {
    int scanned, last;
    for(scanned = last = 0; s[scanned] != '\0'; scanned++) {
        if (scanned==DISPLAY_WIDTH) {
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