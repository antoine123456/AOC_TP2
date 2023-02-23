//
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
// DONE int -> u8
#include "types.h"
//
unsigned randxy(unsigned x, unsigned y)
{
  return (x + (rand() % y)) % y; 
}

//
int main(int argc, char **argv)
{
  //
  srand(getpid());
  
  //
  if (argc < 2)
    return printf("Usage: %s [output file] [length]\n", argv[0]), 1;

  //
  unsigned long long len = atoll(argv[2]);
  
  //
  // const char bases[4] = "ATCG"; 
  // DONE compression
  const char bases[8] = "00011011"; 
  
  //
  FILE *fp = fopen(argv[1], "wb");

  if (!fp)
    return printf("Error: cannot create file '%s'\n", argv[2]), 2;

  u8 rng;
  //Generate random DNA sequence
  // DONE modif type A -> 00, etc
  for (unsigned long long i = 0; i < len; i++){
    rng = randxy(0, 4)*2;
    fprintf(fp, "%c%c",bases[rng],bases[rng+1]);
  }

  //Newline at EOF
  fprintf(fp, "\n");
  
  //
  fclose(fp);
    
  //
  return 0;
}
