#include <iostream>
#include <queue>
#include <stack>

using namespace std;

char s[101][101];
bool vis[101][101];
int n;
int dx[4]={1,-1,0,0};
int dy[4]={0,0,1,-1};

void bfs(int N){
    queue<pair<int,int>> Q;
    int count = 0 ;
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            if(vis[i][j]) continue;
            Q.push({i,j});
            vis[i][j]=true;
            while(!Q.empty()){
                pair<int,int> cur = Q.front(); Q.pop();
                for(int k=0; k<4; k++){
                    int nx = cur.first + dx[k];
                    int ny = cur.second + dy[k];
                    if(nx <0 || nx >=N || ny <0 || ny>=N ) continue;
                    if(s[nx][ny]!=s[cur.first][cur.second] || vis[nx][ny] ) continue;
                    Q.push({nx,ny}); vis[nx][ny]=true;
                }
            }
            count++;
        }
    }
    cout << count << " ";
}
void dfs(int N){
    stack<pair<int,int>> st;
    int count =0;
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            if(vis[i][j]) continue;
            st.push({i,j});
            vis[i][j]=true;
            while(!st.empty()){
                pair<int,int> cur = st.top(); st.pop();
                if(s[cur.first][cur.second]=='B'){
                    for(int k=0; k<4; k++){
                        int nx = cur.first + dx[k];
                        int ny = cur.second +dy[k];
                        if(nx <0 || nx >=N || ny <0 || ny>=N) continue;
                        if(s[nx][ny]!=s[cur.first][cur.second] || vis[nx][ny]) continue;
                        st.push({nx,ny}); vis[nx][ny]=true;
                    }
                }
                else if(s[cur.first][cur.second]=='R' || s[cur.first][cur.second]=='G'){
                    for(int k=0; k<4; k++){
                        int nx = cur.first + dx[k];
                        int ny = cur.second +dy[k];
                        if(nx <0 || nx >=N || ny <0 || ny>=N) continue;
                        if(s[nx][ny]=='B' || vis[nx][ny]) continue;
                        st.push({nx,ny}); vis[nx][ny]=true;
                    }
                }
            }
            count++;         
        } 
    }
        cout << count ;
}

int main(){
    ios::sync_with_stdio(0); cin.tie(0);
    cin >> n;
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cin >> s[i][j];
        }   
    }
    bfs(n);
    for(int i=0; i<n; i++) fill(vis[i],vis[i]+n,0);
    dfs(n);
    return 0;    
}