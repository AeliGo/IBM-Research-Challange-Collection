
#include <stdio.h>
#include <math.h>
#include "../utils/math/math.h"

float getIntegrate(float arr[4])
{
  //nested function
  float mes(float x)
  {
    float loss = arr[0] + arr[1] * pow(x, 2) + arr[2] * pow(x, 4) + arr[3] * pow(x, 6) - fabsf(x);
    return pow(loss, 2) / 2;
  };

  return calculateIntegrate(mes, -1, 1);
}

float *getSlopes(float arr[4])
{
  static float result[4], copyArr[4];
  for (int i = 0; i < 4; i++)
  {
    copyArr[i] = arr[i];
  }
  float delta = 0.00001;

  for (int i = 0; i < 4; i++)
  {
    copyArr[i] = arr[i] + delta;

    result[i] = (getIntegrate(copyArr) - getIntegrate(arr)) / delta;

    copyArr[i] = arr[i];
  }

  return result;
}

void gradientDescent(float origin[4], float gradient[4], float step)
{
  static float result[4];
  for (int i = 0; i < 4; i++)
  {
    origin[i] = origin[i] - step * gradient[i];
  }
}

int main()
{
  float params[] = {1, 1, 1, 1};
  float *p;
  p = params;

  float *slopes = getSlopes(params);
  float previous = getIntegrate(params);

  while (getIntegrate(params) <= previous)
  {
    float new = getIntegrate(params);

    slopes = getSlopes(params);

    printf("mse is：%g", new);
    previous = new;
    gradientDescent(params, slopes, 0.1);
  }

  printf("result is:\n");
  for (int i = 0; i < 4; ++i)
  {
    printf("- %g\n", params[i]);
  }
  //0.143544, 1.2936, -0.0819361, -0.411489

  return 0;
}