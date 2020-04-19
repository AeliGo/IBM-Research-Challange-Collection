
#include <stdio.h>
#include <math.h>

float calculateIntegrate(float f(float), float startPos, float endPos)
{
#define N 100000

    float totalArea = 0;
    float width;

    width = (endPos - startPos) / N;
    for (float i = 1; i <= N; i++)
    {
        totalArea = totalArea + f(startPos + width * i) * width;
    }
    return totalArea;
}
