const gifts1 = [3, 1, 2, 3, 4, 2, 5]
const preparedGifts1 = perpareGifts(gifts1)
console.log(preparedGifts1) // [1, 2, 3, 4, 5]

function perpareGifts(gifts) {
    return [...new Set(gifts)].sort((a,b)=>(a-b))
}