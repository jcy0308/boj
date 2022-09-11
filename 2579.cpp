#include <iostream>
#include <algorithm>

using namespace std;
int stairs[300];
int N;
int ans[300][2];

int main(){
    cin >> N;
    for(int i=0; i<N; i++){
        cin >> stairs[i];
    }
    ans[0][0] = stairs[0];
    ans[1][0] = stairs[1];
    
     ans[1][1] = stairs[1]+stairs[0];
    for(int i=2; i<N; i++){
        ans[i][0] = max(ans[i-2][1],ans[i-2][0]) + stairs[i];
        ans[i][1] = ans[i-1][0] + stairs[i];
       
    }
    // for(int i=0; i< N; i++) cout << ans[i][0] << " ";
    // cout << '\n';
    // for(int i=0; i< N; i++) cout << ans[i][1] << " ";
    // cout << '\n';
    // for(int i=0; i< N; i++) cout << ans[i][2] << " ";
    // cout << '\n';
    cout << max({ans[N-1][0],ans[N-1][1]});
}