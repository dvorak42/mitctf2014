#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <sys/types.h> 
#include <sys/socket.h>
#include <netinet/in.h>

#define BUFSIZE 1024

char flag[BUFSIZE];

int client;

int csend(const char *buf) {
  size_t len = strlen(buf);
  return write(client, buf, len);
}

int crecv(void *buf, size_t n) {
  memset(buf, 0, n);
  return read(client, buf, n);
}

void intro() {
  srand(time(0) + strlen(flag));
  csend("Welcome to the Outer Oort Cloud Survey Console.\n");
  csend("We hope you enjoy your stay.\n");
}

void show_time_travel() {
  csend("Time Travel Data:\n");
  char buf[BUFSIZE]; 
  memset(buf, 0, sizeof(buf));
  sprintf(buf, "\tThe probe has traveled for %d.%d seconds.\n\n", time(0), rand());
  csend(buf);
}

void show_space_travel() {
  srand(rand());
  csend("Space Travel Data:\n");
  char buf[BUFSIZE];
  memset(buf, 0, sizeof(buf));
  sprintf(buf, "\tThe probe has traveled for %d.%d miles.\n\n", rand(), rand());
  csend(buf);
}

int menu() {
  csend("Please make a selection from the following menu:\n");
  csend("\t1) Time Travel Data\n");
  csend("\t2) Space Travel Data\n");
  csend("\t3) Show Admin Password\n");
  csend("\t4) Quit\n");
  csend("> ");
  char buf[BUFSIZE];
  int clen = crecv(buf, BUFSIZE);
  if(clen == 0)
    return 0;
  return atoi(buf);
}

void handle(int sock, struct sockaddr_in client_address) {
  char* hostaddr = inet_ntoa(client_address.sin_addr);
  char buf[BUFSIZE];
  client = sock;

  intro();

  while(1) {
    int choice = menu();
    if(choice == 0) {
      exit(0);
    } else if(choice == 1) {
      show_time_travel();
    } else if(choice == 2) {
      show_space_travel();
    } else if(choice == 3) {
      sprintf(buf, "Please enter your backup code: ");
      csend(buf);
      crecv(buf, BUFSIZE);
      int x = atoi(buf);
      if(x == rand()) {
	sprintf(buf, "Password: %s", flag);
	csend(buf);
      }
      int k = 0;
      while((k = rand() % 3) != 0) {
	if(k == 1) {
	  show_time_travel();
	} else {
	  show_space_travel();
	}
      }
      sprintf(buf, "Error, error, error.\n");
    }
  }
}

int main(int argc, char *argv[]) {
  int server_socket, client_socket, client_addr_len;
  struct sockaddr_in server_addr, client_addr;

  if (argc != 2) {
    fprintf(stderr, "usage: %s <port>\n", argv[0]);
    exit(1);
  }

  FILE* fp;
  fp = fopen("flag", "r");
  if(fp != NULL) {
    char c;
    memset(flag, 0, sizeof(flag));
    while((c = getc(fp)) != EOF) {
      strncat(flag, &c, 1);
    }
    fclose(fp);
  }
  fprintf(stdout, "Flag: %s", flag);
  server_socket = socket(AF_INET, SOCK_STREAM, 0);
  int optval = 1;
  setsockopt(server_socket, SOL_SOCKET, SO_REUSEADDR, (const void *)&optval , sizeof(int));
  memset((char*)&server_addr, 0, sizeof(server_addr));
  server_addr.sin_family = AF_INET;
  server_addr.sin_addr.s_addr = INADDR_ANY;
  server_addr.sin_port = htons(atoi(argv[1]));
  bind(server_socket, (struct sockaddr*)&server_addr, sizeof(server_addr));
  listen(server_socket, 5);
  client_addr_len = sizeof(client_addr);
  while(1) {
    int client_socket = accept(server_socket, (struct sockaddr*)&client_addr, &client_addr_len);
    if (client_socket < 0) {
      continue;
    }

    int pid = fork();
    if(pid == 0) {
      close(server_socket);
      handle(client_socket, client_addr);
      exit(0);
    } else {
      close(client_socket);
    }
  }
  exit(0);
}

