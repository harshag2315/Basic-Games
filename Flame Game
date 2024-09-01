#include<stdio.h>

int length(char *name){
    int len=0;
    for(int i=0; name[i]!='\0'; i++){
        len+=1;
    }

    return len;
}

char * final(int count){
    if(count%5==1){
        return "Friendship";
    }
    else if (count%5==2){
        return "Love";
    }
    else if (count%5==3){
        return "Affection";
    }
    else if (count%5==4){
        return "Marriage";
    }
    else if (count%5==0){
        return "Enimes";
    }
}

char * count(char *name1, char *name2){
    int len1=length(name1);
    int len2=length(name2);
    int count=0;
    int found;

    for(int i=0; i<len1; i++){
        found=0;
        for(int j=0; j<len2; j++){
            if(name1[i]==name2[j]){
                found=1;
                break;
            }
        }
        if(!found){
            count++;
        }
    }
    for(int i=0; i<len2; i++){
        found=0;
        for(int j=0; j<len1; j++){
            if(name2[i]==name1[j]){
                found=1;
                break;
            }
        }
        if(!found){
            count++;
        }
    }

    return final(count);
}


int main(){
    char string_name_1[10000];
    char string_name_2[10000];

    printf("**Hello user, This is can help you to find your love using FLAME Game**\n\n");
    printf("Caution - Make sure to write the names in lower case only\n\n");
    printf("Enter Your Name::");
    scanf("%s", string_name_1);
    printf("Enter Your Interest Name::");
    scanf("%s", string_name_2);
    printf("\nThe Output of the game is ");
    printf("' %s '\n\n", count(string_name_1, string_name_2));

    printf("The logic used to make this game is taken from this tutorial video of pen-paper Flame game ::");
    printf("link- https://www.youtube.com/watch?v=KYHoQvmELPM");

}

/*
eg==
 hello
    01111 - 4
 harsh
    01110 - 3

 4+3=7
 5+2==flamefl - "LOVE"
*/
