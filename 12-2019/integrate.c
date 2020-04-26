
#include <stdio.h>
#include <math.h>
#include "../utils/math/math.h"

double getIntegrate(double arr[8])
{
  //nested function
  double mes(double x)
  {

    // double loss = arr[0] + arr[1] * pow(x, 2) + arr[2] * pow(x, 4) + arr[3] * pow(x, 6) - fabsf(x);
    double loss = arr[0] + arr[1] * pow(x, 2) + arr[2] / (arr[3] + arr[4] * pow(x, 2)) + arr[5] / (arr[6] + arr[7] * pow(x, 2)) - fabsf(x);
    return pow(loss, 2) / 2;
  };

  return calculateIntegrate(mes, -1, 1);
}

double *updateSlopes(double slopes[], double arr[])
{
  double copyArr[8];
  for (int i = 0; i < 8; i++)
  {
    copyArr[i] = arr[i];
  }

  double delta = 0.000001;

  for (int i = 0; i < 8; i++)
  {
    copyArr[i] = arr[i] + delta;
    slopes[i] = (getIntegrate(copyArr) - getIntegrate(arr)) / delta;
    copyArr[i] = arr[i];
  }
}

void updateParams(double origin[8], double gradient[8], double step)
{

  double d;
  double result[8];
  for (int i = 0; i < 8; i++)
  {
    d = step * gradient[i];
    origin[i] = origin[i] - d;
  }
}

double getLearningStep(double previousParams[8], double params[8], double previousSlopes[8], double slopes[8])
{
  double sum = 0, sqSum = 0;
  for (int i = 0; i < 8; i++)
  {
    sum = sum + (params[i] - previousParams[i]) * (slopes[i] - previousSlopes[i]);
    sqSum = sqSum + pow((slopes[i] - previousSlopes[i]), 2);
  }

  return fabs(sum) / sqSum;
}

double *cloneArray(double target[], double arr[])
{
  for (int i = 0; i < 8; i++)
  {
    target[i] = arr[i];
  }
}

int main()
{
  double params[8] = {1,1,1,1,1,1,1,1};
  double slopes[8] = {0,0,0,0,0,0,0,0};

  double previousParams[8] = {0,0,0,0,0,0,0,0};
  double previousSlopes[8] = {0,0,0,0,0,0,0,0};

  double step = 0.1;

  updateSlopes(slopes, params);

  while (getIntegrate(params) > 0.000003)
  {
    cloneArray(previousParams, params);
    cloneArray(previousSlopes, slopes);

    updateParams(params, slopes, step);
    updateSlopes(slopes, params);

    step = getLearningStep(previousParams, params, previousSlopes, slopes);
    double new = getIntegrate(params);

    printf("mse is：%.80lf,%.80lf\n", new, step);
  };

  for (int i = 0; i < 8; ++i)
  {
    printf("result is:%g\n", params[i]);
  }

  return 0;
}