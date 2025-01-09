
function createXmasTree(height, ornament) {
    let arbol = (new Array(height)).fill(0)
    arbol = arbol.map((e, i) => '_'.repeat(height - i - 1) + (ornament.repeat(i)) + ornament + (ornament.repeat(i) + '_'.repeat(height - i - 1))).join('\n')
    let tronco = '_'.repeat(height - 1) + '#' + '_'.repeat(height - 1) + '\n'
    return arbol + '\n' + tronco +'\n'+ tronco
}
const tree3=createXmasTree(6,'@')
console.log(tree3);
