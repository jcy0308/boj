#include <iostream>
#include <queue>

using namespace std;

int n,m;
int arr[1000][1000];
int dist[1000][1000];
int max1; 
int main(){
    ios::sync_with_stdio(0); cin.tie(0);
    queue<pair<int,int>> Q;
    cin >> m >> n;
    for(int i=0; i <n; i++) fill(dist[i],dist[i]+m,-2);
    //cout << "yes";
    for(int i=0; i<n ; i++){
        for(int j=0; j<m; j++){
            cin >> arr[i][j];
            if(arr[i][j]==1) {
                Q.push({i,j});
                dist[i][j]=0;
            }
            if(arr[i][j]==-1) dist[i][j]=0;
        }
    }
    pair<int,int> cur;
    int dx[4]= {1,-1,0,0}; 
    int dy[4] = {0,0,1,-1};
    while(!Q.empty()){
        cur = Q.front(); Q.pop();
        for(int i=0; i<4 ; i++){
            int nx = cur.first + dx[i];
            int ny = cur.second + dy[i];
            if(nx >=n || ny >= m || nx <0 || ny <0) continue;
            if(arr[nx][ny]!=0 || dist[nx][ny]!=-2) continue;
            Q.push({nx,ny});
            dist[nx][ny] = dist[cur.first][cur.second] +1;
        }
        
    }
    // for(int i=0; i<n ; i++){
    //     for(int j=0; j<m; j++){
    //         cout << dist[i][j] << " ";
    //     }
    //     cout << '\n';
    // }
    max1 = dist[0][0];
    for(int i=0; i<n ; i++){
        for(int j=0; j<m; j++){
            if(dist[i][j]==-2) {
                cout << -1;
                return 0;
            }
           if(max1 < dist[i][j]) max1 = dist[i][j];
        }
    }
    cout << max1;
}