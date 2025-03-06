var Roles;
(function (Roles) {
})(Roles || (Roles = {}));
{
    Admin, User;
}
; // Admin = 0, User = 1
var user = Roles.Admin;
/*Por defecto enum inicia el valor de sus propiedades en “0...” , pero se puede modificar, en el
anterior ejemplo Admin sería 0, pero probablemente quiero que sea 1, de igual manera se pueden
modificar todos lo demás.*/
// Roles
(function (Roles) {
})(Roles || (Roles = {}));
{
    Admin = 1, User;
}
;
var user = Roles.Admin; // Ahora User será 2
// Modificando todos
(function (Roles) {
})(Roles || (Roles = {}));
{
    Admin = 1, User = 3, Guest = 0;
}
;
// Roles
(function (Roles) {
})(Roles || (Roles = {}));
{
    Admin = 1, User, Guest;
}
;
var user = string = Roles[1];
