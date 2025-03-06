enum Roles = { Admin, User }; // Admin = 0, User = 1
let user: Roles = Roles.Admin;

/*Por defecto enum inicia el valor de sus propiedades en “0...” , pero se puede modificar, en el
anterior ejemplo Admin sería 0, pero probablemente quiero que sea 1, de igual manera se pueden
modificar todos lo demás.*/
// Roles
enum Roles = { Admin = 1, User };
let user: Roles = Roles.Admin; // Ahora User será 2
// Modificando todos
enum Roles = { Admin = 1, User = 3, Guest = 0 };

// Roles
enum Roles = { Admin = 1, User, Guest };
let user: Roles = string = Roles[1];