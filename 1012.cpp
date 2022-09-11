#include <iostream>
#include <stack>

using namespace std;
int T,N,M,K;
int x,y;
bool baat[50][50];
bool vis[50][50];
int count;
int dx[4]={1,-1,0,0};
int dy[4]={0,0,1,-1};
int main(){
    ios::sync_with_stdio(0); cin.tie(0);
    cin >> T;
    stack<pair<int,int>> S;
    for(int i=0; i< T; i++){
        count =0;
        cin >> M >> N >> K;
        for(int i=0; i<50; i++) fill(baat[i], baat[i]+50, 0);
        for(int i=0; i<50; i++) fill(vis[i], vis[i]+50, 0);
        for(int j=0; j<K; j++){
            cin >> y >> x;
            baat[x][y] = true;
        } 
        for( int k=0; k<N; k++){
            for(int m=0; m<M; m++){
                if(baat[k][m] && vis[k][m]==0){
                    S.push({k,m});
                    vis[k][m]=true;
                while(!S.empty()){
                    pair<int,int> cur = S.top(); S.pop();
                    for(int l=0; l<4; l++){
                        int nx = cur.first + dx[l];
                        int ny = cur.second +dy[l];
                        if(nx <0 || nx >= N || ny <0 || ny >= M) continue;
                        if(vis[nx][ny] || baat[nx][ny]==0) continue;
                        S.push({nx,ny});
                        vis[nx][ny]=true;
                    }
                }
                count++;
                }
            }
        }
    cout << count << '\n';
    // for(int i=0; i<N; i++){
    //     for(int j=0; j<M; j++){
    //         cout << baat[i][j] << " ";
    //     }
    //     cout << '\n';
    // }
    // cout << '\n';
    // for(int i=0; i<N; i++){
    //     for(int j=0; j<M; j++){
    //         cout << vis[i][j] << " ";
    //     }
    //     cout << '\n';
    // }

    }
    
}