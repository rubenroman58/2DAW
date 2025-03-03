const { expect } = require("chai"); // Importamos Chai
describe("Nombre del grupo de pruebas", function () {
    before(() => {
        // Se ejecuta UNA VEZ antes de todas las pruebas
        console.log("Antes de todas las pruebas");
    });
    after(() => {
        // Se ejecuta UNA VEZ después de todas las pruebas
        console.log("Después de todas las pruebas");
    });
    beforeEach(() => {
        // Se ejecuta antes de cada prueba individual
        console.log("Antes de cada prueba");
    });
    afterEach(() => {
        // Se ejecuta después de cada prueba individual
        console.log("Después de cada prueba");
    });
    it("Caso de prueba 1", function () {
        expect(2 + 2).to.equal(4); // Verificamos que la suma sea correcta
    });
    it("Caso de prueba 2", function () {
        expect("Hola").to.be.a("string"); // Verificamos el tipo de dato
    });
   // ejecucion: npx mocha test/math.test.js
});