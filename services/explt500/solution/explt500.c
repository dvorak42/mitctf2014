#include <linux/fs.h>
#include <linux/init.h>
#include <linux/miscdevice.h>
#include <linux/module.h>
#include <asm/uaccess.h>

struct probe_instruction {
  uint64_t instr_num;
  uint16_t opcode;
  char data[200];
  int* (*success)(int*, struct probe_instruction);
  int* (*failure)(int*, struct probe_instruction);
};

typedef enum {
  DISCONNECTED,
  RECEIVING,
  MOVING,
  SCANNING,
} probe_status;

struct probe_info {
  probe_status status;
  char data[256];
};

uint64_t instr_counter = 0;
struct probe_info probe;

void probe_communicate(struct probe_instruction pi, int* status) {
  *status = 1;

  char secret[16];

  secret[0]  = 'A' + ((instr_counter * 23) % 26);
  secret[1]  = 'A' + ((pi.opcode * 17) % 26);
  secret[2]  = 'A' + ((pi.instr_num * 12) % 26);
  secret[3]  = 'A' + ((probe.status * 3) % 26);
  secret[4]  = 'A' + ((secret[0] + secret[1]) % 26);
  secret[5]  = 'A' + ((secret[2] + secret[3]) % 26);
  secret[6]  = 'A' + ((secret[0] + secret[2]) % 26);
  secret[7]  = 'A' + ((secret[1] + secret[3]) % 26);
  secret[8]  = 'A' + ((pi.opcode - pi.opcode) % 26);
  secret[9]  = 'A' + ((pi.opcode + pi.opcode) % 26);
  secret[10] = 'A' + ((26) % 26);
  secret[11] = 'A' + ((pi.opcode * probe.status) % 26);
  secret[12] = 'A' + ((pi.instr_num - instr_counter) % 26);
  secret[13] = 'A' + ((2) % 26);
  secret[14] = 'A' + ((0) % 26);
  secret[15] = 'A' + ((1) % 26);

  if(!strncmp(pi.data, secret, strlen(secret))) {
    probe.status = pi.opcode % 4;
    strncpy(probe.data, pi.data+16, 200 - 16);
    *status = 0;
  }
}

int* probe_success(int* status, struct probe_instruction pi) {
  printk(KERN_ERR "[NEPTUNE] Probe communication completed succesfully.\n");
}

int* probe_failure(int* status, struct probe_instruction pi) {
  printk(KERN_ERR "[NEPTUNE] Error communicating with probe.\n");
}

static ssize_t neptune_read(struct file* file, char* buf, size_t size, loff_t* offset) {
  char str[512];
  ssize_t n;
  char* status;
  if(probe.status == DISCONNECTED)
    status = "DISCONNECTED";
  else if(probe.status == RECEIVING)
    status = "RECEIVING";
  else if(probe.status == MOVING)
    status = "MOVING";
  else if(probe.status == SCANNING)
    status = "SCANNING";

  n  = sprintf(str, "Neptune Orbiter (Clock %d):\n", instr_counter);
  n += sprintf(str+n, "\tStatus: %s\n", status);
  n += sprintf(str+n, "\tCurrent Data: %s\n\n", probe.data);

  if(size < n) {
    return -EINVAL;
  }
  
  if(*offset != 0) {
    return 0;
  }
  
  if(copy_to_user(buf, str, n))
    return -EINVAL;

  *offset = n;
  return n;
}

static ssize_t neptune_write(struct file* file, const char* buf, size_t size, loff_t* offset) {
  struct probe_instruction pi;
  int* status = 0;

  pi.instr_num = instr_counter;
  instr_counter += 1;
  pi.opcode = pi.instr_num % 4;
  pi.success = probe_success;
  pi.failure = probe_failure;
  memset(pi.data, 0, 200);
  copy_from_user(pi.data, buf, size);
  //pi.success = 0xffffffff810645c7;
  //pi.failure = 0xffffffff8106430e;

  probe_communicate(pi, &status);

  if(status == 0) {
    status = pi.success(status, pi);
  }

  if(status != 0) {
    status = pi.failure(status, pi);
  }
  
  return size;
}

static const struct file_operations neptune_fops = {
  .owner = THIS_MODULE,
  .read = neptune_read,
  .write = neptune_write,
};

static struct miscdevice neptune_dev = {
  .minor = MISC_DYNAMIC_MINOR,
  .name = "neptune_orbiter",
  .fops = &neptune_fops,
};

static int __init neptune_init(void) {
  int ret = misc_register(&neptune_dev);
  if(ret)
    printk(KERN_ERR "[NEPTUNE] Error connecting to Neptune Probe\n");
  else {
    printk(KERN_ERR "[NEPTUNE] Successfully connected to Neptune Probe.\n");
    printk(KERN_ERR "[NEPTUNE] Protocol system initiated at /dev/neptune_orbiter.\n");
  }

  return ret;
}

module_init(neptune_init);

static void __exit neptune_exit(void) {
  misc_deregister(&neptune_dev);
  printk(KERN_ERR "[NEPTUNE] Disconnected from Neptune Probe.\n");
}

module_exit(neptune_exit);

MODULE_LICENSE("MIT");
MODULE_AUTHOR("John Smith <jsmith@vanqeri.com>");
MODULE_DESCRIPTION("Neptune Probe Communication Module");
MODULE_VERSION("1.0");
