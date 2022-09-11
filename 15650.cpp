#include <iostream>

using namespace std;
int m,n;
int arr[9];
bool used[9];
void func(int a){
    if(a==m+1) {
        for(int i=1; i<=m; i++) cout << arr[i] << " ";
        cout << '\n';
        return;
    }
    for(int i=1; i<=n; i++){
        if(used[i]) continue;
        used[i] = true;
        arr[a] = i;
        if(arr[a-1]>arr[a]) {
            used[i] = false;
            continue;
        }
        func(a+1);
        used[i] = false;
    }
}
int main(){
    cin >> n >> m;
    func(1);
}