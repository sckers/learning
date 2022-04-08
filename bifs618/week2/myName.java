/* Week2 in-class exercise
   Name: myName.java
   Author: Sarah Kerscher
   Date: 24Jan21

*/

//import the Scanner class to get user input
import java.util.Scanner;
public class myName {

	public static void main(String[] args) {

		//  TO DO:
		//
		//  a. Create a new Scanner to get user input
		Scanner userInput = new Scanner(System.in);	

		//  b. Prompt the user to get the name
		System.out.println("\nEnter your name:");

		//  c. Get user's name input and assigned to a name variable
                String userName;
                userName = userInput.nextLine();

		//  d. Display a welcome message, such as:
		//  "Hello, name, welcome to BIFS618!" 
		System.out.printf("\n%s, %s, %s!\n", "Hello", userName, "welcome to BIFS618");
                System.out.println("\n\nAuthor: Sarah Kerscher");


	}
}
