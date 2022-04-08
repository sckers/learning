/*
BIFS 618
Homework 2, Question 1
DNA.java
Sarah Kerscher
*/

class DNA{
	// establish DNA variable
	private String DNA;

	// set the sequence to the DNA variable
	public void setDNA(String seq) {
		DNA = seq;
	}

	// method to get the DNA string
	public String getDNA() {
		return DNA;
	}

	// method to test validity of DNA sequence
	public boolean isDNAvalid() {
		// initialize and set boolean to be returned
		boolean isDNA = true;
		// set DNA to a variable
		String myDNA = getDNA();
		// list of acceptable characters
		String nucs = "agtcAGTC";
		// loop through each character in the string
		for (int i = 0; i < myDNA.length(); i++) {
			// test that character is A, G, T, C
			if (nucs.indexOf(myDNA.charAt(i)) >= 0) {
				continue;
			}
			else {
				isDNA = false;
				break;
			}
		}
		return isDNA;
	}

	// method to get the length of DNA
	public double getSize() {
		double DNAlength = getDNA().length();
		return DNAlength;
	}

	// method to count specified bases
	public double baseCount(char nuc) {
		String myStr = getDNA();
		double nucCount = 0;
		for (int i = 0; i < myStr.length(); i++) {
			if ((myStr.charAt(i)) == nuc) {
				nucCount++;
			}
			else {
				continue;
			}
		}
		return nucCount;
	}
}
