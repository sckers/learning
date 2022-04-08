/*
BIFS 618
Homework 4, Question 1
DNA.java
Sarah Kerscher
*/

import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.Arrays;

class DNA{
	// initialize variables
	private String seq;
	private String id;

	// build constructor
	public DNA(String id, String seq){
		this.id = id;
		this.seq = seq;
	}

	public DNA(){}

	// set the sequence to the DNA variable
	public void setSeq(String seq) {
		this.seq = seq;
	}

	// method to get the DNA string
	public String getSeq() {
		return seq;
	}

	// set ID
	public void setID(String id){
		this.id = id;
	}

	// get ID
	public String getID(){
		return id;
	}

	// method to test validity of DNA sequence
	public boolean isDNAvalid() {
		// create regex pattern
		Pattern pt = Pattern.compile("[^AGTC\s]+", Pattern.CASE_INSENSITIVE);
		// create matcher object
		Matcher mt = pt.matcher(seq);
		// look for pattern in DNA string
		return mt.find();
	}

	// method to get the length of DNA
	public double getSize() {
		double DNAlength = seq.length();
		return DNAlength;
	}

	// method to count specified bases
	public double baseCount(char nuc) {
		double nucCount = 0;
		for (int i = 0; i < seq.length(); i++) {
			if ((seq.charAt(i)) == nuc) {
				nucCount++;
			}
		}
		return nucCount;
	}

	// method for parsing the FASTA file
	public ArrayList<String[]> parseFASTA(Scanner openedFile){

		// add objects
		ArrayList<String[]> entries = new ArrayList<String[]>();
		String fileSeq = "";
		String header = "";
		entries.add(new String[]{"",""});

		// while the file has more lines
		while(openedFile.hasNextLine()){
			String newLine = openedFile.nextLine();
			if (newLine.startsWith(">")){
				// clear the seq string to start over for the next entry
				fileSeq = "";

				// overwrite the first element in the entry array with the new header
				header = newLine.trim();
			}

			// otherwise, add the line to the seq string
			else {
				fileSeq += newLine.trim();
			}

			final String header2 = header;
			entries.removeIf(entry -> entry[0].equals(header2));
			entries.add(new String[]{header, fileSeq});

		}

		// Now we should have a list of lists for each entry
		// each entry list includes the header string and the sequence string without white space
		// this list of lists will be parsed in another method to return the sequence
		return entries;
	}

	// method to get sequence based on entry id
	public String findEntry(ArrayList<String[]> entries){

		// set up objects
		Pattern p = Pattern.compile(id);
		String matchSeq = "";

		// for each entry in the array
		for (String[] entry : entries){

			// search the string for the pattern matching the input id
			// set up matcher: search first element of entry
			Matcher m = p.matcher(entry[0]);
			if (m.find()){

				// return seq exit loop on first match (there should only be one match for each id)
				matchSeq = entry[1];
				break;
			}
		}

		// return sequence
		return matchSeq;
	}

	// method to validate id in array
	public boolean findID(ArrayList<String[]> entries){
		// set boolean variable
		Boolean found = false;

		// for each entry in the array
		for(String[] entry : entries){
			// search for the id in the string
			// if the id exists in the string
			if(entry[0].contains(id)){
				// return true
				found = true;
			}
		}

		// return final boolean
		return found;
	}

	// method to break a long sequence into separate lines
	public String formatSeq(int len){

		String formattedSeq = "";
		while(seq.length() > len){
			formattedSeq += seq.substring(0, len) + "\n";
			seq = seq.substring(len);
		}

		if(seq.length() > 0){
			formattedSeq += seq;
		}

		return formattedSeq;
	}

	// method to find a feature based on input regex pattern
	// returned list is of a list with format (ID, seq, feature seq, feature start, feature end)
	public ArrayList<String[]> findFeature(String pattern, ArrayList<String[]> entries){
		// create objects
		ArrayList<String[]> featureEntries = new ArrayList<String[]>();
		//String[] featureEntry = new String[5];
		Pattern feature = Pattern.compile(pattern);

		// for each entry(sequence element) in the entries list
		for(String[] entry : entries){
			Matcher m = feature.matcher(entry[1]);

			// if the pattern is found
			if(m.find()){
				String[] featureEntry = new String[5];
				// add ID and seq to featureEntry list
				featureEntry[0] = entry[0];
				featureEntry[1] = entry[1];
				// add the match string to entry list
				featureEntry[2] = m.group();
				// add the match start position (string) to entry list
				featureEntry[3] = Integer.toString(m.start());
				// add the match end position (string) to the entry list
				featureEntry[4] = Integer.toString(m.end());
				// add the resulting entry list to a new list of entries containing feature
				featureEntries.add(featureEntry);
			}
		}

		// return the new list of entries containing the feature
		return featureEntries;
	}

	// method to annotate feature and format sequence
	public String annotateFeature(int len, String start, String end){

		String annotatedSeq = "";
		int lineStart = 1;
		int lineFeatureStart = 0;
		int lineFeatureEnd = 0;
		while(seq.length() > len){
			annotatedSeq += seq.substring(0, len) + "\n";
			if(lineStart <= Integer.parseInt(end) && lineStart + len - 1 >= Integer.parseInt(start)){
				lineFeatureStart = Math.max(0, Integer.parseInt(start) - lineStart + 1);
				lineFeatureEnd = Math.min(len, Integer.parseInt(end) - lineStart + 1);
				for(int i = 1; i <= lineFeatureStart; i++){
					annotatedSeq += " ";
				}
				for(int i = lineFeatureStart + 1; i <= lineFeatureEnd; i++){
					annotatedSeq += "*";
				}
			}
			annotatedSeq += "\n";
			seq = seq.substring(len);
			lineStart += len;
		}

		if(seq.length() > 0){
			annotatedSeq += seq + "\n";
			if(lineStart <= Integer.parseInt(end) && lineStart + len - 1 >= Integer.parseInt(start)){
				lineFeatureStart = Math.max(0, Integer.parseInt(start) - lineStart + 1);
				lineFeatureEnd = Math.min(len, Integer.parseInt(end) - lineStart + 1);
				for(int i = 1; i <= lineFeatureStart; i++){
					annotatedSeq += " ";
				}
				for(int i = lineFeatureStart + 1; i <= lineFeatureEnd; i++){
					annotatedSeq += "*";
				}
			}
			annotatedSeq += "\n";
		}

		return annotatedSeq;
	}
}
