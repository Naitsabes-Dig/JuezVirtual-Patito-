#include <bits/stdc++.h>
using namespace std;

// DFS para recorrer la componente conectada
void dfs(char nodo, map<char, vector<char>>& grafo, set<char>& visitados) {
    visitados.insert(nodo);
    for (char vecino : grafo[nodo]) {
        if (visitados.find(vecino) == visitados.end()) {
            dfs(vecino, grafo, visitados);
        }
    }
}

int main() {
    int t;
    string linea;
    getline(cin, linea);
    t = stoi(linea);
    
    getline(cin, linea); // línea en blanco después del número de casos

    vector<int> resultados;
    int casos_leidos = 0;

    while (casos_leidos < t) {
        // Saltar líneas en blanco
        while (getline(cin, linea) && linea.empty());
        if (cin.eof()) break;

        char nodo_max = linea[0];

        // Inicializar grafo
        map<char, vector<char>> grafo;
        for (char c = 'A'; c <= nodo_max; c++) {
            grafo[c] = {};
        }

        // Leer aristas
        while (getline(cin, linea) && !linea.empty()) {
            if (linea.size() >= 2) {
                char u = linea[0], v = linea[1];
                grafo[u].push_back(v);
                grafo[v].push_back(u);
            }
        }

        // Contar componentes conectadas
        set<char> visitados;
        int componentes = 0;
        for (char c = 'A'; c <= nodo_max; c++) {
            if (visitados.find(c) == visitados.end()) {
                dfs(c, grafo, visitados);
                componentes++;
            }
        }

        resultados.push_back(componentes);
        casos_leidos++;
    }

    // Imprimir resultados con línea en blanco entre casos
    for (size_t i = 0; i < resultados.size(); i++) {
        if (i > 0) cout << endl;
        cout << resultados[i] << endl;
    }

    return 0;
}
