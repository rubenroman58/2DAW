const { convertirMayusculas,
    convertirMinusculas } = require('./archivo');
test('convertir a mayúsculas', () => {
    const resultado = convertirMayusculas('hola');
    expect(resultado).toBe('HOLA');
});
test('convertir a minúsculas', () => {
    const resultado = convertirMinusculas('HOLA');
    expect(resultado).toBe('hola');
});