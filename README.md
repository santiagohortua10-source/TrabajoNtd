
---

## 0. Clonar el repositorio y abrirlo en VSCode

1. Si no tienes Git instalado, descárgalo de [git-scm.com](https://git-scm.com/) e instálalo.
2. Abre una terminal (o la terminal integrada de VSCode) en la carpeta donde
   quieras guardar el proyecto (ej. `C:\` o `Documentos`).
3. Clona el repositorio:
```bash
   git clone https://github.com/santiagohortua10-source/TrabajoNtd.git
```
   Esto crea una carpeta llamada `TrabajoNtd` con todo el código.
4. Abre VSCode, ve a **File > Open Folder** (Archivo > Abrir carpeta) y
   selecciona la carpeta `TrabajoNtd` que se acaba de crear.

   Alternativa más rápida: desde la terminal, entra a la carpeta y abre
   VSCode directamente:
```bash
   cd TrabajoNtd
   code .
```

Continúa con el paso 1 para dejar el proyecto corriendo.

---

## 1. Abrir el proyecto en VSCode

1. Descomprime el proyecto en la carpeta donde guardas tus trabajos (ej. `C:\TareaNTD`).
2. Abre VSCode y ve a **File > Open Folder** (Archivo > Abrir carpeta), selecciona esa carpeta.
3. Abre una terminal integrada: **Terminal > New Terminal**.
4. Crea un entorno virtual (solo la primera vez):
```bash
   python -m venv .venv
```
5. Actívalo:
   - **Windows (PowerShell):** `.venv\Scripts\Activate.ps1`
   - **Windows (cmd):** `.venv\Scripts\activate.bat`
   - **Mac/Linux:** `source .venv/bin/activate`

   Sabrás que funcionó porque aparece `(.venv)` al inicio de la línea. Si VSCode
   pregunta si quieres usar ese entorno como intérprete, di que sí (o hazlo
   manualmente con `Ctrl+Shift+P` → *Python: Select Interpreter*).
6. Instala las dependencias:
```bash
   pip install -r requirements.txt
```
7. Ejecuta la aplicación:
```bash
   python app.py
```
   Debe aparecer algo como `Running on http://127.0.0.1:5000`.
8. Abre [http://localhost:5000](http://localhost:5000) en tu navegador para ver el catálogo.

Deja esa terminal abierta mientras trabajas — si la cierras, el servidor se apaga.

---

## 2. Endpoints disponibles

| Método | Ruta                          | Descripción                                   |
|--------|-------------------------------|------------------------------------------------|
| GET    | `/`                           | Página principal (HTML)                         |
| GET    | `/api/productos`              | Lista de productos con su stock, en JSON        |
| POST   | `/api/productos/<id>/comprar` | Compra 1 unidad del producto y descuenta stock  |

> El stock se guarda **en memoria**: si reinicias el servidor, vuelve a los
> valores iniciales.

---

## 3. Probar la API desde Postman

Con el servidor corriendo (`python app.py`), abre Postman y prueba lo siguiente:

### GET /api/productos
- Método: `GET`
- URL: `http://127.0.0.1:5000/api/productos`
- Sin body.
- Respuesta esperada (200): JSON con los 10 productos, cada uno con su campo `stock`.

### POST /api/productos/{id}/comprar
- Método: `POST`
- URL: `http://127.0.0.1:5000/api/productos/1/comprar` (cambia el `1` por el id que quieras)
- Sin body ni headers especiales.
- Respuesta esperada (200):
```json
  {
      "estado": "exito",
      "datos": { "id": 1, "nombre": "Quantum Phone S", "...": "...", "stock": 11 }
  }
```
- Si repites la misma petición, el stock sigue bajando cada vez.

### Casos de error para probar
- **Sin stock (400):** sigue comprando el mismo producto hasta llegar a 0 unidades.
```json
  { "estado": "error", "mensaje": "Sin stock disponible" }
```
- **Producto inexistente (404):** prueba con un id que no exista, ej. `http://127.0.0.1:5000/api/productos/999/comprar`.
```json
  { "estado": "error", "mensaje": "Producto no encontrado" }
```

> Nota: como el stock vive en el mismo servidor, si compras desde Postman
> mientras tienes la página abierta en el navegador, el navegador no se
> entera del cambio hasta que recargues (F5) — solo actualiza el número
> cuando tú haces clic en su propio botón "Comprar".
