/*
an attempt at implementing the question 3 from the practice exam (just to see what it looks like)
*/
#include <stdio.h>
#include <stdlib.h>

typedef struct matrix{
	int n;
	int** pointer_array;
}matrix;

matrix* create(){
	int** pointer_array = malloc(sizeof(int*));
	pointer_array[0] = calloc(1, sizeof(int));

	matrix* new_matrix = malloc(sizeof(matrix));

	new_matrix->pointer_array = pointer_array;
	new_matrix->n = 1;
	return new_matrix;
}

void free_matrix(matrix* dyn_matrix){
	for (int i = 0; i < dyn_matrix->n; i++){
		free(dyn_matrix->pointer_array[i]);
	}

	free(dyn_matrix->pointer_array);
	free(dyn_matrix);
}

int* get_address(int** pointer_array, int i, int j){
	// accessing the row (which colour/layer you are trying to take elements from)
	
	if (i >= j)
		return &pointer_array[i][j];
	if (j > i)
		// because when you try to access the element, it "wraps around" and thus you need to skip over the initial row elements to get to the one you want
		return &pointer_array[j][j + i];
}

int get(int** dyn_matrix, int i, int j){
	return *get_address(dyn_matrix, i, j);
}

void set(int** dyn_matrix, int i, int j, int value){
	*get_address(dyn_matrix, i, j) = value;
}

void increase_size(matrix* dyn_matrix){
	dyn_matrix->pointer_array = realloc(dyn_matrix->pointer_array, ++(dyn_matrix->n));
	dyn_matrix->pointer_array[dyn_matrix->n - 1] = calloc((dyn_matrix->n) *2 + 1, sizeof(int));
}

int main(int argc, char** argv){
	matrix* my_matrix = create();
	printf("%d\n", get(my_matrix->pointer_array, 0,0));

	set(my_matrix->pointer_array, 0,0, 69);
	printf("%d\n", get(my_matrix->pointer_array, 0,0));

	increase_size(my_matrix);
	printf("%d\n", get(my_matrix->pointer_array, 0,1));
	
	set(my_matrix->pointer_array, 0, 1, 1);
	printf("%d\n", get(my_matrix->pointer_array, 0,1));
	printf("%d\n", get(my_matrix->pointer_array, 0,0));
	free_matrix(my_matrix);
	return 0;
}
