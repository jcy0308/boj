#include <iostream>

using namespace std;

int n;
int arr[2500002];
int ans;
int main(){
    cin.tie(0); ios::sync_with_stdio(0);
    cin >> n;
    for(int i=1; i<=n ; i++){
        cin >> arr[i];
    }
    int k=0;
    for(int i=1; i<=n; i++){
        if(arr[i] + k != i){
            ans++; k++;
        }
    }
    cout << ans;
}