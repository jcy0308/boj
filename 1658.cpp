#include <bits/stdc++.h>
using namespace std;

char arr[101][101];
int vis[101][101];
int n,m;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    scanf("%d %d", &n,&m);
    getchar();
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            scanf("%c",&arr[i][j]);
        }
        getchar();
    }
    for(int i=0; i< n; i++) fill(vis[i], vis[i]+m, -1);
    // for(int i=0; i<n ; i++){
    //     for(int j=0; j<m; j++){
    //         printf("%c",arr[i][j]);
    //     }
    //     printf("\n");
    // }
    //for(int i=0; i<n; i++) printf("%c",arr[i][5]);
    queue<pair<int,int> > Q;
    int dx[4]={1,-1,0,0};
    int dy[4]={0,0,1,-1};
    pair<int, int> cur;
    vis[0][0]=0;
    Q.push({0,0});
    while(vis[n-1][m-1]==-1){
        cur = Q.front(); Q.pop();
        
        for(int i=0; i<4; i++){
            int nx = cur.first + dx[i];
            int ny = cur.second + dy[i];
           // cout << "nx= " << nx << " ny= " << ny << '\n';
            if(nx >= n || nx <0 || ny >= m || ny <0) continue; 
            if(arr[nx][ny]!= '1' || vis[nx][ny]!=-1) continue; 
            vis[nx][ny]= vis[cur.first][cur.second]+1; 
            Q.push({nx,ny});
           // cout << nx << " " << ny << '\n';
            
        }
    }
    printf("%d",vis[n-1][m-1]+1);
    //cout << vis[n-1][m-1]+1;
    return 0;
}