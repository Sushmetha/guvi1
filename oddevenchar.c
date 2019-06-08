#include <stdio.h>
#include <string.h>

int main(void) {
	char str[20],temp;
	scanf("%s",&str);
	int i ;
	for(i=0;i<=strlen(str);i=i+1){
		temp=str[i];
		str[i]=str[i+1];
		str[i+1]=temp;
		printf("%s",str);
		break;
		
	}
	return 0;
}
