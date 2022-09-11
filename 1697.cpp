#include <iostream>
#include <queue>

using namespace std;

int subin[200002];
int dist[100001];
int n,k;
int main(){
    fill(dist,dist+100001,-1);
    cin >> n >> k;
    queue<int> Q;
    dist[n]=0;
    Q.push(n);
    int cur;
    while(dist[k]==-1){
        cur = Q.front(); Q.pop();
        int next = cur +1;
        if(dist[next] ==-1) {
        Q.push(next); 
        dist[next] = dist[cur]+1;
        }
        next = cur -1 ;
        if(next >=0 && dist[next] == -1){
            dist[next] = dist[cur] + 1;
            Q.push(next);
        }
        next = 2*cur;
        if(dist[next]==-1 && next <=100000){
            dist[next] = dist[cur] + 1;
            Q.push(next);
        }
    }
    cout << dist[k];
    return 0;


}