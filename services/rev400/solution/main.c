#include <limits.h>
#include <signal.h>
#include <stdio.h>
#ifdef DEBUG
#define PTRACE_TRACEME 1

int ptrace(int a, int b, int c, int d) {
  return 0;
}

int getuid() {
  return 7331;
}

int getgid() {
  return 7331;
}
#else
#include <sys/ptrace.h>
#endif

int secret_key_generation(int seed) {
  int x1 = ptrace(PTRACE_TRACEME, 0, 1, 0)+1;
  int x2 = getuid();
  int x3 = getgid();
  unsigned int x = (x1+x2+x3+(x1^x2^x3)+(x1+x2^x3)+(x2+x1^x3)+(x3+x2^x1))^seed;
  srandom(x);
  return (int)(random()^x);
}


int main(int argc, char* argv[]) {
  if(ptrace(PTRACE_TRACEME, 0, 1, 0) == -1 || getuid() > USHRT_MAX || getgid() > USHRT_MAX) {
    while(1 + ptrace(PTRACE_TRACEME, 0, 1, 0) != 1) {
      __asm__("int3");
    }
    printf(":(\n");
    return 1;
  }
  char buf[16];
  gets(buf);
  printf("You typed: %s\n", buf);
  printf("The flag is: \n");
  int seed = 0;
  int i = 0;
  int d[] = {1298165448, 975234962, 1922453638, 133188808, 1634540227, 1541428002, 1597339749, 489593553, 1653068183, 253378686, 445278496, 848061202, 874033590, 200235642, 1699478674, 832188216, 1683112182, 2000177300, 1548754852, 292453822, 441896655, 910965363, 1075993314, 1754000221, 1434661660, 1592388006, 751713007, 1743910400, 1912252329, 1828805036, 1443471142, 896016015, 1910730046, 28780289, 758459117, 1830298973, 2038583381, 1629798134, 1472104855, 847982605, 1095812447, 883289254};
  while(i < sizeof(d)/sizeof(int)) {
    seed = secret_key_generation(seed);
    printf("%c", seed^d[i]);
    i += 1;
  }
  printf("\n");
}
