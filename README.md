# 🏆 Guía Rápida · Juez Virtual UMSA

<img src="https://github.com/user-attachments/assets/942370fb-f28c-4c24-b6a4-ca810f47df1e" alt="Logo Juez Virtual" width="80" />

Registro · Inicio de sesión · Envío de soluciones · Estados del juez

---

## 📑 Índice
- [Primeros pasos](#primeros-pasos)
- [Registro de usuario](#registro-de-usuario)
- [Inicio de sesión](#inicio-de-sesión)
- [Explorar problemas](#explorar-problemas)
- [Enviar solución](#enviar-solución)
- [Estados del juez](#estados-del-juez)
- [Tips & Buenas prácticas](#tips--buenas-prácticas)

---

## 🔹 Primeros pasos

Dirígete a la página del Juez Virtual de la UMSA:  
👉 [https://jv.umsa.bo](https://jv.umsa.bo)

> 💡 Consejo: agrega el sitio a tus favoritos y revisa la hora/fecha de tu sistema antes de concursos.

<img src="https://github.com/user-attachments/assets/9a587f1b-a41f-4ab6-9429-60f5d3fa6427" alt="Página principal Juez Virtual" width="700" />

---

## 🔹 Registro de usuario

En la parte superior derecha, haz clic en **Registro**.  
Completa tus datos y usa un **correo personal válido**.  
Tu **nombre de usuario** será tu *nickname*.

<img src="https://github.com/user-attachments/assets/0bce6f80-32b7-4727-933d-7c0747c75861" alt="Formulario de registro" width="400" />

---

## 🔹 Inicio de sesión

En la parte superior derecha, selecciona **Iniciar sesión**.  
Ingresa tu **nickname** y tu **contraseña**.

<img src="https://github.com/user-attachments/assets/7d65e4fe-b9ea-4e7b-a625-88c7e9fbca24" alt="Pantalla de inicio de sesión" width="500" />

---

## 🔹 Explorar problemas

Haz clic en **Problemas** para ver el listado y selecciona uno para abrir el enunciado.

<img src="https://github.com/user-attachments/assets/25279238-48dd-4c14-8d68-bfdd46cf0504" alt="Listado de problemas" width="700" />

Cada problema incluye:

- **Descripción**: el enunciado a resolver.  
- **Entrada**: formato de los datos de entrada.  
- **Salida**: formato esperado de la respuesta.  
- **Ejemplos**: entrada y salida esperada.  

Ejemplo:

<img src="https://github.com/user-attachments/assets/267b6f86-8565-4430-b76d-bcf8e98e8fdf" alt="Detalle problema A+B" width="600" />

---

## 🔹 Enviar solución

1. Selecciona el **lenguaje de programación**.  
2. Sube tu archivo de código y confirma el envío.  
3. Serás redirigido a la **pantalla de estado**.

> 📌 **En Java:**  
> - La clase debe llamarse `Main`.  
> - El método principal debe llamarse `main`.  
> - El envío debe ser **un único archivo**.

Ejemplo de plantilla en **Java**:

```java
import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String line;
    StringBuilder out = new StringBuilder();
    while ((line = br.readLine()) != null) {
      if (line.trim().isEmpty()) continue;
      String[] p = line.trim().split("\\s+");
      long a = Long.parseLong(p[0]);
      long b = Long.parseLong(p[1]);
      out.append(a + b).append('\n');
    }
    System.out.print(out.toString());
  }
}
