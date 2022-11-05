/*Problem 3 (codechef)
In ChefLand, human brain speed is measured in bits per second (bps). 
Chef has a threshold limit of XX bits per second above which his calculations are prone to errors. 
If Chef is currently working at YY bits per second, is he prone to errors?

If Chef is prone to errors print YES, otherwise print NO.

Input Format
The only line of input contains two space separated integers 
XX and YY — the threshold limit and the rate at which Chef is currently working at.

Output Format
If Chef is prone to errors print YES, otherwise print NO.
*/
#include<stdio.h>
int main()
{
    int x, y;
    scanf("%d %d",&x, &y);
    if (x < y)
    {
        printf("YES");
    }
    else
    {
        printf("NO");
    }
    return 0;
}