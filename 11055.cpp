#include <iostream>
#include <algorithm>

using namespace std;
int n;
int arr[1001];
int d[1001];

int main(){
    cin >> n;
    for(int i=0; i<n; i++) {
        cin >> arr[i];
        d[i]=arr[i];
    }
    for(int i=0; i<n; i++){
        for(int j=0; j<i; j++){
            if(arr[j] < arr[i]) d[i] = max(d[i], d[j] + arr[i]);
        }
        
    }
    // for(int i=0; i<n; i++){
    //     cout << d[i] << " ";
    // }
    cout << *max_element(d,d+n);
}