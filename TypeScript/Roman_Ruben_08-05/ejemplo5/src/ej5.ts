interface User {
    name: string;
    age: number;
    havePets: boolean;
}
let list: any[] = [1, '2', true];
let user: User = {
    name: "Tu nombre",
    age: 29,
    havePets: true
};
console.log(list[0], user.name);