#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, P;
    cin >> N >> P;

    vector<int> numeros(N);
    for (int i = 0; i < N; i++) {
        cin >> numeros[i];
    }

    unordered_map<long long, int> suma_map;
    long long suma = 0;
    for (int i = 0; i < N; i++) {
        suma += numeros[i];
        if (suma_map.find(suma) == suma_map.end()) {
            suma_map[suma] = i; // guardamos el primer índice donde ocurre la suma
        }
    }

    for (int q = 0; q < P; q++) {
        long long S;
        cin >> S;
        if (suma_map.count(S)) {
            cout << suma_map[S] << "\n";
        } else {
            cout << "No existe\n";
        }
    }

    return 0;
}
