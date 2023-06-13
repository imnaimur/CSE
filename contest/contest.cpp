#include<bits/stdc++.h>
using namespace std;


int main()
{

 int n ;
 char c;
 string s = "codeforces";
    for (int j = 0; j< n;j++){
        cin >> c;
        if (c == s[j]){
            cout<< "Yes"<< endl;
            break;
        }else{
            cout<<"No" << endl;
        }
    }
 }
