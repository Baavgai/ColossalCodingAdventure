#ifndef CAPL_C_H
#define CAPL_C_H

struct State_s;
typedef struct State_s State;

State *stateCreate();
void stateDestroy(State *);
void stateDump(State *); // for testing
void stateSet(State *, int zone, const char *key, int value);
int stateGet(State *, int zone, const char *key);
bool stateHas(State *, int zone, const char *key);
void stateDel(State *, int zone, const char *key);

#define COMMAND_MAX_BUFF 500
typedef struct {
    char cmd[COMMAND_MAX_BUFF], verb[COMMAND_MAX_BUFF], noun[COMMAND_MAX_BUFF];
} ParsedCommand;

void userInput(ParsedCommand *);
#endif
