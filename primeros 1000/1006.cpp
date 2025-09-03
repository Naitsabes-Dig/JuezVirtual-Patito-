#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    cin.ignore(); // limpiar salto de línea

    for (int t = 0; t < T; t++) {
        string s;
        getline(cin, s);

        string res = "";
        bool mayus = true; // empezamos con mayúscula

        for (char c : s) {
            if (isalpha(c)) { // solo alternamos en letras
                if (mayus) {
                    res.push_back(toupper(c));
                } else {
                    res.push_back(tolower(c));
                }
                mayus = !mayus; // alternamos
            } else {
                // espacios u otros caracteres se copian tal cual
                res.push_back(c);
            }
        }

        cout << res << "\n";
    }

    return 0;
}
