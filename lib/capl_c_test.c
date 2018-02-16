#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include "capl_c.h"

#define D stateDump(s); printf("---\n");

int main() {
    display(
        "ABC DEFG HIJKL MNOPQR STUVWX YZ0123 456 789 "
        "ABC DEFG HIJKL MNOPQR STUVWX YZ0123 456 789 "
        "ABC DEFG HIJKL MNOPQR STUVWX YZ0123 456 789 "
        "ABC DEFG HIJKL MNOPQR STUVWX YZ0123 456 789\n"
        "ABC DEFG HIJKL MNOPQR STUVWX YZ0123 456 789 "
        "ABC DEFG HIJKL MNOPQR STUVWX YZ0123 456 789 "
        "ABC DEFG HIJKL MNOPQR STUVWX YZ0123 456 789 "
        "ABC DEFG HIJKL MNOPQR STUVWX YZ0123 456 789\n"
        "ABC DEFG HIJKL MNOPQR STUVWX YZ0123 456 789 "
        "ABC DEFG HIJKL MNOPQR STUVWX YZ0123 456 789 "
        "ABC DEFG HIJKL MNOPQR STUVWX YZ0123 456 789 "
        "ABC DEFG HIJKL MNOPQR STUVWX YZ0123 456 789 "
        "ABC DEFG HIJKL MNOPQR STUVWX YZ0123 456 789 "
        "ABC DEFG HIJKL MNOPQR STUVWX YZ0123 456 789\n"
        "ABC DEFG HIJKL MNOPQR STUVWX YZ0123 456 789 "
        "ABC DEFG HIJKL MNOPQR STUVWX YZ0123 456 789 "
        " tail"
        );
    /*
    State *s = stateCreate();
    printf("begin\n");
    stateSet(s, 0, "Foo", 1);
    D;
    stateSet(s, 0, "bar", 2);
    D;
    stateDel(s, 0, "foo");
    D;
    printf("end\n");
    */
    return 0;
}
