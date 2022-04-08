/*BIFS 618
Final, Question 34
final_34.java
Sarah Kerscher
*/

import java.io.*;
import java.util.*;

public class final_34{

  private static Scanner fileScan;
  private static ArrayList<String> wordList = new ArrayList<String>();

  public static void openFile(String[] fileNames){
    for(String name : fileNames){
      try{
        fileScan = new Scanner(new File(name));
      }

      catch(Exception e){
        System.out.println("File not found");
      }
    }
  }

  public static void readWords(){
    while(fileScan.hasNext()){
      wordList.add(fileScan.next());
    }
  }

  public static void closeFile(){
    fileScan.close();
  }

  public static void main(String[] args){

    openFile(args);
    readWords();

    // print number of words in file
    System.out.printf("The file contains %d words.\n\n", wordList.size());

    // sort list and print unique words and their count
    Collections.sort(wordList);

    // for the words in the list
    for(int i = 0; i < wordList.size(); i++){
      // set our counter equal to 1 because this is the first occurrence
      int counter = 1;

      // if this isn't the first occurrence (ie this word is the same as the one
      // before it in the list) go on to the next iteration of the loop
      if(i != 0 && wordList.get(i).equals(wordList.get(i - 1))){
        continue;
      }

      // if this is the first occurrence, compare to the next word in the list
      for(int j = i + 1; j < wordList.size(); j++){
        // if these two are equal to each other, add to the counter
        if(wordList.get(i).equals(wordList.get(j))){
          counter++;
        }
      }

      // now we've found all occurrences of that word, so print it
      System.out.printf("%s, %d occurrences\n", wordList.get(i), counter);
    }

    closeFile();
  }
}
