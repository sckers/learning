/* Week2 in-class exercise
   Name: Average.java
   Author: Sarah Kerscher
   Date: 24Jan25

*/

public class Average {

	public static void main(String[] args) {

		double grade1 = 76.0;
		double grade2 = 83.0;
		double grade3 = 62.0;


		//  TO DO:
		//
		//  a.  Compute and display the average grade
		double average = (grade1 + grade2 + grade3) / 3;
                System.out.printf("%s%.1f\n\n", "Average grade: ", average);

		//  b.  Display a PASS/FAIL message
		//        average >= 75.0  PASS
		//        average <  75.0  FAIL
                if (average >= 75.0) {
                    System.out.println("Average >= 75.0  PASS");
                }
                else{
                    System.out.println("Average < 75.0  FAIL");
                }
                System.out.println("\n\nAuthor: Sarah Kerscher");
	}
}
