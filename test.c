#include <stdio.h>
float *updateSlopes(float slopes[], float arr[])
{
    float copyArr[4];
    int i = 0;
    for (i = 0; i < 4; i++)
    {
        copyArr[i] = arr[i];
    }

    float delta = 0.00001;

    for (i = 0; i < 4; i++)
    {
        copyArr[i] = arr[i] + delta;

        slopes[i] = 0.5;

        // copySlopes[i] = (getIntegrate(copyArr) - getIntegrate(arr)) / delta;
        //
        copyArr[i] = arr[i];
    }
}

int main()
{
    float params[] = {1, 1, 1, 1};
    float slopes[] = {0, 0, 0, 0};

    float previousParams[4] = {0};
    float previousSlopes[4] = {0};

    float step = 0.001;

    updateSlopes(slopes, params);
    printf("params is：%g %g %g %g\n", params[0], params[1], params[2], params[3]);
    printf("slopes is：%g %g %g %g\n", slopes[0], slopes[1], slopes[2], slopes[3]);
}
