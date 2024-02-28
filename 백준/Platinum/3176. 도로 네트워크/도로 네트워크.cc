    #include <bits/stdc++.h>

    #define X first
    #define Y second
    using namespace std;

    int n;
    int p[18][100001];
    int min_p[18][100001];
    int max_p[18][100001];
    int depth[100001];
    int visited[100001];
    vector<pair<int,int>> adj[100001];

    void bfs(int start) {
        queue<int> q;
        q.push(start);
        visited[start] = 1;
        depth[start] = 0;
        min_p[0][start] = 1e9;
        max_p[0][start] = 0;
        for(int i=1; i<=17; i++) min_p[i][start] = 1e9;
        while(!q.empty()){
            int cur = q.front(); q.pop();
            for(auto next : adj[cur]){
                if(visited[next.X] != 0) continue;
                visited[next.X] = 1;
                p[0][next.X]= cur;
                min_p[0][next.X] = next.Y;
                max_p[0][next.X] = next.Y;
                depth[next.X] = depth[cur] + 1;
                q.push(next.X);
            }
        }

        for(int i=1; i<18; i++){
            for(int j=1; j<=n; j++){
                p[i][j] = p[i-1][p[i-1][j]];
                min_p[i][j] = min(min_p[i-1][p[i-1][j]], min_p[i-1][j]);
                max_p[i][j] = max(max_p[i-1][p[i-1][j]], max_p[i-1][j]);
            }
        }
        

    }

    pair<int,int> find_lca(int x, int y ) {
        if( depth[x] < depth[y]){
            int tmp = x;
            x= y;
            y = tmp;
        }
        int min_v = 1e9;
        int max_v = 0;
        // for(int i=1; i<=17; i++){
        //     for(int j=1; j<=n; j++) cout << min_p[i][j] << " ";
        //     cout << '\n'; 
        // }
        for(int i=17; i>=0; i--){
            if(depth[x] - depth[y] >= (1<<i)){
                min_v = min(min_v, min_p[i][x]);
                // cout << i << " " <<min_v << '\n';
                //min_v = min(min_v, min_p[i][y]);
                // cout << i << " " <<min_v << '\n';
                max_v = max(max_v, max_p[i][x]);
                //max_v = max(max_v, max_p[i][y]);

                // cout << i << " " <<min_v << '\n';
                x  = p[i][x];        
            }
        }

        if (x == y) return {min_v, max_v};
        else {
            for(int i=17; i>=0; i--){
                if(p[i][x] != p[i][y]){
                    min_v = min(min_v, min_p[i][x]);
                    min_v = min(min_v, min_p[i][y]);

                    max_v = max(max_v, max_p[i][x]);
                    max_v = max(max_v, max_p[i][y]);
                    x  = p[i][x];  
                    y  = p[i][y];      
                }
            }
        }
        min_v = min(min_v, min_p[0][x]);
        min_v = min(min_v, min_p[0][y]);

        max_v = max(max_v, max_p[0][x]);
        max_v = max(max_v, max_p[0][y]);
        return {min_v, max_v};
    }
    int main() {
        cin.tie(0); ios::sync_with_stdio(0);
        cin >> n;
        int a,b,c;
        for(int i=0; i<n-1; i++){
            cin >> a >> b >> c;
            adj[a].push_back({b,c}); 
            adj[b].push_back({a,c});
        }
        //memset(visited,-1,sizeof(visited));
        for(int i=1; i<=n; i++){
            min_p[0][i] = 1e9;
        }
        bfs(1);

        // find_lca();
        int k;
        cin >> k;
        int minv,maxv;
        for(int i=0; i<k; i++){
            cin >> a >> b;
            tie(minv,maxv) = find_lca(a,b);
            cout << minv << " " << maxv << '\n';
        }
    }