#include <iostream>

using namespace std;
int n,even,odd,ans;
int arr[1000001];
bool arr2[1000004];
int main(){
    cin >> n;
    for(int i=1 ; i<=n; i++){
        cin >> arr[i];
    }
    for(int i=1 ; i<=n; i++){
        if(arr[i]%2==0) {
            arr2[i] = 0;
            even++;
            }
        else arr2[i] = 1; 
    }
   // odd = n - even;
   
        for(int i=1; i<=n ; i++){
            if(arr2[i] == 0) {  
                
            }
        }

        cout << ans;
   
}