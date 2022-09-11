#include <iostream>

using namespace std;
int m,n;
int arr[9];
bool used[9];

void f(int x, int y){
    if(y == m+1){
        for(int i=1; i<=m; i++) cout << arr[i] << " ";
        cout << '\n'; return;
    }
    for(int i=1; i<=x; i++){
        if(used[i]) continue;
        arr[y] = i;
        used[i] = true;
        f(x,y+1);
        used[i] = false;
    }
}
int main(){
    cin >> n >> m;
    f(n,1);


}