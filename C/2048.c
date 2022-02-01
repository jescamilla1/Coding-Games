#include <stdio.h>
#include <ctype.h> /* for tolower() */

int board[4][4] = {0};
int i,j;
void GameBoard(){
    for (i = 0; i<4; i++ ){
        printf("+---+---+---+---+\n");
        for(j = 0; j<4; j++){
            if(board[i][j] == 0){
                printf("|   ");
            }
            else{
                printf("| %c ", board[i][j] );
            }
        }
        printf("|\n");
    }
    printf("+---+---+---+---+\n");
}

char getDirection(){
    char choice;

    printf("(U)p (D)own (L)eft (R)ight\n? ");
    scanf("%c", &choice);
    choice = tolower(choice);

    return choice;
}
void testFile(char *fileName){
    /*WORK ON THIS 2/1*/
    printf("%s", fileName);
}
void moveUP(){
    printf("Moving up");
    /*move from bottom up so i = 4*/
}
void moveDown(){
    /*move from up to bottom so i = 0*/
    printf("Moving down");
}
void moveLeft(){
    /*move from right to left so j = 4*/
    printf("Moving Left");
}
void moveRight(){
    printf("Moving Right");
    /*move from left to right so j = 4*/
    
}
 
int main( int argc, char *argv[]){
    char ch;
    /* Check commandline args */
    if(argc == 2){
        testFile(argv[1]);
    }
    else{
        printf("New Game\n\n\n");
    }
    /* GameBoard(); */

    /* Execute direction with appropriate function */
    ch = getDirection();
    switch(ch){
        case 'u':
            moveUP();
            break;
        case 'd':
            moveDown();
            break;
        case 'l':
            moveLeft();
            break;
        case 'r':
            moveRight();
            break;
        case 'q':
            printf("Quite");
            break;
        default:
            printf("defauilt");
            break;
    }
    return 0;
}
