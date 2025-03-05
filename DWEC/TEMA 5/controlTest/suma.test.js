const suma = require('./suma');
test('sumar 1 + 2 es igual a 3', () => {
    expect(suma(1, 2)).toBe(3);
});



test('agregando un numero positivo que no sea 0', () => {
    for (let a = 1; a < 10; a++) {
        for (let b = 1; b < 10; b++) {
            expect(a + b).not.toBe(0);
        }
    }
});

test('null', () => {
    const n = null;
    expect(n).toBeNull();
    expect(n).toBeDefined();
    expect(n).not.toBeUndefined();
    expect(n).not.toBeTruthy();
    expect(n).toBeFalsy();
});
//Ejemplo
test('cero', () => {
    const z = 0;
    expect(z).not.toBeNull();
    expect(z).toBeDefined();
    expect(z).not.toBeUndefined();
    expect(z).not.toBeTruthy();
    expect(z).toBeFalsy();
});


test('dos mas dos', () => {
    const value =a*x*x + b*x + c; 
    expect(value).toBeGreaterThan(3);
    expect(value).toBeGreaterThanOrEqual(3.5);
    expect(value).toBeLessThan(5);
    expect(value).toBeLessThanOrEqual(4.5);
    // toBe y toEqual son equivalentes para números
    expect(value).toBe(4);
    expect(value).toEqual(4);
});

test('no hay I en Team', () => {
    expect('team').not.toMatch(/I/);
});
//Ejemplo
test('hay "stop" en Christoph', () => {
    expect('Christoph').toMatch(/stop/);
});

//para ejecutar npx jest suma.test.js