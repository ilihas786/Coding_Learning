// optional Parameters:

function calculatePrice(price: number, discount?: number): number {
    return price - (discount || 0)
}
calculatePrice(100, 10)
calculatePrice(100)

// passing the number of arguments
function sum(message: string, ...numbers: number[]): void {
    console.log(message, numbers)
}

sum("The total numbers are ", 1, 2, 3, 4)
sum("The total numbers are ", 1, 2, 3, 4, 5, 6, 6)