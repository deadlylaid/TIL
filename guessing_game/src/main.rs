extern crate rand;

use std::io;
use std::cmp::Ordering;
use rand::Rng;

fn main() {
    println!("숫자를 골라보세요!");
    
    let the_number = rand::thread_rng().gen_range(-101, 101);

    loop {
        println!("-100 부터 100 까지의 정수 중 하나를 선택하세요!");

        let mut guessed_number = String::new();

        io::stdin().read_line(&mut guessed_number).expect("값 입력에 실패했습니다!");

        let guessed_number: i32 = match guessed_number.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        match guessed_number.cmp(&the_number) {
            Ordering::Less => println!("너무 작은 숫자를 선택하셨군요!"),
            Ordering::Greater => println!("너무 큰 숫자를 선택하셨군요!"),
            Ordering::Equal => {
                println!("맞췄습니다!");
                break;
            }
        }
    }
}