use std::io;

fn main() {
    println!("Guess the number!");
    println!("Please input your guess.");
    
    let mut guess = String::new(); // mutable
    let mut guess2 = String::new(); // mutable

    io::stdin().read_line(&mut guess).expect("Raised Error");
    io::stdin().read_line(&mut guess2).expect("Raised Error");

    println!("You guessed: {} and {}", guess, guess2);
}