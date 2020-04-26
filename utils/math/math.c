
#include <stdio.h>
#include <math.h>

double calculateIntegrate(double f(double), double startPos, double endPos)
{
#define N 100000

    double totalArea = 0;
    double width;

    width = (endPos - startPos) / N;
    for (double i = 1; i <= N; i++)
    {
        totalArea = totalArea + f(startPos + width * i) * width;
    }
    return totalArea;
}
