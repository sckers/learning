/*
BIFS 618
Homework 2, Question 1
DNA.java
Sarah Kerscher
*/

import java.util.regex.Pattern;
import java.util.regex.Matcher;

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
		// set DNA to a variable
		String myDNA = getDNA();
		// create regex pattern
		Pattern pt = Pattern.compile("[^AGTC\s]+", Pattern.CASE_INSENSITIVE);
		// create matcher object
		Matcher mt = pt.matcher(myDNA);
		// look for pattern in DNA string
		return mt.find();
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
