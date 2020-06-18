#include <iostream>
#include <cstdlib>
#include <cmath>
using namespace std;

int main()
{
  long factorise = 600851475143;
  long largestfactor = 1;
  long i = 2;


  while (i <= factorise)
  {
    if (factorise % i == 0)
    {
      factorise = factorise / i;
      cout << i << endl;
    }
    if (factorise % i != 0)
    {
      i += 1;
    }
  }

}
