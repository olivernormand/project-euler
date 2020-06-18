#include <iostream>
#include <cstdlib>
#include <cmath>
using namespace std;

int main()
{
  int n = 100;
  int sum = 0;

  for (int i = 0; i <= n; i++)
  {
    sum += i ;
  }
  int squareofsum = pow(sum, 2);

  int sumofsquare = 0;

  for (int i = 0; i <= n; i++)
  {
    sumofsquare += pow(i,2);
  }

  cout << "Sum of Square" << '\t' << sumofsquare << endl;
  cout << "Square of Sum" << '\t' << squareofsum << endl;
  cout << "Difference" << '\t' << squareofsum - sumofsquare << endl;
}
