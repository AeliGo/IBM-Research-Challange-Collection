#include <stdio.h>

int getGoldenRectangleNumber(int n)
{
  int i, t1 = 0, t2 = 1, nextTerm;

  for (i = 0; i <= n; ++i)
  {
    if (i == n)
    {
      return t1 * t2;
    }

    nextTerm = t1 + t2;
    t1 = t2;
    t2 = nextTerm;
  }
}

int main()
{
  int a = 0;
  a = getGoldenRectangleNumber(4);
  printf("result is：%d", a);

  return 0;
}