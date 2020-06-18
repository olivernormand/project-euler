#include <iostream>
#include <cstdlib>
#include <cmath>
using namespace std;


int main()
{
  long limit = 1000000; // also need to change in the array :(
  long primes[1000000 + 1];

  for (long i = 0; i < limit; i++)
  {
    primes[i] = i;
  }

  long nprime = 1;
  long i = 2;

  while (i < limit)
  {
    if (primes[i] != 0)
    {
      for (long k = 2; k <= long(limit / i); k++)
      {
        primes[k*i] = 0;
      }
      cout << nprime << '\t' << primes[i] << endl;
      nprime += 1;
      i += 1;
    }
    if (primes[i] == 0)
    {
      i += 1;
    }
  }
  cout << endl;
}
