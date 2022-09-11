#include <iostream>

using namespace std;

long long dp[100];
int t,n;
int main(){
    cin.tie(0); ios::sync_with_stdio(0);
    dp[0]=1; dp[1]=1; dp[2] = 1; dp[3]=2; dp[4]=2;
    for(int i=5; i<100; i++){
        dp[i] = dp[i-1] + dp[i-5];
    }
    cin >> t;
    while(t--){
        cin >> n;
        cout << dp[n-1] << '\n';
    }
    
}