from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'  # Necesaria para usar flash messages

@app.route('/', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        
        # Validación de entrada
        if not nombre:
            flash('Por favor, ingresa tu nombre.', 'error')
            return redirect(url_for('formulario'))
        
        if len(nombre) < 2:
            flash('El nombre debe tener al menos 2 caracteres.', 'error')
            return redirect(url_for('formulario'))
        
        # Respuesta exitosa
        flash(f'¡Gracias, {nombre}! 🧡', 'success')
        return redirect(url_for('formulario'))
    
    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
