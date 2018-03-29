#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int vert[10][10] = {
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 1, 1, 0, 0, 0, 0, 0, 0},
    {0, 0, 1, 1, 1, 0, 0, 0, 0, 0},
    {0, 0, 1, 1, 1, 0, 0, 0, 0, 0},
    {0, 0, 1, 0, 1, 0, 0, 0, 1, 0},
    {1, 0, 0, 0, 1, 0, 0, 0, 1, 0},
    {1, 0, 0, 0, 1, 0, 0, 0, 0, 0},
    {1, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
};

int clum[10][10] = {
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 1, 0, 0, 1, 1, 1, 1, 1},
    {0, 0, 1, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 1, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 1, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 1, 1, 0, 1, 1, 1, 0, 0},
    {0, 0, 0, 0, 0, 1, 1, 1, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
};

int fire(int row, int col, int board[10][10]){
    if(board[row][col] == 1){
        return 1;
    }
    return 0;
}

int strat_method(int board[10][10]){
    int hits = 0;
    for(int i = 0; i < 10; i++){
        for(int j = 0; j < 10; j++){
            int hit_miss = fire(i, j, board);
            if(hit_miss == 1){
                hits++;
                if(hits > 16){
                    return 0;
                }
            }
        }
    }
    return 1;
}

int main(int argc, char* argv[]){
    int result = strat_method(vert);
    if(result != 0){
        printf("Error occured with strategy\n");
    }
    return 0;
}
