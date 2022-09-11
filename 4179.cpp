#include <iostream>
#include <queue>

using namespace std;
int n,m;
char maze[1000][1000];
int jihun[1000][1000];
int fire[1000][1000];

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> m;
    for(int i=0; i<n; i++) fill(fire[i],fire[i]+m, -1);
    for(int i=0; i<n; i++) fill(jihun[i],jihun[i]+m, -1);
    queue<pair<int,int>> J;
    queue<pair<int,int>> F;
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            cin >> maze[i][j];
            if(maze[i][j]=='J') {
                J.push({i,j}); jihun[i][j]=0;
                if(i==0 || j==0 || i ==n-1 || j ==m-1){
                cout << 1;
                return 0;
            }      
            }
            else if(maze[i][j]=='F') {
                F.push({i,j}); fire[i][j]=0;
            }
        }
    }
    int dx[4]={1,-1,0,0};
    int dy[4]={0,0,1,-1};
    pair<int,int> cur_j, cur_f;
    while(!F.empty()){
        cur_f = F.front(); F.pop();
        for(int i=0; i<4; i++){
            int nx_f = cur_f.first + dx[i];
            int ny_f = cur_f.second +dy[i];
            if(maze[nx_f][ny_f]!='#' && nx_f >=0 && nx_f <n && ny_f >=0 && ny_f <m && fire[nx_f][ny_f]==-1){
                fire[nx_f][ny_f] = fire[cur_f.first][cur_f.second]+1; 
                F.push({nx_f,ny_f});
            }
        }
    }

    // for(int i=0; i<n; i++){
    //     for(int j=0; j<m; j++){
    //         cout << fire[i][j] << " ";
    //     }
    //     cout << '\n';
    // }
    while(!J.empty()){
        cur_j = J.front(); J.pop();
        for(int i=0; i<4; i++){
            int nx_j = cur_j.first + dx[i];
            int ny_j = cur_j.second + dy[i];
            if(nx_j <0 || nx_j >=n || ny_j <0 || ny_j >=m) continue;
            if(maze[nx_j][ny_j]=='#' || jihun[nx_j][ny_j]!=-1) continue;
            jihun[nx_j][ny_j] = jihun[cur_j.first][cur_j.second]+1;
            if((jihun[nx_j][ny_j]  >= fire[nx_j][ny_j]) && fire[nx_j][ny_j]!=-1) {
                jihun[nx_j][ny_j]--;
                continue;
            }
            J.push({nx_j,ny_j}); 
            
            
            if(nx_j==0 || ny_j==0 || nx_j ==n-1 || ny_j ==m-1){
                cout << jihun[nx_j][ny_j] +1;
                return 0;
            }       
        }
    }
                // for(int i=0; i<n; i++){
                //     for(int j=0; j<m; j++){
                //         cout << jihun[i][j] << " ";
                //     }
                //     cout << '\n';
                // }
    cout << "IMPOSSIBLE";
    return 0;

}