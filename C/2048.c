#include <stdio.h>
#include <ctype.h> // for tolower()

int board[4][4] = {};
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
    printf("%s", fileName);
}
void moveUP(){
    printf("Moving up");
}
void moveDown(){
    printf("Moving down");
}
void moveLeft(){
    printf("Moving Left");
}
void moveRight(){
    printf("Moving Right");
}
 
int main( int argc, char *argv[]){
    char ch;
    // Check commandline args
    if(argc == 2){
        testFile(argv[1]);
    }
    else{
        printf("New Game\n\n\n");
    }
    //GameBoard();

    // Execute direction with appropriate function
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
