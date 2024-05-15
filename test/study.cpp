#include <iostream>
using namespace std;

#define max 50
struct Sqlist
{
  int data[max];
  int length = 0;
};
void init(Sqlist &s)
{
  cout << "Enter the elements of the list: ";
  for (int i = 0; i < max; i++)
  {
    cin >> s.data[i];
    s.length++;
    if (s.data[i] == -1)
    {
      s.length--;
      break;
    }
  }
}
bool listdelete(Sqlist &s)
{
  if (s.length == 0)
  {
    return false;
  }
  int min = s.data[0];
  int flag = 0;
  for (int i = 1; i < s.length; i++)
  {
    if (s.data[i] < min)
    {
      min = s.data[i];
      flag = i;
    }
    s.data[flag] = s.data[i];
  }
  s.length = s.length - 1;
  return true;
}
void print(Sqlist s)
{
  for (int i = 0; i < s.length; i++)
  {
    cout << s.data[i] << " ";
  }
  cout << endl;
}
int main()
{
  Sqlist s;
  init(s);
  listdelete(s);
  print(s);
  return 0;
}