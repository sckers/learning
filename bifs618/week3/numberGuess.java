
/* Week3 in-class exercise
   Name: numberGess.java
   Author: Sarah Kerscher
   Date: 01Feb21

*/

// need the Scanner class to get user input
import java.util.Scanner;

public class numberGuess {

    /**
     * @param args
     */
    public static void main(String[] args) {
        // TODO:
        //
        // a. declare a final int, and assign a value of 6 as the guessed number
       	int guess = 6;

        // b. create a Scanner to get user input
	Scanner input = new Scanner(System.in);	
        
        // c. use a do {} while loop to prompt the user to enter an integer between 1 and 10,
        //    assign the user input to an int, and compare to the guessing number
        int userInput;
        System.out.println("What number am I thinking of?\n");
        do{
           System.out.println("Enter your guess as an integer: ");
           userInput = input.nextInt();
        }
       while(userInput != guess);
        System.out.printf("%s %d.\n\n", "Correct! The number I am thinking of is",
                guess);
        
    // Here is to print your name  
    System.out.println("Author: Sarah Kerscher\n");
    }

}