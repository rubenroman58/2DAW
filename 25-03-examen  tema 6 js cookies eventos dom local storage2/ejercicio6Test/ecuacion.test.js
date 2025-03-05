const ecuacion = require('./ecuacion');
// importa la funcion ecuacion del modulo ecuacion 
test('ejercicio6a', () => {
    expect(ecuacion(0, 0,0,0)).toBe(0);
});
// Ejercicio 6a test para ver que ecuacion(0,0,0,0) es cero
test('ejercicio6b', () => {
    expect(ecuacion(0, 1,1,10)).toBeGreaterThan(5);
    expect(ecuacion(0, 1,1,10)).toBeLessThan(100);
   
  
});


// Ejercicio 6b test para ver que ecuacion(0,1,1,10) es mayor que 5 y menor que 100


// Ejercicio 6c test para ver que ecuacion(0,0,1,x) es uno para cualquier valor entero de x del 0 al 100

