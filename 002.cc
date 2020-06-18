#include <iostream>
#include <cstdlib>
#include <cmath>
using namespace std;

int main()
{
  int n0, n1, n2, placeholder, answer;
  n1 = 1;
  n2 = 1;
  answer = 0;

  while (n2 < 4000000)
  {
    n0 = n1;
    n1 = n2;
    n2 = n0 + n1;
    if (n2 % 2 == 0)
    {
      answer += n2;
    }
  }

  cout << answer << endl;
}
