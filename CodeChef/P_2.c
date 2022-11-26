//Problem 2 (from codechef)
/*Chef's son wants to go on a roller coaster ride. 
The height of Chef's son is XX inches while the minimum height required to go on the ride is HH inches. 
Determine whether he can go on the ride or not.*/

#include <stdio.h>

int main() {
	int x,h,t;          //t - no of chef's sons
    scanf("%d",&t);         // h - minimum height
    for (int i = 0; i < t; i++)         //x - chef's son's height
    {
        scanf("%d %d",&x, &h);
        if (x >= h)
        {
            printf("YES\n");
        }
        else
        {
            printf("NO\n");
        }   
    }
	return 0;
}