
/* Week3 in-class exercise
   Name: numberGess.java
   Author: Sarah Kerscher
   Date: 01Feb21

*/

// need the Scanner class to get user input
import java.util.Scanner;

// to make the guess a random value, import the Random class
import java.util.Random;

public class randomGuess {

    /**
     * @param args
     */
    public static void main(String[] args) {
        // TODO:
        //
        // a. declare a final int, and assign a value of 6 as the guessed number
        //    We want this value to be random, so we will create a new random
        Random rand = new Random();
        
        // The random number generator provides a number from 0 to one less what
        // is in the parentheses, so here it is 0-9
       	int guess = rand.nextInt(10);
        
        // Now we need to add 1 to the guess to get the number between 1 and 10
        guess++;

        // b. create a Scanner to get user input
	Scanner input = new Scanner(System.in);	
        
        // c. use a do {} while loop to prompt the user to enter an integer between 1 and 10,
        //    assign the user input to an int, and compare to the guessing number
        int userInput;
        System.out.println("What number am I thinking of between 1 and 10?\n");
        do{
           System.out.println("Enter your guess as an integer: ");
           userInput = input.nextInt();
           // We want to tell the user in which direction to point their next guess
           if (userInput < guess){
               System.out.println("Your guess is less than the number I'm thinking of.\n");
           }
           else if(userInput > guess){
               System.out.println("Your guess is more than the number I'm thinking of.\n");
           }
        }
       while(userInput != guess);
        System.out.printf("%s %d.\n\n\n", "Correct! The number I am thinking of is",
                guess);
        
    // Here is to print your name  
    System.out.println("Author: Sarah Kerscher\n");
    }

}