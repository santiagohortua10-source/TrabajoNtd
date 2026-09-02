from flask import Flask, jsonify, render_template, request


app = Flask(__name__)

# Base de datos simulada de productos tecnológicos (con stock)
PRODUCTOS = [
    {
        "id": 1,
        "nombre": "Quantum Phone S",
        "descripcion": "5G, 1TB, Pantalla OLED. Potencia y rendimiento.",
        "precio": "3.899.900",
        "icono": "📱",
        "stock": 12
    },
    {
        "id": 2,
        "nombre": "GPU Nova RX 900",
        "descripcion": "Gama alta, 8K, Ray Tracing para gaming y renderizado.",
        "precio": "7.199.900",
        "icono": "💻",
        "stock": 5
    },
    {
        "id": 3,
        "nombre": "Aura Noise-Canceling",
        "descripcion": "Alta Res, ANC, Batería 40h para largas sesiones.",
        "precio": "2.149.900",
        "icono": "🎧",
        "stock": 20
    },
    {
        "id": 4,
        "nombre": "SmartWatch Pulse X",
        "descripcion": "Monitor cardíaco, GPS integrado y batería de 7 días.",
        "precio": "1.299.900",
        "icono": "⌚",
        "stock": 8
    },
    {
        "id": 5,
        "nombre": "TabletPro 12 Ultra",
        "descripcion": "Pantalla 12'', lápiz incluido, ideal para diseño y estudio.",
        "precio": "4.599.900",
        "icono": "📲",
        "stock": 7
    },
    {
        "id": 6,
        "nombre": "Teclado Mecánico Volt",
        "descripcion": "Switches rojos, retroiluminado RGB, diseño ergonómico.",
        "precio": "459.900",
        "icono": "⌨️",
        "stock": 30
    },
    {
        "id": 7,
        "nombre": "Cámara ActionCam 4K",
        "descripcion": "Resistente al agua, estabilización óptica, ideal para deportes.",
        "precio": "899.900",
        "icono": "📷",
        "stock": 15
    },
    {
        "id": 8,
        "nombre": "Parlante Boom Bass",
        "descripcion": "Sonido 360°, resistente al agua, batería de 20 horas.",
        "precio": "649.900",
        "icono": "🔊",
        "stock": 18
    },
    {
        "id": 9,
        "nombre": "Router MeshNet AX",
        "descripcion": "WiFi 6, cobertura total del hogar, configuración por app.",
        "precio": "749.900",
        "icono": "📡",
        "stock": 10
    },
    {
        "id": 10,
        "nombre": "Monitor UltraWide 34\"",
        "descripcion": "Curvo, 144Hz, ideal para gaming y productividad.",
        "precio": "2.899.900",
        "icono": "🖥️",
        "stock": 6
    }
]


@app.route('/')
def inicio():
    # Renderiza la interfaz gráfica y le pasa los productos (con su stock)
    return render_template('index.html', productos=PRODUCTOS)


@app.route('/api/productos')
def api_productos():
    # Endpoint (GET) JSON por si otra app necesita los datos
    return jsonify({"estado": "exito", "datos": PRODUCTOS})

#METODO POST
@app.route('/api/productos/<int:producto_id>/comprar', methods=['POST'])
def comprar_producto(producto_id):
    # Compra 1 unidad del producto indicado: descuenta su stock
    for producto in PRODUCTOS:
        if producto['id'] == producto_id:
            if producto['stock'] <= 0:
                return jsonify({"estado": "error", "mensaje": "Sin stock disponible"}), 400
            producto['stock'] -= 1
            return jsonify({"estado": "exito", "datos": producto})
    return jsonify({"estado": "error", "mensaje": "Producto no encontrado"}), 404


#METODO PUT 
@app.route('/api/productos/<int:producto_id>', methods=['PUT'])
def reemplazar_producto(producto_id):
    datos = request.get_json()

    campos_requeridos = [
        'nombre',
        'descripcion',
        'precio',
        'icono',
        'stock'
    ]

    for campo in campos_requeridos:
        if campo not in datos:
            return jsonify({
                "estado": "error",
                "mensaje": f"Falta el campo: {campo}"
            }), 400

    for producto in PRODUCTOS:
        if producto['id'] == producto_id:
            producto['nombre'] = datos['nombre']
            producto['descripcion'] = datos['descripcion']
            producto['precio'] = datos['precio']
            producto['icono'] = datos['icono']
            producto['stock'] = datos['stock']

            return jsonify({
                "estado": "exito",
                "mensaje": "Producto actualizado correctamente",
                "datos": producto
            })

    return jsonify({
        "estado": "error",
        "mensaje": "Producto no encontrado"
    }), 404



#METODO DELETE
@app.route('/api/productos/<int:producto_id>', methods=['DELETE'])
def eliminar_producto(producto_id):
    # Elimina el producto indicado
    for producto in PRODUCTOS:
        if producto['id'] == producto_id:
            PRODUCTOS.remove(producto)

            return jsonify({
                "estado": "exito",
                "mensaje": "Producto eliminado correctamente",
                "datos": producto
            })

    return jsonify({
        "estado": "error",
        "mensaje": "Producto no encontrado"
    }), 404


if __name__ == '__main__':
    # host='0.0.0.0' permite acceder desde otros dispositivos en tu red
    app.run(debug=True, host='0.0.0.0', port=5000)