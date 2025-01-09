createFrame(['a', 'bb', 'ccc', 'dddd'])
function createFrame(names) {

    let tamaño = names.reduce((ac, el) => (Math.max(ac,el.length)), 0)
    let tapa = '*'.repeat(tamaño + 4)
    let regalos = names.map((el) => '* ' + el + ' '.repeat(tamaño - el.length) + ' *').join('\n')
    return tapa + '\n' + regalos + '\n' + tapa;
}