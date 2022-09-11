#include <iostream>

using namespace std;

int N; 
int tmp;
int num[11];
int main(){
    num[1]=1; num[2]=2; num[3]=4;
    for(int i=4; i<11; i++){
        num[i]=num[i-1] + num[i-2] + num[i-3];
    }
    cin >> N;
    int* arr = (int*)malloc(sizeof(int)*N);
    for(int i=0; i<N; i++){
        cin >> arr[i];
            }
    for(int i=0; i<N; i++)
    cout << num[arr[i]] << '\n';


}