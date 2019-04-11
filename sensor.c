#include <stdio.h>
#include <stdlib.h>
#include <math.h>

//Compile as gcc file.c -lm

int function(long int *current, long int *voltage)
{
    //printf("current: %ld voltage: %ld\n", *current, *voltage);
    int wc = 2;
    int wv = 3;
    int b = 1;
    int cur = *current;
    int vol = *voltage;
    FILE* fp;

    int result = wc * cur + wv * vol + b;

    float tan_value = tan(result);
    printf("The value of tan(%d) : %f\n", result, tan_value);

    //Write the results to an outfile
    fp = fopen("out.txt", "a");
    fprintf(fp, "%f\n",tan_value);
    fclose(fp);
}

int main() {

    char ch, file_name[25];
    printf("Enter name of a file you wish to see\n");
    scanf("%s", file_name);

    FILE* fp;

    fp = fopen(file_name, "r");

    if (fp == NULL)
    {
        perror("Error while opening the file.\n");
        exit(EXIT_FAILURE);
    }

    char* line = NULL;
    size_t len = 0;
    char * pEnd;
    long int cur, vol, sc, ref;

    while ((getline(&line, &len, fp)) != -1) {
        // using printf() in all tests for consistency
        cur = strtol (line, &pEnd, 10);
        vol = strtol (pEnd, &pEnd, 10);
        sc = strtol (pEnd, &pEnd, 10);
        ref = strtol (pEnd, &pEnd, 10);
        //printf("%s", line);
        //printf("current: %ld voltage: %ld\n", cur, vol);
        function(&cur,&vol);
    }
    fclose(fp);

    if (line)
        free(line);
}
