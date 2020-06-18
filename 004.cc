#include <iostream>
#include <cstdlib>
#include <cmath>
using namespace std;

void digitarray(int powersoftentrue[], int n1, int n2)
{
  int powersoftenfind[6];
  int product = n1 * n2;

  for (int i = 0; i < 6; i++)
  {
    powersoftenfind[i] = int(product * pow(10, -i));
  }
  for (int i = 0; i < 5; i++)
  {
    powersoftenfind[i] = powersoftenfind[i] - 10 * powersoftenfind[i+1];
  }
  for (int i = 0; i < 6; i++)
  {
    powersoftentrue[i] = powersoftenfind[5-i];
  }
}

bool ispalendrome(int powersoftentrue[])
{
  // find largest power of ten
  int largestpoweroften = 0;
  for (int i = 0; i < 6; i++)
  {
    if (powersoftentrue[i] != 0)
    {
      largestpoweroften = 6 - i;
      break;
    }
  }
  if (largestpoweroften == 0)
  {
    return false;
  }
  if (largestpoweroften == 1)
  {
    return true;
  }
  if (largestpoweroften == 2)
  {
    if (powersoftentrue[4] == powersoftentrue[5])
    {
      return true;
    }
    if (powersoftentrue[4] != powersoftentrue[5])
    {
      return false;
    }
  }
  if (largestpoweroften == 3)
  {
    if (powersoftentrue[3] == powersoftentrue[5])
    {
      return true;
    }
    if (powersoftentrue[3] != powersoftentrue[5])
    {
      return false;
    }
  }
  if (largestpoweroften == 4)
  {
    if (powersoftentrue[2] == powersoftentrue[5] && powersoftentrue[3] == powersoftentrue[4])
    {
      return true;
    }
    if (powersoftentrue[2] != powersoftentrue[5] || powersoftentrue[3] != powersoftentrue[4])
    {
      return false;
    }
  }
  if (largestpoweroften == 5)
  {
    if (powersoftentrue[1] == powersoftentrue[5] && powersoftentrue[2] == powersoftentrue[4])
    {
      return true;
    }
    if (powersoftentrue[1] != powersoftentrue[5] || powersoftentrue[2] != powersoftentrue[4])
    {
      return false;
    }
  }
  if (largestpoweroften == 6)
  {
    if (powersoftentrue[0] == powersoftentrue[5] && powersoftentrue[1] == powersoftentrue[4] && powersoftentrue[2] == powersoftentrue[3])
    {
      return true;
    }
    if (powersoftentrue[0] != powersoftentrue[5] || powersoftentrue[1] != powersoftentrue[4] || powersoftentrue[2] != powersoftentrue[3])
    {
      return false;
    }
  }
  return false;
}

int main()
{
  int powersoftentrue[6];
  int multiples[2];

  for (int i = 1; i < 1000; i++)
  {
    for (int j = i; j < 1000; j++)
    {
      digitarray(powersoftentrue, i, j);
      if (ispalendrome(powersoftentrue) == true)
      {
        cout << i * j << '\t' << i << '\t' << j << endl;
      }
    }
  }
}
