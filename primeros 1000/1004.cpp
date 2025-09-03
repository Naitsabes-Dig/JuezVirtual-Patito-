
#include <bits/stdc++.h>
using namespace std;

struct Node {
    int x, y, cost;
};

int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N, M;
        cin >> N >> M;

        vector<string> lab(N);
        for (int i = 0; i < N; i++) {
            cin >> lab[i];
        }

        int x1, y1, x2, y2;
        cin >> x1 >> y1;
        cin >> x2 >> y2;

        // Matriz de distancias inicializada con infinito
        vector<vector<int>> dist(N, vector<int>(M, INT_MAX));
        deque<pair<int,int>> dq;

        dist[x1][y1] = 0;
        dq.push_back({x1, y1});

        while (!dq.empty()) {
            auto [x, y] = dq.front();
            dq.pop_front();

            for (int k = 0; k < 4; k++) {
                int nx = x + dx[k];
                int ny = y + dy[k];

                if (nx < 0 || ny < 0 || nx >= N || ny >= M) continue;

                int w = (lab[nx][ny] == '#') ? 1 : 0;
                if (dist[x][y] + w < dist[nx][ny]) {
                    dist[nx][ny] = dist[x][y] + w;
                    if (w == 0)
                        dq.push_front({nx, ny}); // prioridad si no rompe pared
                    else
                        dq.push_back({nx, ny});
                }
            }
        }

        cout << "Laberinto #" << t << ": " << dist[x2][y2] << "\n";
    }

    return 0;
}
