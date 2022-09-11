#include <iostream>

using namespace std;
int n,a,b;
int ans = 1001;
int main(){
    cin >> n;
    while(n--){
        cin >> a >> b;
        if(a <= b) ans = min(b, ans);
    }
    if(ans==1001) cout << -1;
    
    else cout << ans;
}